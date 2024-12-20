import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def calculate_metrics(schedule):
    # Ensure distance is a float and pickup_time is a datetime
    schedule['distance'] = schedule['distance'].astype(float)
    schedule['pickup_time'] = pd.to_datetime(schedule['pickup_time'])

    metrics = {}

    # Calculate the number of rides for each asset
    num_rides_per_asset = schedule['asset'].value_counts().to_dict()

    # Calculate Mile Efficiency (variance of distances per asset)
    mile_efficiency = (
        schedule.groupby('asset')['distance'].apply(lambda x: x.var() * len(x) / num_rides_per_asset[x.name]).fillna(0).to_dict()
    )

    # Calculate Time Efficiency (standard deviation of pickup times per asset in minutes)
    schedule['pickup_minutes'] = schedule['pickup_time'].dt.hour * 60 + \
                                 schedule['pickup_time'].dt.minute + \
                                 schedule['pickup_time'].dt.second / 60
    time_efficiency = (
        schedule.groupby('asset')['pickup_minutes'].apply(lambda x: x.std() * len(x) / num_rides_per_asset[x.name]).fillna(0).to_dict()
    )

    # Calculate Average Closeness (average distance between consecutive rides per asset)
    def calculate_average_closeness(group):
        distances = group.sort_values('pickup_time')['distance'].values
        if len(distances) < 2:
            return 0
        return np.mean(np.abs(np.diff(distances))) * len(distances) / num_rides_per_asset[group.asset.iloc[0]]

    average_closeness = (
        schedule.groupby('asset').apply(calculate_average_closeness).to_dict()
    )

    metrics['mile_efficiency'] = mile_efficiency
    metrics['time_efficiency'] = time_efficiency
    metrics['average_closeness'] = average_closeness

    # Calculate Asset Downtime (time between consecutive pickups)
    def calculate_asset_downtime(schedule):
        # Ensure pickup_time is a datetime object
        schedule['pickup_time'] = pd.to_datetime(schedule['pickup_time'])
        
        # Sort the data by asset and pickup time
        schedule = schedule.sort_values(by=['asset', 'pickup_time'])
        
        # Calculate downtime between consecutive pickups for each asset
        schedule['downtime'] = schedule.groupby('asset')['pickup_time'].diff().dt.total_seconds() / 3600  # downtime in hours
        
        # We want to calculate average downtime per asset (higher downtime is worse)
        downtime_per_asset = schedule.groupby('asset')['downtime'].apply(lambda x: x.mean() * len(x) / num_rides_per_asset[x.name]).fillna(0)  # Use 0 for the first ride of each asset

        return downtime_per_asset

    # Adding downtime metric to the metrics
    downtime_per_asset = calculate_asset_downtime(schedule)
    metrics['asset_downtime'] = downtime_per_asset.to_dict()

    # Calculate scores for each metric
    scores = {}

    # Mile Efficiency Score (lower is better, ideal is 0)
    scores['mile_efficiency_score'] = {asset: 0 if value == 0 else value for asset, value in mile_efficiency.items()}

    # Time Efficiency Score (lower is better, ideal is 0)
    scores['time_efficiency_score'] = {asset: 0 if value == 0 else value for asset, value in time_efficiency.items()}

    # Average Closeness Score (lower is better, ideal is 0)
    scores['average_closeness_score'] = {asset: 0 if value == 0 else value for asset, value in average_closeness.items()}

    # Pickup Times Score: Ideally close together, so the smaller the better (we use the average of differences for this)
    def calculate_pickup_times_score(group):
        pickup_times = group['pickup_minutes'].values
        if len(pickup_times) < 2:
            return 0
        diffs = np.abs(np.diff(pickup_times))
        return np.mean(diffs) * len(pickup_times) / num_rides_per_asset[group.asset.iloc[0]]
    
    pickup_times_score = schedule.groupby('asset').apply(calculate_pickup_times_score).to_dict()

    scores['pickup_times_score'] = pickup_times_score

    return metrics, scores
def normalize_scores(scores):
    normalized_scores = {}
    for metric_name, metric_data in scores.items():
        min_score = min(metric_data.values())
        max_score = max(metric_data.values())

        # Normalize each score (lower is better, so we reverse the scaling)
        normalized_scores[metric_name] = {
            asset: (score - min_score) / (max_score - min_score) if max_score != min_score else 0
            for asset, score in metric_data.items()
        }
    return normalized_scores

def calculate_bottom_line_score(normalized_scores):
    bottom_line_scores = {}
    for asset in normalized_scores['mile_efficiency_score'].keys():
        # Average of all normalized scores for each asset
        scores_for_asset = [
            normalized_scores['mile_efficiency_score'][asset],
            normalized_scores['time_efficiency_score'][asset],
            normalized_scores['average_closeness_score'][asset],
            normalized_scores['pickup_times_score'][asset]
        ]
        bottom_line_scores[asset] = np.mean(scores_for_asset)
    return bottom_line_scores

def calculate_variance_scalars(metrics, scores=None):
    variance_scalars = {}

    # Variance for raw metrics (distance, pickup time, etc.)
    for metric_name, metric_data in metrics.items():
        variance_scalars[metric_name] = np.var(list(metric_data.values()))
    
    # Variance for scores (mile_efficiency_score, time_efficiency_score, etc.)
    if scores:
        for score_name, score_data in scores.items():
            variance_scalars[score_name] = np.var(list(score_data.values()))
    
    return variance_scalars

def print_variance_scalars(variance_scalars):
    print("\nVariance (measures variability of each metric and score):")
    for metric_name, variance in variance_scalars.items():
        print(f"{metric_name.replace('_', ' ').title()}: {variance:.4f}")

def plot_scatter_pickup_times(schedule):
    # Ensure pickup time is in minutes
    schedule['pickup_minutes'] = schedule['pickup_time'].dt.hour * 60 + \
                                 schedule['pickup_time'].dt.minute + \
                                 schedule['pickup_time'].dt.second / 60

    plt.figure(figsize=(10, 6))
    for asset in schedule['asset'].unique():
        asset_data = schedule[schedule['asset'] == asset]
        plt.scatter([asset] * len(asset_data), asset_data['pickup_minutes'], alpha=0.6, label=f"Asset {asset}")
    
    plt.title('Pickup Times by Asset')
    plt.xlabel('Asset')
    
    # Set y-axis from 0 to 1440 (minutes in a day)
    plt.ylabel('Pickup Time (HH:MM)')
    plt.ylim(0, 1440)
    
    # Set the y-axis ticks to be in hours and minutes format
    def time_formatter(x, pos):
        return f'{int(x // 60):02d}:{int(x % 60):02d}'
    
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(time_formatter))
    
    plt.xticks(rotation=45)
    
    # Move legend outside the plot
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Assets")
    
    # Adjust layout to fit everything
    plt.tight_layout()

    plt.show()

    # Explanation under the plot
    print("The scatter plot above shows the pickup times for each asset. Each point represents a ride, "
          "and the y-axis shows the pickup time in minutes. The x-axis indicates the asset to which the ride is assigned. "
          "This visualization helps to understand how evenly the rides are distributed across different assets over time.")

def plot_metrics(metrics):
    y_labels = {
        'mile_efficiency': 'Variance in Distance (miles²)',
        'time_efficiency': 'Standard Deviation in Pickup Time (minutes)',
        'average_closeness': 'Average Distance Between Rides (miles)',
        'asset_downtime': 'Average Downtime (hours)'
    }

    for metric_name, metric_data in metrics.items():
        assets = list(metric_data.keys())
        values = list(metric_data.values())

        plt.figure(figsize=(10, 6))
        plt.bar(assets, values, color='skyblue')
        plt.title(metric_name.replace('_', ' ').title())
        plt.xlabel('Asset')
        plt.ylabel(y_labels.get(metric_name, 'Value'))
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Explanation under the plot
        print(f"The bar chart above shows the {metric_name.replace('_', ' ').title()} for each asset. "
              "This helps visualize the efficiency of each asset in terms of the specific metric. "
              "Lower values indicate better performance for each metric.")




def print_metrics(metrics):

    # Example data for assets and their scores (as provided)
    asset_ids = ['v101', 'v102', 'v104', 'v105', 'v106', 'v107', 'v108', 'v109', 'v202', 'v301']

    mile_efficiency_scores = [v for v in metrics['mile_efficiency'].values()]
    time_efficiency_scores = [v for v in metrics['time_efficiency'].values()]
    avg_closeness_scores = [v for v in metrics["average_closeness"].values()]
    asset_downtime_scores = [v for v in metrics['asset_downtime'].values()]

    # Normalize the scores (using min-max normalization)
    def normalize_scores(scores):
        min_score = min(scores)
        max_score = max(scores)
        return [(score - min_score) / (max_score - min_score) for score in scores]

    mile_efficiency_normalized = normalize_scores(mile_efficiency_scores)
    time_efficiency_normalized = normalize_scores(time_efficiency_scores)
    avg_closeness_normalized = normalize_scores(avg_closeness_scores)
    asset_downtime_normalized = normalize_scores(asset_downtime_scores)

    # Combine normalized scores to calculate the bottom-line score
    bottom_line_normalized_scores = [(mile + time + avg + pickup) / 4
                                    for mile, time, avg, pickup in zip(mile_efficiency_normalized,
                                                                        time_efficiency_normalized,
                                                                        avg_closeness_normalized,
                                                                        asset_downtime_normalized)]

    # Variance calculation function
    def calculate_variance(scores):
        return np.var(scores)

    # Calculate variance for each metric
    mile_efficiency_variance = calculate_variance(mile_efficiency_normalized)
    time_efficiency_variance = calculate_variance(time_efficiency_normalized)
    avg_closeness_variance = calculate_variance(avg_closeness_normalized)
    asset_downtime_variance = calculate_variance(asset_downtime_normalized)
    bottom_line_variance = calculate_variance(bottom_line_normalized_scores)

    # Output the results
    print("Variance (measures variability of each metric):")
    print(f"Mile Efficiency Score Variance: {mile_efficiency_variance:.4f}")
    print(f"Time Efficiency Score Variance: {time_efficiency_variance:.4f}")
    print(f"Average Closeness Score Variance: {avg_closeness_variance:.4f}")
    print(f"Pickup Times Score Variance: {asset_downtime_variance:.4f}")
    print(f"Bottom-Line Score Variance: {bottom_line_variance:.4f}")

    # Scores for assets
    print("\nMile Efficiency Score:")
    for asset, score in zip(asset_ids, mile_efficiency_scores):
        print(f"Asset {asset}: {score:.2f}")

    print("\nTime Efficiency Score:")
    for asset, score in zip(asset_ids, time_efficiency_scores):
        print(f"Asset {asset}: {score:.2f}")

    print("\nAverage Closeness Score:")
    for asset, score in zip(asset_ids, avg_closeness_scores):
        print(f"Asset {asset}: {score:.2f}")

    print("\nPickup Times Score:")
    for asset, score in zip(asset_ids, asset_downtime_scores):
        print(f"Asset {asset}: {score:.2f}")

    print("\nNormalized Scores (0 = best, 1 = worst):")
    print("\nMile Efficiency Score:")
    for asset, score in zip(asset_ids, mile_efficiency_normalized):
        print(f"Asset {asset}: {score:.2f}")

    print("\nTime Efficiency Score:")
    for asset, score in zip(asset_ids, time_efficiency_normalized):
        print(f"Asset {asset}: {score:.2f}")

    print("\nAverage Closeness Score:")
    for asset, score in zip(asset_ids, avg_closeness_normalized):
        print(f"Asset {asset}: {score:.2f}")

    print("\nPickup Times Score:")
    for asset, score in zip(asset_ids, asset_downtime_normalized):
        print(f"Asset {asset}: {score:.2f}")

    print("\nBottom-Line Normalized Scores (average across all metrics):")
    for asset, score in zip(asset_ids, bottom_line_normalized_scores):
        print(f"Asset {asset}: {score:.2f}")

if __name__ == "__main__":
    # Load the finalized schedule from a CSV file (replace 'schedule.csv' with your file path)
    schedule = pd.read_csv(r'C:\Users\cyberwitch\Documents\portfolio\ALTR_PROJECT\Schedule-24-10-28 - schedule-24-10-28.csv')
    
    # Ensure the pickup_time column is a datetime object
    schedule['pickup_time'] = pd.to_datetime(schedule['pickup_time'])

    # Calculate metrics and scores
    metrics, scores = calculate_metrics(schedule)

    # Print the metrics
    print_metrics(metrics)
    
    # Normalize the scores
    normalized_scores = normalize_scores(scores)
    
    # Plot metrics like variance, time efficiency, and closeness
    plot_metrics(metrics)
    
    # Plot pickup times by asset
    plot_scatter_pickup_times(schedule)
    






