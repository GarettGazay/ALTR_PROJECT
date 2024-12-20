
# Transportation Scheduling App with Reinforcement Learning

## Overview
This project implements a transportation scheduling system using reinforcement learning (RL) to optimize the distribution of rides across available assets. The goal is to efficiently allocate rides while minimizing mileage, maximizing time efficiency, and balancing the ride distribution across assets.

## Key Features
- **Single-Agent RL System**: A single agent schedules all rides for an asset (Non-Emergency Ambulance).
- **RL-based Scheduling**: The agent learns to allocate rides based on available resources (time, distance, ride duration) while optimizing for efficiency.
- **Mileage Minimization**: The app aims to minimize total mileage covered by the asset, improving fuel efficiency and reducing operational costs.
- **Time Efficiency**: The system ensures that rides are completed within their designated time windows to improve service quality.
- **Ride Distribution**: The app optimizes ride allocation to avoid underusing assets, ensuring efficient use of resources.
- **Multi-Loading**: The app looks for multi-loading opporunities and will load assets with multiple riders for a single trip under the correct conditions.

## Key Metrics
The following metrics demonstrate the efficiency and effectiveness of the scheduling system:

1. **Mileage Minimization**: Measures how well the agent minimizes total mileage traveled by the asset.
   - Metric: Total mileage per episode, average mileage per ride, optimal distance ratio.

2. **Time Efficiency**: Tracks how well the system schedules rides within the assigned time windows.
   - Metric: Average ride completion time, percentage of rides completed on time, and time-to-completion ratio.

3. **Ride Distribution Across Assets**: Ensures that rides are balanced across all assets to avoid underloading any single asset.
   - Metric: Distribution balance score (variance in ride assignments), ride assignments per asset, percentage of assets utilized.
   - The load balance reward establishes a baseline logic, supporting the other reward priorities to maximize efficiency, and balance all rewards evenly toward solving the transportation scheduling problem for NEMT.

4. **Reward Convergence** (Optional): Measures how quickly the RL agent converges to an optimal policy during training.
   - Metric: Number of episodes for reward stabilization, improvement in reward over time.

## Setup Instructions
To run the transportation scheduling app, follow these steps:

### Prerequisites
- Python 3.7+
- Required libraries:
  - `gym`
  - `numpy`
  - `stable-baselines3` (or your chosen RL library)
  - `pymunk` (if physics-based simulations are required)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/transportation-scheduling.git
   cd transportation-scheduling


### How It Works
In this single-agent system, the RL agent is responsible for scheduling all rides within the given time slots (shift duration of assets). The agent interacts with the environment, receiving observations such as available the current load of all assets, the next state of all assets given a selection, time localization, and several additional metrics, then makes decisions to allocate rides in a way that minimizes mileage, completes rides on time, and balances the distribution of rides across available assets.

### Training
The training process uses a flavor of the Reinforcement Learning algorithm Proximal Policy Optimization (PPO) that retains long term memory of best practices from day to day. The agent is rewarded for completing rides on time, minimizing mileage, and distributing rides efficiently across the assets. The agent learns from its interactions with the environment and gradually improves its scheduling policy.

### Performance
During training, several key metrics are tracked to evaluate the system's performance. Below is an example of the system's performance over 100 episodes:

| Metric                        | Value                      |
|-------------------------------|----------------------------|
| Reward Min/Max                | 0 - 1
| Average Reward                | 0.85                       |
| Mileage Minimization          | 95% optimal distance       |
| On-time Performance           | 92% on-time completion     |
| Ride Distribution Balance     | 0.7 (lower is better)      |
| Reward Convergence Epochs     | 100                        |




## Usage

1. **Training the Model:**
   Run the training script to train RL agents:
   ```bash
   python src/main.py --train
   ```

2. **Evaluating Performance:**
   Test the trained model on new data:
   ```bash
   python src/main.py --evaluate
   ```

3. **Visualizing Metrics:**
   Generate visualizations for metrics:
   ```bash
   python src/visualization/metrics_plotter.py
   ```

4. **Interactive Dashboard (Optional):**
   Launch a dashboard to explore metrics in real-time:
   ```bash
   streamlit run src/visualization/dashboard.py
   ```

---

## Metrics Tracked

### **1. Scheduling Metrics**
- **Ride Completion Rate:** Percentage of assigned rides successfully scheduled without conflicts.
- **On-Time Performance:** Proportion of rides completed within the scheduled time window.
- **Ride Balancing:** Variance or standard deviation of rides distributed across assets.

### **2. Efficiency Metrics**
- **Miles Per Ride:** Average distance traveled per ride.
- **Idle Time Minimization:** Percentage of time assets spend idle during their shifts.
- **Average Utilization Rate:** Time spent on rides versus total available shift time for assets.

### **3. Cost Metrics**
- **Fuel Cost Reduction:** Savings from optimized routing.
- **Driver Hours Reduction:** Hours saved through efficient scheduling.
- **Skipped Ride Penalty Reduction:** Decrease in penalties incurred from skipped rides.

### **4. Scalability Metrics**
- **Number of Rides Scheduled Per Episode:** Handles increasing ride volume efficiently.
- **Time to Converge:** Speed at which RL agents learn optimal policies.
- **Inference Time:** Time taken to generate schedules in real-time.

### **5. Robustness Metrics**
- **Performance in Edge Cases:** Scheduling with limited assets or peak times.
- **Success Rate After Skipping Rides:** Effectiveness in handling skipped rides.
- **Reward Trends:** Cumulative reward growth over training episodes.

---

## Visualizations

### **Key Graphs and Charts**
1. **Ride Balancing:** Bar chart showing rides per asset.
2. **Reward Trends:** Line graph of cumulative rewards over episodes.
3. **On-Time Performance:** Pie chart or bar graph of completed vs. late rides.
4. **Miles Per Ride:** Histogram or scatter plot of ride distances.
5. **Heatmap:** Correlation between metrics like utilization and rewards.

### **Sample Code for Plotting**

```python
import matplotlib.pyplot as plt

def plot_rewards(rewards):
    plt.figure(figsize=(10, 5))
    plt.plot(rewards, label="Cumulative Rewards")
    plt.xlabel("Episodes")
    plt.ylabel("Rewards")
    plt.title("Reward Growth Over Time")
    plt.legend()
    plt.grid()
    plt.savefig("data/rewards_plot.png")
    plt.show()

# Example usage
reward_data = [100, 150, 200, 250, 300]
plot_rewards(reward_data)
```

---

## Interactive Dashboard

An optional interactive dashboard is available to explore metrics dynamically.

### **Setup**
Install Streamlit:
```bash
pip install streamlit
```

### **Dashboard Code**
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
ride_data = pd.read_csv("data/runtime_log.csv")
reward_data = pd.read_csv("data/rewards_log.csv")

# Sidebar options
st.sidebar.title("Metrics Explorer")
metric = st.sidebar.selectbox("Select a metric to visualize", ["Rewards", "Utilization"])

if metric == "Rewards":
    st.title("Reward Growth Over Time")
    st.line_chart(reward_data['reward'])

elif metric == "Utilization":
    st.title("Asset Utilization")
    st.bar_chart(ride_data.groupby('asset')['utilization'].mean())
```

Run the dashboard:
```bash
streamlit run src/visualization/dashboard.py
```

---

## Automating Metrics Logging

### **Log Rewards to CSV**

```python
import csv

def log_rewards(reward, episode, filename="data/rewards_log.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([episode, reward])

# Example usage
log_rewards(250, 1)
log_rewards(300, 2)
```

---

## Jupyter Notebooks

### **`training_visualization.ipynb`**
- Analyze training progress: reward trends, ride balancing metrics.

### **`exploratory_analysis.ipynb`**
- Explore parameter effects on ride distribution and asset availability.

---

## Future Work
- Integration with real-world datasets for live scheduling.
- Enhanced scalability to handle thousands of rides.
- Improved multi-agent collaboration for global optimization.

---

## Technologies Used
- **Reinforcement Learning:** Stable-Baselines3
- **Visualization:** Matplotlib, Seaborn, Streamlit
- **Data Processing:** Pandas, NumPy
