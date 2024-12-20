schedule = pd.read_csv(r'C:\Users\cyberwitch\Documents\portfolio\ALTR_PROJECT\Schedule-24-10-28 - schedule-24-10-28.csv')

# BOTTOM LINE SCORES
The **bottom line scores** represent an overall performance score for each asset, derived from the individual metrics calculated for the schedule. These scores aim to provide a consolidated view of each asset's performance across multiple aspects of efficiency. Specifically, the bottom line score is the **average** of the following four key metrics:

1. **Mile Efficiency Score**: Measures the variance in the distance traveled by each asset. Lower values are better, indicating that the asset's distance traveled per ride is more consistent.
   
2. **Time Efficiency Score**: Measures the standard deviation of pickup times per asset. Lower values suggest that the asset’s pickup times are more consistent and predictable.
   
3. **Average Closeness Score**: Reflects the average distance between consecutive rides for each asset. Lower values indicate that rides are grouped more closely together, which could lead to more efficient use of resources.

4. **Pickup Times Score**: Measures the average difference in pickup times between consecutive rides. A smaller value suggests more evenly spaced pickup times, which is ideal for optimizing scheduling.

### Purpose:
The bottom line score combines these four metrics into one value per asset, giving an overall performance score. This score can be used to compare the efficiency of different assets in handling rides and to evaluate how well each asset performs across the different aspects of the schedule.

### Calculation:
The bottom line score for each asset is calculated as the average of the four individual scores for that asset. Ideally, lower bottom line scores indicate better overall performance, as it suggests that the asset is both efficient in terms of distance, time, ride closeness, and pickup times.


In summary, the bottom line scores summarize the combined efficiency and performance of each asset, offering a way to assess and compare assets in a single, consolidated measure.

# Dividing by the number of rides
Dividing by `num_rides_per_asset` helps normalize metrics across assets, ensuring fair comparisons. It accounts for differences in ride volume, preventing assets with more rides from being unfairly penalized or rewarded. This normalization removes bias caused by varying numbers of rides, allowing you to accurately assess each asset’s efficiency and performance relative to its workload. Essentially, it ensures that assets are evaluated on the true quality of their performance, not just the quantity of rides they handle.

# Standard Deviation and Variance

Standard deviation is a measure of how spread out the values in a dataset are. It tells you how much individual data points deviate from the mean (average) value. A higher standard deviation indicates that the values are more spread out, while a lower standard deviation indicates that the values are closer to the mean.


To understand the standard deviation in your data:

### Step-by-step explanation using the data:

- **Mile Efficiency Values**:
  - Asset v101: 5.23
  - Asset v102: 7.97
  - Asset v104: 22.82
  - Asset v105: 61.35
  - Asset v106: 29.90
  - Asset v107: 5.20
  - Asset v108: 16.70
  - Asset v109: 56.83
  - Asset v202: 4.48
  - Asset v301: 19.83

- **Total variance**: 391.39 (Variance is the average of squared deviations from the mean.)

- **Standard deviation (19.78)** is the square root of the variance. It represents the typical distance between the values and the mean.

### Why the standard deviation is 19.78:
1. **Find the Mean (Average)** of the Mile Efficiency values:
   - Mean = (5.23 + 7.97 + 22.82 + 61.35 + 29.90 + 5.20 + 16.70 + 56.83 + 4.48 + 19.83) / 10 = 230.31 / 10 = 23.03

2. **Calculate the Squared Differences** from the mean for each asset:
   - (5.23 - 23.03)² = 318.73
   - (7.97 - 23.03)² = 228.49
   - (22.82 - 23.03)² = 0.04
   - (61.35 - 23.03)² = 1464.33
   - (29.90 - 23.03)² = 47.42
   - (5.20 - 23.03)² = 318.35
   - (16.70 - 23.03)² = 39.84
   - (56.83 - 23.03)² = 1153.69
   - (4.48 - 23.03)² = 340.16
   - (19.83 - 23.03)² = 10.30

3. **Find the Variance** by averaging these squared differences:
   - Variance = (318.73 + 228.49 + 0.04 + 1464.33 + 47.42 + 318.35 + 39.84 + 1153.69 + 340.16 + 10.30) / 10 = 391.39

4. **Find the Standard Deviation** by taking the square root of the variance:
   - Standard deviation = √391.39 ≈ 19.78

### In summary:
- The standard deviation of **19.78** means that the mile efficiency values generally deviate from the average of 23.03 by approximately 19.78 miles, on average.
- This helps to quantify how spread out the mile efficiency values are. A standard deviation of 19.78 shows that while some assets have relatively low mile efficiency (close to the mean), others have higher or more varied mile efficiencies.
--- Mile Efficiency ---
Asset v101: 5.23
Asset v102: 7.97
Asset v104: 22.82
Asset v105: 61.35
Asset v106: 29.90
Asset v107: 5.20
Asset v108: 16.70
Asset v109: 56.83
Asset v202: 4.48
Asset v301: 19.83
Total variance for Mile Efficiency: 391.39
Standard deviation for Mile Efficiency: 19.78 (miles generally deviate from the mean miles 23.03 by 19.78 miles)


# Aim of these metrics
- A well-optimized scheduling system would aim to reduce this variation and ensure that all assets are utilized as efficiently as possible.
- Ideally, the goal should be to reduce the standard deviation by better balancing the workload across the assets. This would result in more consistent mile efficiencies across assets, reflecting a better overall scheduling quality.
- The extreme difference between assets with low mile efficiency (e.g., Asset v101 with 5.23) and high mile efficiency (e.g., Asset v105 with 61.35) suggests that some assets might be consistently facing inefficient routes or schedules, leading to higher fuel costs or unnecessary wear on vehicles, while others are performing much better.
- A system with high mile efficiency variance could lead to higher operational costs due to inefficiency. Assets with higher mileages are likely using more fuel, while others may be underused, leading to potentially higher fixed costs per ride.
In addition, this inefficiency could impact sustainability efforts if environmental goals are tied to reducing mileage or optimizing vehicle use.