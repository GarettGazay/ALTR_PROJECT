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

def calculate_bottom_line_score(scores):
    bottom_line_scores = {}
    for asset in scores['mile_efficiency_score'].keys():
        # Average of all scores for each asset
        scores_for_asset = [
            scores['mile_efficiency_score'][asset],
            scores['time_efficiency_score'][asset],
            scores['average_closeness_score'][asset],
            scores['pickup_times_score'][asset]
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

def print_summary(metrics, scores, bottom_line_scores, variance_scalars):
    print("Summary of Key Metrics and Variance Scores:")
    
    # Print variance and standard deviation for each metric
    for metric_name, metric_data in metrics.items():
        print(f"\n--- {metric_name.replace('_', ' ').title()} ---")
        for asset, value in metric_data.items():
            print(f"Asset {asset}: {value:.2f}")
        
        metric_variance = variance_scalars.get(metric_name, 0)
        print(f"Total variance for {metric_name.replace('_', ' ').title()}: {metric_variance:.2f}")
        print(f"Standard deviation for {metric_name.replace('_', ' ').title()}: {np.sqrt(metric_variance):.2f}")

    # Print bottom line scores
    print("\n--- Bottom Line Scores ---")
    for asset, bottom_line_score in bottom_line_scores.items():
        print(f"Asset {asset}: {bottom_line_score:.2f}")

    print("\nVariance and Standard Deviation have been calculated for each metric and score, providing a breakdown of performance consistency across assets.")
    
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

if __name__ == "__main__":
    # Load the finalized schedule from a CSV file (replace 'schedule.csv' with your file path)
    # schedule = pd.read_csv(r'C:\Users\cyberwitch\Documents\portfolio\ALTR_PROJECT\Schedule-24-10-28 - schedule-24-10-28.csv')
    schedule = pd.read_csv(r'C:\Users\cyberwitch\Documents\portfolio\ALTR_PROJECT\agent_schedule_2024_10_31_converted.csv')
    
    # Ensure the pickup_time column is a datetime object
    schedule['pickup_time'] = pd.to_datetime(schedule['pickup_time'])

    # Calculate metrics and scores
    metrics, scores = calculate_metrics(schedule)
    
    # Calculate bottom line scores
    bottom_line_scores = calculate_bottom_line_score(scores)
    
    # Calculate variance scalars
    variance_scalars = calculate_variance_scalars(metrics, scores)
    
    # Print summary
    print_summary(metrics, scores, bottom_line_scores, variance_scalars)
    
    # Plot metrics like variance, time efficiency, and closeness
    plot_metrics(metrics)
    
    # Plot pickup times by asset
    plot_scatter_pickup_times(schedule)
