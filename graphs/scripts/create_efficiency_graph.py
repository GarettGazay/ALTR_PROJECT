import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Updated data with 11 assets
data = {
    "Asset": ["SC101_A", "SC103_A", "SC104", "SC105", "SC106", "SC107", "SC108", "SC109", "SC201", "SC202", "SC203"],
    "Ride": ["Ride 1", "Ride 2", "Ride 3", "Ride 4", "Ride 5", "Ride 6", "Ride 7", "Ride 8", "Ride 9", "Ride 10", "Ride 11"],
    "Miles_Per_Ride": [16.84,
                       10.09457142857143,
                       5.067454545454546,
                       8.687,
                       8.347333333333333,
                       11.818555555555557,
                       7.62042857142857,
                       7.987272727272727,
                       7.451818181818182,
                       14.638200000000001,
                       7.2194],
    "Idle_Time_Percent": [4.910714285714286,
                          4.077380952380952,
                          3.3712121212121207,
                          4.053030303030304,
                          4.097222222222222,
                          4.097222222222222,
                          4.2559523809523805,
                          4.090909090909092,
                          3.7878787878787885,
                          5.333333333333334,
                          3.6666666666666665],  # Idle time percentages
    "Utilized_Time": [4.910714285714286,
4.0773809523809526,
3.3712121212121207,
4.053030303030302,
4.097222222222222,
4.097222222222221,
4.255952380952381,
4.090909090909092,
3.787878787878787,
5.333333333333334,
3.6666666666666665],  # Time spent on rides (in hours)
 
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Calculate Average Utilization Rate as Utilized Time / Total Shift Time * 100
df["Utilization_Rate"] = (100 - df["Utilized_Time"])

# Set Seaborn style for the plots
sns.set(style="whitegrid")

# Create a figure with three subplots: one for Miles Per Ride, one for Idle Time Percentage, and one for Utilization Rate
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Adjust the width of the bars by specifying the width parameter
bar_width = 0.8  # Adjust the width as needed

# Plotting Miles Per Ride per Asset
sns.barplot(x="Asset", y="Miles_Per_Ride", data=df, estimator="mean", errorbar=None, palette="viridis", ax=axes[0], width=bar_width)
axes[0].set_title("Miles Per Ride: Average Distance per Asset", fontsize=16)
axes[0].set_xlabel("Asset (Vehicle)", fontsize=14)
axes[0].set_ylabel("Average Miles Per Ride", fontsize=14)

# Plotting Idle Time Percentage per Asset
sns.barplot(x="Asset", y="Idle_Time_Percent", data=df, estimator="mean", errorbar=None, palette="coolwarm", ax=axes[1], width=bar_width)
axes[1].set_title("Idle Time Per Asset: Percentage of Idle Time", fontsize=16)
axes[1].set_xlabel("Asset (Vehicle)", fontsize=14)
axes[1].set_ylabel("Idle Time Percentage (%)", fontsize=14)

# Plotting Average Utilization Rate per Asset
sns.barplot(x="Asset", y="Utilization_Rate", data=df, estimator="mean", errorbar=None, palette="plasma", ax=axes[2], width=bar_width)

# Adjust the y-axis to be between 0 and 100
axes[2].set_ylim(0, 100)

# Add title and labels for clarity
axes[2].set_title("Average Utilization Rate per Asset", fontsize=16)
axes[2].set_xlabel("Asset (Vehicle)", fontsize=14)
axes[2].set_ylabel("Utilization Rate (%)", fontsize=14)

# Adjust the x-axis label positions to spread the bars apart
for ax in axes:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.set_xticks(range(len(df["Asset"])))

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()
