# ALTR (Advantage Leveraging Timetable Reinforcement)
### Ambulance Transport Scheduling Solution for NEMT

A scheduling optimization app I developed for ambulance operations, using deep learning and reinforcement learning to improve efficiency. ALTR, now used by an NEMT company based in Mountain View, CA, automates 90% of ride scheduling, significantly reducing payroll costs, and optimizing the company's daily operations.

---

## **Overview**

This app leverages **Python**, **OpenAI Gym**, **Pytorch** and **Stable-Baselines3 (SB3)** to optimize the scheduling of ambulances for timely pickup and delivery of patients for various types of appointments. It includes a simplified demonstration with sample data and outputs.

---

## **Features**

- **AI-Driven Optimization**: Uses reinforcement learning to enhance operational scheduling efficiency.
- **Simulation Environment**: Built with OpenAI Gym for creating and testing scheduling scenarios.
- **Scalable Design**: Capable of adapting to different operational constraints and objectives.
- **Interactive Visualizations**: Outputs sample schedules to demonstrate results.

---

## **Tech Stack**

- **Language**: Python
- **Libraries**: 
  - OpenAI Gym
  - Pytorch
  - Stable-Baselines3
  - NumPy, Pandas, Matplotlib, Tensorboard
- **Development Tools**:
  - Jupyter Notebook (optional for analysis)
  - Docker (optional for containerization)

---


## **How It Works**

## **How It Works**

### **Features Include**:
- Mileage optimization
- On-time performance optimization
- Asset utilization
- Automated scheduling
- Adaptable scheduling (intelligently fits specified trips into a driver’s schedule)
- Lunch breaks can be set for each schedule

---

### **1. Problem Breakdown**:
Ambulance and Non-Emergency Medical Transportation (NEMT) service providers often face the challenge of scheduling critical appointments, such as clinical visits, dialysis sessions, and hospital discharges. This task is traditionally handled by human dispatchers who manually create optimized schedules. However, the process is time-consuming, often taking hours even for small operations.

**Human schedule generation inefficiency:**
- Time Consumption: Human schedulers spend significant time organizing and adjusting the schedule, which can take hours, especially when last-minute changes occur.
- Inaccuracy: Human errors lead to scheduling conflicts, overworked drivers, and inefficient use of available time slots.
- Limited Flexibility: It is difficult for human schedulers to foresee all possible trip combinations and constraints, leading to missed opportunities for optimization.
- Stressful Workload: Dispatchers often juggle multiple priorities at once, creating stress and a high likelihood of mistakes or inefficiency.
- Long-term impacts on efficiency, in terms of both mileage and time, are often difficult to factor into immediate scheduling decisions.




The ALTR Scheduling System is designed to address this inefficiency by automating the scheduling process through reinforcement learning (RL). Instead of relying on human dispatchers for routine scheduling tasks, ALTR uses intelligent algorithms to automatically generate schedules. This not only saves valuable time but also allows for more optimized and innovative solutions that would be difficult or time-intensive for humans to manually discover. By automating the scheduling process, ALTR empowers human schedulers to focus on more strategic decisions, ultimately improving overall operational efficiency.

---

### **2. Reinforcement Learning**:
ALTR uses reinforcement learning (RL) to optimize ambulance scheduling, with the goal of maximizing efficiency across key metrics such as mileage, on-time performance, and asset utilization.

- **RL Agent**: The RL agent learns from past scheduling data and receives rewards based on predefined objectives (e.g., minimizing mileage, improving on-time performance). This enables the system to make better decisions over time.
- **SB3**: ALTR utilizes the Stable Baselines3 (SB3) library for implementing RL algorithms. This allows us to fine-tune and optimize the agent's policies in response to dynamic scheduling conditions.

#### **How Reinforcement Learning Works in ALTR**:
1. **State Representation**: The agent receives a state that includes available rides, asset statuses, and time windows.
2. **Action Space**: The agent selects actions from a discrete action space, such as assigning a ride to a driver, optimizing the route, or adjusting the schedule.
3. **Reward Function**: The agent is rewarded based on metrics like mileage reduction, on-time performance, and overall asset utilization.
4. **Policy Improvement**: Through repeated interactions with the environment, the agent refines its policy, ultimately optimizing scheduling decisions.

![RL Process](path_to_image/reinforcement_learning_process.png) <!-- Add a diagram illustrating how the reinforcement learning process works -->

---

## **3. Outputs**
ALTR organizes unscheduled rides into the most efficient schedules possible, based on predefined environment parameters. By prioritizing factors like mileage optimization, on-time performance, and asset utilization, the system generates clear, actionable outputs:

- **Optimized Schedules**: ALTR arranges rides into efficient schedules that maximize resource use and minimize conflicts. 
- **Performance Insights**: The system provides visual representations of key metrics such as mileage reduction, on-time rates, and overall asset efficiency, offering transparency into the decision-making process.

![Optimization Visualization](path_to_image/schedule_visualization.png) <!-- Optional placeholder for an image -->

---

## **4. In Action**
Here’s a practical example of ALTR transforming the scheduling process for an NEMT service. The system automatically matches rides to drivers, considering time constraints, and mileage.<br><br>
The system also performs ride batching (multi-loading a single vehicle). (Pictured below)

### **Before ALTR Implementation**
Manual scheduling often results in a "good-enough" state. If we look at:
 - the number of "dead" miles (miles traveled without a passenger)
 - on-time performance
 - spot utilization (how many spots a vehicle has for riders) 
 
 we can see the Human did just "good enough" in this case. This case is of course representative of the typical NEMT schedule generated by dispatchers at a real NEMT company using ALTR.

![human_schedule](path_to_image/schedule_visualization.png) <!-- Optional placeholder for an image -->
<!-- Placeholder for an image or textual example of manual scheduling -->

### **After ALTR Implementation**
ALTR automates the entire process, optimizing schedules in seconds, reducing wasted time and mileage, and improving on-time performance.

![altr_optimized_schedule](path_to_image/schedule_visualization.png) <!-- Optional placeholder for an image -->
<!-- Placeholder for an image or example of optimized schedules -->

---

By automating and optimizing scheduling, ALTR ensures that service providers can focus on strategic improvements rather than routine logistics, delivering measurable efficiency gains without the need for time-consuming manual intervention.

---

### **Next Steps if You Need Data**
If you'd like to showcase efficiency gains more concretely, you could:
1. Simulate manual schedules using randomized trip data to illustrate inefficiencies.
2. Generate comparative charts showing improvements in key metrics like time saved, mileage reduced, and on-time performance with ALTR.



## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ambulance-scheduling-demo.git
   cd ambulance-scheduling-demo
