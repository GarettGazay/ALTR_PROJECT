# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation, PillowWriter
# import numpy as np

# # Number of assets and rides
# num_assets = 10
# num_rides = 90

# # Generate vertical positions for rides and assets
# ride_positions = np.linspace(10, 0, num_rides)  # Rides aligned vertically from top to bottom
# asset_positions = np.linspace(10, 0, num_assets)  # Assets aligned vertically from top to bottom

# # Assign each ride to a random asset
# np.random.seed(42)  # For reproducibility
# assignments = np.random.choice(num_assets, num_rides)

# # Coordinates for rides (left side) and assets (right side)
# ride_coords = np.column_stack((np.zeros(num_rides), ride_positions))
# asset_coords = np.column_stack((np.ones(num_assets) * 10, asset_positions))

# # Create the figure
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.set_xlim(-2, 12)
# ax.set_ylim(-1, 11)
# ax.set_title("Ride Assignments to Assets")
# ax.axis('off')  # Hide axes for cleaner visualization

# # Plot rides and assets as dots
# rides = ax.scatter(ride_coords[:, 0], ride_coords[:, 1], color='blue', s=5, label="Rides")  # Smaller blue dots
# assets = ax.scatter(asset_coords[:, 0], asset_coords[:, 1], color='red', s=50, label="Assets")  # Larger red dots

# # Add legend
# ax.legend(loc='upper center')

# # Initialize a list for line artists
# lines = []

# # Animation function
# def animate(i):
#     ride_index = i  # Current ride index
#     asset_index = assignments[ride_index]  # Assigned asset index
#     ride_pos = ride_coords[ride_index]
#     asset_pos = asset_coords[asset_index]
#     line, = ax.plot([ride_pos[0], asset_pos[0]], [ride_pos[1], asset_pos[1]], color='green', alpha=0.7)
#     lines.append(line)  # Store the line for cleanup if needed

# # Create the animation
# ani = FuncAnimation(fig, animate, frames=num_rides, interval=100, repeat=False)

# # Save the animation as a GIF
# ani.save("ride_assignments.gif", writer=PillowWriter(fps=10))

# # Display the animation
# plt.show()
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

# Number of assets and rides
num_assets = 10
num_rides = 90

# Generate vertical positions for rides and assets
ride_positions = np.linspace(10, 0, num_rides)  # Rides aligned vertically from top to bottom
asset_positions = np.linspace(10, 0, num_assets)  # Assets aligned vertically from top to bottom

# Assign each ride to a random asset
np.random.seed(42)  # For reproducibility
assignments = np.random.choice(num_assets, num_rides)

# Coordinates for rides (left side) and assets (right side)
ride_coords = np.column_stack((np.zeros(num_rides), ride_positions))
asset_coords = np.column_stack((np.ones(num_assets) * 10, asset_positions))

# Rewards initialization
mile_rewards = np.zeros(num_rides)
on_time_rewards = np.zeros(num_rides)
load_balance_rewards = np.zeros(num_rides)

# Function to calculate the mileage reward (minimizing distance between ride and asset)
def calculate_mile_reward(ride_index, asset_index):
    ride_pos = ride_coords[ride_index]
    asset_pos = asset_coords[asset_index]
    distance = np.abs(ride_pos[1] - asset_pos[1])  # Simple vertical distance
    return max(0, 1 - distance / num_rides) * (1 + np.random.normal(0, 0.1))  # Adding noise for variance

# Function to calculate on-time reward (ride closer to asset = on time)
def calculate_on_time_reward(ride_index, asset_index):
    ride_pos = ride_coords[ride_index]
    asset_pos = asset_coords[asset_index]
    time_diff = np.abs(ride_pos[1] - asset_pos[1])
    return max(0, 1 - time_diff / (num_rides / 2)) * (1 + np.random.normal(0, 0.1))  # Adding noise for variance

# Function to calculate load balance reward (distribute rides evenly)
def calculate_load_balance_reward():
    ride_counts = np.bincount(assignments, minlength=num_assets)  # Count rides per asset
    avg_load = num_rides / num_assets
    balance = np.sum(np.abs(ride_counts - avg_load)) / num_rides  # Measure imbalance
    return max(0, 1 - balance) * (1 + np.random.normal(0, 0.1))  # Adding noise for variance

# Create the figure
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-2, 12)
ax.set_ylim(-1, 11)
ax.set_title("Ride Assignments to Assets")
ax.axis('off')  # Hide axes for cleaner visualization

# Plot rides and assets as dots
rides = ax.scatter(ride_coords[:, 0], ride_coords[:, 1], color='blue', s=5, label="Rides")  # Smaller blue dots
assets = ax.scatter(asset_coords[:, 0], asset_coords[:, 1], color='red', s=50, label="Assets")  # Larger red dots

# Add legend
ax.legend(loc='upper center')

# Initialize a list for line artists
lines = []

# Initialize text objects for displaying cumulative rewards
mile_text = ax.text(-2, 9.5, 'Mileage Reward: 0.00', fontsize=8, color='black', ha='center')
on_time_text = ax.text(-2, 9.0, 'On-time Reward: 0.00', fontsize=8, color='black', ha='center')
load_balance_text = ax.text(-2, 8.5, 'Load Balance Reward: 0.00', fontsize=8, color='black', ha='center')

# Animation function
def animate(i):
    ride_index = i  # Current ride index
    asset_index = assignments[ride_index]  # Assigned asset index
    ride_pos = ride_coords[ride_index]
    asset_pos = asset_coords[asset_index]
    
    # Update rewards
    mile_rewards[ride_index] = calculate_mile_reward(ride_index, asset_index)
    on_time_rewards[ride_index] = calculate_on_time_reward(ride_index, asset_index)
    
    # Cumulative rewards
    cumulative_mile_reward = np.mean(mile_rewards[:i+1])
    cumulative_on_time_reward = np.mean(on_time_rewards[:i+1])
    cumulative_load_balance_reward = calculate_load_balance_reward()
    
    # Plot the line for the current assignment
    line, = ax.plot([ride_pos[0], asset_pos[0]], [ride_pos[1], asset_pos[1]], color='green', alpha=0.7)
    lines.append(line)  # Store the line for cleanup if needed
    
    # Update reward text
    mile_text.set_text(f'Mileage Reward: {cumulative_mile_reward:.2f}')
    on_time_text.set_text(f'On-time Reward: {cumulative_on_time_reward:.2f}')
    load_balance_text.set_text(f'Load Balance Reward: {cumulative_load_balance_reward:.2f}')

# Create the animation
ani = FuncAnimation(fig, animate, frames=num_rides, interval=100, repeat=False)

# Save the animation as a GIF
ani.save("ride_assignments_with_rewards.gif", writer=PillowWriter(fps=10))

# Display the animation
plt.show()
