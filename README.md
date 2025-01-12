# Advantage Leveraging Transit Reinforcement 


### Feel free to ask questions! 
<img src="./images/raised_hand.png" style="width:5%; margin-left:80px;">

## Overview

ALTR is a transportation scheduling system using Reinforcement Learning (RL) to optimize ride distribution across available assets. The goal is to efficiently allocate rides while minimizing mileage, maximizing time efficiency, and balancing distribution across assets.


## But First... What is Reinforcement Learning?

Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment. The agent takes actions, observes the results, and receives feedback in the form of rewards or penalties. Over time, the agent improves its behavior to maximize cumulative rewards.

### Example: A Robot in a Maze

Imagine a robot navigating a maze to find a charging station before its battery runs out. The robot (agent) explores the maze (environment) and decides which direction to move (action). If it gets closer to the charging station, it receives a reward; if it moves farther away or wastes battery, it gets no reward (or a penalty). Through trial and error, the robot learns the optimal paths to reach the charging station efficiently, avoiding dead ends and unnecessary detours.

This process mirrors RL, where the agent learns strategies to achieve its goal by maximizing rewards.

<img src="./images/robot_maze.jpg" style="width:60%;">

## Single-Agent RL Scheduling System 
(As opposed to a Multi-Agent system) <br>

This system is designed for Non-Emergency Ambulance services. The agent learns to allocate rides efficiently by considering factors like time, distance, and load balancing. It generates an optimized plan for the entire day, taking into account all assets and rides. With finely tuned learning parameters, the agent continuously improves, adapting to daily, weekly, and monthly trends.

### Side note on learning parameters: 
- Simply put, the agent learns more when it is improving and less when it is not. This approach encourages positive exploration while preventing the agent from reinforcing bad behaviors or getting stuck in sub-optimal outcomes.

## Feature Definitions

- **Mileage Minimization**: The agent aims to reduce total mileage, improving fuel efficiency and lowering operational costs.

- **Time Efficiency**:  The agent leverages temporal localization to create an efficient time plan across the entire day of rides.

- **Ride Distribution (Load Balancing)**: Optimizes allocation to prevent underutilization of assets.

- **Multi-Loading**: Identifies opportunities to load multiple riders onto a single trip under suitable conditions.

## Upcoming Features

- **Assigned Breaks**: Allows the user to assign designated breaks for drivers, while optimizing the schedule around them. (Lunch breaks, etc)

- **Pre-loading**: Assigns fixed rides, such as school pickups, and optimizes schedules around them. (Example is a public school contract where the TP wants a certain set of assets to be assigned to those rides.)

- **Live Dispatch**: Dynamically adjusts schedules to accommodate new ride requests or cancellations. For example, a TP has a pool of unassigned rides. Whenever there is a change in the environment (e.g., a cancellation or a shift in the load state of assets), the agent identifies new load opportunities that maximize rewards. TPs will also be able to use this feature to assess whether accepting a ride is feasible or not.

- **Ghost Assets**: Simulates additional assets to show how unassigned rides could be managed. A Ghost Asset’s schedule can be outsourced to a subcontractor or used to advise the TP about the need to aquire or utilize additional vehicles.


## Installation
Coming soon <span style="font-size: 2em;">👨‍🔬</span>
<!-- 
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/transportation-scheduling.git
   cd transportation-scheduling
   ``` -->

<!-- ## Overview
The following data is sourced from a real-life ambulance company that uses ALTR in its daily operations. While the rider names are fictional, the data reflects real-world scenarios. The agent handles several situational variables to the best of its ability. For example, time gaps often occur due to a shortage of rides in certain areas, particularly between 6 AM and 9 AM. These gaps result from low demand during those hours for this company and timeframe. In real scheduling scenarios, human dispatchers typically fill these gaps with same-day or day-prior requests. The system is designed to eliminate the tedium of manual scheduling, allowing dispatchers to focus on more creative tasks, rather than spending hours on repetitive scheduling work. The agent currently integrates standard trips, multi-loaded trips, and pre-scheduled trips. Special rides, such as gurney transports, are being developed but are not yet implemented.

The agent is given certain allowances to break the rules, so in the scheduled data we may see sitations where a an appointment time, and a pickup time for the next ride are very close together, this is due to the local proximity, and buffer time allowances. -->

## How It Works

- The agent receives a list of unordered rides.
- It evaluates each ride based on constraints such as asset shift windows, mileage and time rules.
- Using this evaluation, the agent builds a comprehensive schedule for the entire day, aiming to assign rides to assets in a way that maximizes efficiency and minimizes wasted resources.
- The agent strategically assigns rides to assets, balancing workload distribution, and optimizing for both individual asset performance and overall system efficiency.

In this single-agent system, the RL agent is responsible for scheduling all rides within the given time slots (shift duration of assets). The agent interacts with the environment, receiving several observations, then makes decisions to allocate rides in a way that minimizes mileage, completes rides on time, and balances the distribution of rides across available assets. 


### Two Types of Ride Scheduling Methods

The process of scheduling rides using reinforcement learning can be approached through two distinct methods, each with its own strengths and limitations:

---
# Current Capabilities and Future Vision

### **1. Non-Positional One-to-One Scheduling (Current Method)**  
This is the current implementation where the agent processes rides in a **one-to-one mapping**. The system works as follows:
- **Workflow**: The agent loops through all available rides sequentially. Over the course of training, it learns an optimal scheduling policy for the entire day.  

- **Strengths**:  
  - Simplicity: The method is straightforward, as the agent focuses on scheduling each ride individually with a long-term plan.
  - Effective for Specific Categories: It performs well for wheelchair rides.

- **Limitations**:  
  - Narrow Scope: The system lacks the ability to dynamically account for the real-time state of all assets, limiting its adaptability.  

  - Category-Specific: Currently, it is tailored to wheelchair rides and does not generalize to other ride types like **gurney** or **ambulatory** transports.

---

### **2. Dynamic Timing and Resource Optimization (Future Method)**  
DTRO is an advanced approach that incorporates a **state-aware scheduling strategy** that dynamically considers the load state of all assets throughout the scheduling process:
- **Workflow**: The agent tracks the real-time load state of every asset (e.g., vehicles, available capacity) at each step of the scheduling process. It uses this information to adapt and make optimal decisions for allocating rides.  
- **Feedback-Driven Optimization**: As the agent trains, it receives detailed feedback about successful and unsuccessful scheduling actions. This feedback enables it to refine its policy and create rules for optimizing **all ride categories** (e.g., wheelchair, gurney, and ambulatory).  
- **Strengths**:  
  - **Comprehensive Scheduling**: By considering the state of all assets, the system can make rules for diverse ride types, ensuring efficient utilization of resources.  
  - **Dynamic Adaptability**: The agent can react to changes in asset availability or ride requirements in real-time.  
  - **Unified System**: Unlike the one-to-one method, this approach allows a single agent to manage multiple categories, eliminating the need for separate agents.  
- **Challenges**:  
  - Increased Complexity: The system requires more computational resources and training time to handle the expanded state space and decision-making process.  
  - Developmental Stage: This method is still under active development and has not yet been fully implemented.  

---

### **Looking Ahead**  
While the non-positional one-to-one method provides a solid foundation for wheelchair ride scheduling, its limitations highlight the need for a more advanced approach. The dynamic asset state positional load method represents the future of ride scheduling by enabling the agent to holistically manage diverse categories of transport in a unified system. This evolution will pave the way for more efficient, adaptable, and comprehensive ride scheduling solutions.




### Unordered Rides
<details>
<summary>Click here to see unordered rides list</summary>
<div style="max-height: 200px; overflow-y: auto; border: 1px solid #ccc; padding: 10px;">
   <table border="1" style="width: 100%; border-collapse: collapse;">
      <thead>
         <tr>
            <th>RIDER</th>
            <th>PICKUP</th>
            <th>APPT_TIME</th>
            <th>ASSET</th>
            <th>PICKUP ADDRESS</th>
            <th>DROPOFF ADDRESS</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>NANCY BISHOP</td>
            <td>09:35:00</td>
            <td>10:00:00</td>
            <td>None</td>
            <td>1102 W FREMONT AVE SUNNYVALE CA 94087</td>
            <td>420 BROADWAY ST REDWOOD CITY CA 94063</td>
         </tr>
         <tr>
            <td>TONY VU</td>
            <td>10:12:00</td>
            <td>10:30:00</td>
            <td>None</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
            <td>696 E SANTA CLARA ST SAN JOSE CA 95112</td>
         </tr>
         <tr>
            <td>KABIR SANDHU</td>
            <td>13:45:00</td>
            <td>14:04:00</td>
            <td>None</td>
            <td>14651 S BASCOM AVE LOS GATOS CA 95032</td>
            <td>1147 LEIGH AVE SAN JOSE CA 95126</td>
         </tr>
         <tr>
            <td>KRISHNA PATEL</td>
            <td>18:15:00</td>
            <td>18:34:00</td>
            <td>None</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
            <td>1695 MENDENHALL DR SAN JOSE CA 95130</td>
         </tr>
         <tr>
            <td>ARMANDO VARGAS</td>
            <td>10:35:00</td>
            <td>10:58:00</td>
            <td>None</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
            <td>2160 INTERBAY DR SAN JOSE CA 95122</td>
         </tr>
         <tr>
            <td>ALEX PARKER</td>
            <td>14:00:00</td>
            <td>14:30:00</td>
            <td>None</td>
            <td>751 S BASCOM AVE SAN JOSE CA 95128</td>
            <td>6780 MEADOW VISTA CT SAN JOSE CA 95135</td>
         </tr>
         <tr>
            <td>LUCIAS SOLIS</td>
            <td>09:02:00</td>
            <td>09:15:00</td>
            <td>None</td>
            <td>260 N BAYVIEW AVE SUNNYVALE CA 94086</td>
            <td>610 N PASTORIA AVE SUNNYVALE CA 94085</td>
         </tr>
         <tr>
            <td>ANJALI VERMA</td>
            <td>18:15:00</td>
            <td>18:28:00</td>
            <td>None</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
            <td>2063 FOREST AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>ALEX PARKER</td>
            <td>12:31:00</td>
            <td>13:00:00</td>
            <td>None</td>
            <td>6780 MEADOW VISTA CT SAN JOSE CA 95135</td>
            <td>751 S BASCOM AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>VICTOR NGO</td>
            <td>14:41:00</td>
            <td>15:00:00</td>
            <td>None</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
            <td>266 N JACKSON AVE SAN JOSE CA 95116</td>
         </tr>
         <tr>
            <td>FELIX GOMEZ</td>
            <td>12:25:00</td>
            <td>12:36:00</td>
            <td>None</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
            <td>1919 FRUITDALE AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>MICHAEL LAM</td>
            <td>12:00:00</td>
            <td>12:18:00</td>
            <td>None</td>
            <td>200 JOSE FIGUERES AVE SAN JOSE CA 95116</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>OLIVER LEE</td>
            <td>14:46:00</td>
            <td>15:00:00</td>
            <td>None</td>
            <td>1300 W SAN CARLOS ST SAN JOSE CA 95126</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>CENTRAL AVENUE 1</td>
            <td>08:30:00</td>
            <td>09:00:00</td>
            <td>None</td>
            <td>188 DUANE ST REDWOOD CITY CA 94062</td>
            <td>270 ESCUELA AVE MOUNTAIN VIEW CA 94040</td>
         </tr>
         <tr>
            <td>MIGUEL TORRES</td>
            <td>06:49:00</td>
            <td>07:05:00</td>
            <td>None</td>
            <td>987 PREVOST ST SAN JOSE CA 95125</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>LINDA TRAN</td>
            <td>11:25:00</td>
            <td>11:38:00</td>
            <td>None</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
            <td>3067 OAKBRIDGE DR SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>ISABEL MARTINEZ</td>
            <td>12:15:00</td>
            <td>12:34:00</td>
            <td>None</td>
            <td>751 S BASCOM AVE SAN JOSE CA 95128</td>
            <td>561 VERMONT ST SAN JOSE CA 95110</td>
         </tr>
         <tr>
            <td>ANDREW CARTER</td>
            <td>15:45:00</td>
            <td>16:05:00</td>
            <td>None</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
            <td>2000 MONTEREY HWY SAN JOSE CA 95112</td>
         </tr>
         <tr>
            <td>LUIS RAMIREZ</td>
            <td>10:50:00</td>
            <td>11:10:00</td>
            <td>None</td>
            <td>3133 COLDWATER DR SAN JOSE CA 95148</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>PETER ZHANG</td>
            <td>10:00:00</td>
            <td>10:20:00</td>
            <td>None</td>
            <td>125 CIRO AVE SAN JOSE CA 95128</td>
            <td>60 N 3RD ST SAN JOSE CA 95112</td>
         </tr>
         <tr>
            <td>FELIX GOMEZ</td>
            <td>08:36:00</td>
            <td>08:45:00</td>
            <td>None</td>
            <td>1919 FRUITDALE AVE SAN JOSE CA 95128</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>ANNIE TRAN</td>
            <td>08:15:00</td>
            <td>08:30:00</td>
            <td>None</td>
            <td>3209 KNIGHTSWOOD WAY SAN JOSE CA 95148</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
         </tr>
         <tr>
            <td>SOPHIA HOVSEPIAN</td>
            <td>15:00:00</td>
            <td>15:11:00</td>
            <td>None</td>
            <td>4360 STEVENS CREEK BLVD SAN JOSE CA 95119</td>
            <td>340 NORTHLAKE DR SAN JOSE CA 95117</td>
         </tr>
         <tr>
            <td>ELIZA HARPER</td>
            <td>11:06:00</td>
            <td>11:45:00</td>
            <td>None</td>
            <td>1889 MIDFIELD AVE SAN JOSE CA 95122</td>
            <td>450 BROADWAY ST REDWOOD CITY CA 94063</td>
         </tr>
         <tr>
            <td>PRIYA KAPOOR</td>
            <td>10:07:00</td>
            <td>10:25:00</td>
            <td>None</td>
            <td>1150 TILTON DR SUNNYVALE CA 94087</td>
            <td>610 N PASTORIA AVE SUNNYVALE CA 94085</td>
         </tr>
         <tr>
            <td>KIM NGUYEN</td>
            <td>10:33:00</td>
            <td>10:50:00</td>
            <td>None</td>
            <td>555 UMBARGER RD SAN JOSE CA 95111</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>ANJALI VERMA</td>
            <td>14:31:00</td>
            <td>14:45:00</td>
            <td>None</td>
            <td>2063 FOREST AVE SAN JOSE CA 95128</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>CENTRAL AVENUE 2</td>
            <td>14:00:00</td>
            <td>14:30:00</td>
            <td>None</td>
            <td>270 ESCUELA AVE MOUNTAIN VIEW CA 94040</td>
            <td>2170 STERLING AVE MENLO PARK CA 94025</td>
         </tr>
         <tr>
            <td>LUCIAS SOLIS</td>
            <td>12:45:00</td>
            <td>12:58:00</td>
            <td>None</td>
            <td>610 N PASTORIA AVE SUNNYVALE CA 94085</td>
            <td>260 N BAYVIEW AVE SUNNYVALE CA 94086</td>
         </tr>
         <tr>
            <td>ARMANDO VARGAS</td>
            <td>06:43:00</td>
            <td>07:05:00</td>
            <td>None</td>
            <td>2160 INTERBAY DR SAN JOSE CA 95122</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>RAFAEL CRUZ</td>
            <td>14:47:00</td>
            <td>15:05:00</td>
            <td>None</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
            <td>2121 ALEXIAN DR SAN JOSE CA 95116</td>
         </tr>
         <tr>
            <td>PRIYA KAPOOR</td>
            <td>13:40:00</td>
            <td>13:57:00</td>
            <td>None</td>
            <td>610 N PASTORIA AVE SUNNYVALE CA 94085</td>
            <td>1150 TILTON DR SUNNYVALE CA 94087</td>
         </tr>
         <tr>
            <td>TONY VU</td>
            <td>11:30:00</td>
            <td>11:49:00</td>
            <td>None</td>
            <td>696 E SANTA CLARA ST SAN JOSE CA 95112</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>VICTOR NGO</td>
            <td>16:00:00</td>
            <td>16:17:00</td>
            <td>None</td>
            <td>266 N JACKSON AVE SAN JOSE CA 95116</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>CARLOS RIVERA</td>
            <td>14:15:00</td>
            <td>14:32:00</td>
            <td>None</td>
            <td>2121 ALEXIAN DR SAN JOSE CA 95116</td>
            <td>1161 FRITZEN ST SAN JOSE CA 95122</td>
         </tr>
         <tr>
            <td>MANUEL HERRERA</td>
            <td>10:45:00</td>
            <td>11:10:00</td>
            <td>None</td>
            <td>340 NORTHLAKE DR SAN JOSE CA 95117</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>ADRIAN NAVARRO</td>
            <td>06:28:00</td>
            <td>06:45:00</td>
            <td>None</td>
            <td>1103 AUDUBON DR SAN JOSE CA 95122</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>KEVIN HOANG</td>
            <td>17:00:00</td>
            <td>17:16:00</td>
            <td>None</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
            <td>705 PINTO DR SAN JOSE CA 95111</td>
         </tr>
         <tr>
            <td>HAROLD GRAY</td>
            <td>16:15:00</td>
            <td>16:41:00</td>
            <td>None</td>
            <td>450 BROADWAY ST REDWOOD CITY CA 94063</td>
            <td>1002 W FREMONT AVE SUNNYVALE CA 94087</td>
         </tr>
         <tr>
            <td>MAY LANE</td>
            <td>04:45:00</td>
            <td>05:05:00</td>
            <td>None</td>
            <td>180 N JACKSON AVE SAN JOSE CA 95116</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>DANIEL MENDOZA</td>
            <td>10:10:00</td>
            <td>10:35:00</td>
            <td>None</td>
            <td>120 JOSE FIGUERES AVE SAN JOSE CA 95116</td>
            <td>393 BLOSSOM HILL RD SAN JOSE CA 95123</td>
         </tr>
         <tr>
            <td>EZRA TEKLAY</td>
            <td>13:15:00</td>
            <td>13:33:00</td>
            <td>None</td>
            <td>1040 HAMILTON CT MENLO PARK CA 94025</td>
            <td>649 UNIVERSITY AVE PALO ALTO CA 94301</td>
         </tr>
         <tr>
            <td>JUAN GARCIA</td>
            <td>13:45:00</td>
            <td>14:00:00</td>
            <td>None</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
            <td>3748 UNDERWOOD DR SAN JOSE CA 95117</td>
         </tr>
         <tr>
            <td>CARMEN ORTEGA</td>
            <td>06:03:00</td>
            <td>06:15:00</td>
            <td>None</td>
            <td>2065 FOREST AVE SAN JOSE CA 95128</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>CHARLES THAI</td>
            <td>18:30:00</td>
            <td>18:51:00</td>
            <td>None</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
            <td>1216 FLICKINGER AVE SAN JOSE CA 95131</td>
         </tr>
         <tr>
            <td>CARLOS RIVERA</td>
            <td>10:28:00</td>
            <td>10:45:00</td>
            <td>None</td>
            <td>1161 FRITZEN ST SAN JOSE CA 95122</td>
            <td>2121 ALEXIAN DR SAN JOSE CA 95116</td>
         </tr>
         <tr>
            <td>HAROLD GRAY</td>
            <td>14:33:00</td>
            <td>15:00:00</td>
            <td>None</td>
            <td>1002 W FREMONT AVE SUNNYVALE CA 94087</td>
            <td>450 BROADWAY ST REDWOOD CITY CA 94063</td>
         </tr>
         <tr>
            <td>ELIZA HARPER</td>
            <td>12:45:00</td>
            <td>13:25:00</td>
            <td>None</td>
            <td>450 BROADWAY ST REDWOOD CITY CA 94063</td>
            <td>1889 MIDFIELD AVE SAN JOSE CA 95122</td>
         </tr>
         <tr>
            <td>AMAR SINGH</td>
            <td>09:50:00</td>
            <td>10:10:00</td>
            <td>None</td>
            <td>1515 MARBURG WAY SAN JOSE CA 95133</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
         </tr>
         <tr>
            <td>NANCY BISHOP</td>
            <td>11:15:00</td>
            <td>11:41:00</td>
            <td>None</td>
            <td>420 BROADWAY ST REDWOOD CITY CA 94063</td>
            <td>1102 W FREMONT AVE SUNNYVALE CA 94087</td>
         </tr>
         <tr>
            <td>DANIEL MENDOZA</td>
            <td>09:14:00</td>
            <td>09:30:00</td>
            <td>None</td>
            <td>680 WILLIS AVE SAN JOSE CA 95125</td>
            <td>125 CIRO AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>MARIA SANTOS</td>
            <td>08:00:00</td>
            <td>08:22:00</td>
            <td>None</td>
            <td>301 OLD SAN FRANCISCO RD SUNNYVALE CA 94086</td>
            <td>10150 TORRE AVE CUPERTINO CA 95014</td>
         </tr>
         <tr>
            <td>LUCY PHAN</td>
            <td>08:55:00</td>
            <td>09:15:00</td>
            <td>None</td>
            <td>1125 MALLOW TERRACE SAN JOSE CA 95133</td>
            <td>614 TULLY RD SAN JOSE CA 95111</td>
         </tr>
         <tr>
            <td>ROBERT ESCOBAR</td>
            <td>08:07:00</td>
            <td>08:30:00</td>
            <td>None</td>
            <td>2000 MONTEREY HWY SAN JOSE CA 95112</td>
            <td>2005 NAGLEE AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>HENRY NGUYEN</td>
            <td>13:41:00</td>
            <td>14:00:00</td>
            <td>None</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
         </tr>
         <tr>
            <td>DANIEL MENDOZA</td>
            <td>10:30:00</td>
            <td>10:50:00</td>
            <td>None</td>
            <td>125 CIRO AVE SAN JOSE CA 95128</td>
            <td>680 WILLIS AVE SAN JOSE CA 95125</td>
         </tr>
         <tr>
            <td>OLIVER LEE</td>
            <td>18:30:00</td>
            <td>18:44:00</td>
            <td>None</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
            <td>1300 W SAN CARLOS ST SAN JOSE CA 95126</td>
         </tr>
         <tr>
            <td>DYLAN HUNTER</td>
            <td>15:11:00</td>
            <td>15:25:00</td>
            <td>None</td>
            <td>2063 FOREST AVE SAN JOSE CA 95128</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>JOSHUA LOPEZ</td>
            <td>10:05:00</td>
            <td>10:30:00</td>
            <td>None</td>
            <td>2268 QUIMBY RD SAN JOSE CA 95122</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>MINH TRAN</td>
            <td>10:18:00</td>
            <td>10:35:00</td>
            <td>None</td>
            <td>890 MOSS DR SAN JOSE CA 95116</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
         </tr>
         <tr>
            <td>CHRISTINA VO</td>
            <td>12:36:00</td>
            <td>13:00:00</td>
            <td>None</td>
            <td>1001 S MAIN ST MILPITAS CA 95035</td>
            <td>751 S BASCOM AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>JASON NGUYEN</td>
            <td>15:50:00</td>
            <td>16:10:00</td>
            <td>None</td>
            <td>393 BLOSSOM HILL RD SAN JOSE CA 95123</td>
            <td>2991 SAMARIA PL SAN JOSE CA 95111</td>
         </tr>
         <tr>
            <td>LINDA TRAN</td>
            <td>08:23:00</td>
            <td>08:35:00</td>
            <td>None</td>
            <td>3067 OAKBRIDGE DR SAN JOSE CA 95121</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>MINH TRAN</td>
            <td>14:05:00</td>
            <td>14:22:00</td>
            <td>None</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
            <td>890 MOSS DR SAN JOSE CA 95116</td>
         </tr>
         <tr>
            <td>BEATRICE SERRANO</td>
            <td>14:45:00</td>
            <td>14:59:00</td>
            <td>None</td>
            <td>7019 REALM DR SAN JOSE CA 95119</td>
            <td>5927 SOUTHRIDGE CT SAN JOSE CA 95138</td>
         </tr>
         <tr>
            <td>AMAR SINGH</td>
            <td>13:30:00</td>
            <td>13:49:00</td>
            <td>None</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
            <td>1515 MARBURG WAY SAN JOSE CA 95133</td>
         </tr>
         <tr>
            <td>CONNOR REYNOLDS</td>
            <td>15:45:00</td>
            <td>16:08:00</td>
            <td>None</td>
            <td>1450 KOOSER RD SAN JOSE CA 95118</td>
            <td>2063 FOREST AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>NICHOLAS DAWSON</td>
            <td>05:45:00</td>
            <td>06:00:00</td>
            <td>None</td>
            <td>900 LINCOLN AVE SAN JOSE CA 95126</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>CONNOR REYNOLDS</td>
            <td>10:52:00</td>
            <td>11:15:00</td>
            <td>None</td>
            <td>2063 FOREST AVE SAN JOSE CA 95128</td>
            <td>1450 KOOSER RD SAN JOSE CA 95118</td>
         </tr>
         <tr>
            <td>KIM NGUYEN</td>
            <td>14:50:00</td>
            <td>15:08:00</td>
            <td>None</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
            <td>555 UMBARGER RD SAN JOSE CA 95111</td>
         </tr>
         <tr>
            <td>MAY LANE</td>
            <td>08:35:00</td>
            <td>08:58:00</td>
            <td>None</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
            <td>180 N JACKSON AVE SAN JOSE CA 95116</td>
         </tr>
         <tr>
            <td>MANUEL HERRERA</td>
            <td>15:10:00</td>
            <td>15:35:00</td>
            <td>None</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
            <td>340 NORTHLAKE DR SAN JOSE CA 95117</td>
         </tr>
         <tr>
            <td>RAFAEL CRUZ</td>
            <td>18:35:00</td>
            <td>18:54:00</td>
            <td>None</td>
            <td>2121 ALEXIAN DR SAN JOSE CA 95116</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>ETHAN BRADFORD</td>
            <td>14:00:00</td>
            <td>14:16:00</td>
            <td>None</td>
            <td>2101 FOREST AVE SAN JOSE CA 95128</td>
            <td>1267 MERIDIAN AVE SAN JOSE CA 95125</td>
         </tr>
         <tr>
            <td>EZRA TEKLAY</td>
            <td>08:58:00</td>
            <td>09:15:00</td>
            <td>None</td>
            <td>649 UNIVERSITY AVE PALO ALTO CA 94301</td>
            <td>1040 HAMILTON CT MENLO PARK CA 94025</td>
         </tr>
         <tr>
            <td>ANDREW CARTER</td>
            <td>10:53:00</td>
            <td>11:15:00</td>
            <td>None</td>
            <td>2000 MONTEREY HWY SAN JOSE CA 95112</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>JUAN GARCIA</td>
            <td>10:00:00</td>
            <td>10:15:00</td>
            <td>None</td>
            <td>3748 UNDERWOOD DR SAN JOSE CA 95117</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>SOPHIA HOVSEPIAN</td>
            <td>10:03:00</td>
            <td>10:15:00</td>
            <td>None</td>
            <td>340 NORTHLAKE DR SAN JOSE CA 95117</td>
            <td>4360 STEVENS CREEK BLVD SAN JOSE CA 95119</td>
         </tr>
         <tr>
            <td>MIGUEL TORRES</td>
            <td>11:05:00</td>
            <td>11:21:00</td>
            <td>None</td>
            <td>888 S BASCOM AVE SAN JOSE CA 95128</td>
            <td>987 PREVOST ST SAN JOSE CA 95125</td>
         </tr>
         <tr>
            <td>ANNIE TRAN</td>
            <td>12:00:00</td>
            <td>12:15:00</td>
            <td>None</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
            <td>3209 KNIGHTSWOOD WAY SAN JOSE CA 95148</td>
         </tr>
         <tr>
            <td>CENTRAL AVENUE 1</td>
            <td>14:00:00</td>
            <td>14:31:00</td>
            <td>None</td>
            <td>270 ESCUELA AVE MOUNTAIN VIEW CA 94040</td>
            <td>188 DUANE ST REDWOOD CITY CA 94062</td>
         </tr>
         <tr>
            <td>HENRY NGUYEN</td>
            <td>16:30:00</td>
            <td>16:49:00</td>
            <td>None</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
            <td>2501 ALVIN AVE SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>CHARLES THAI</td>
            <td>14:23:00</td>
            <td>14:45:00</td>
            <td>None</td>
            <td>1216 FLICKINGER AVE SAN JOSE CA 95131</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>CARMEN ORTEGA</td>
            <td>09:45:00</td>
            <td>09:57:00</td>
            <td>None</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
            <td>2065 FOREST AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>ROBERT ESCOBAR</td>
            <td>13:15:00</td>
            <td>13:38:00</td>
            <td>None</td>
            <td>2005 NAGLEE AVE SAN JOSE CA 95128</td>
            <td>2000 MONTEREY HWY SAN JOSE CA 95112</td>
         </tr>
         <tr>
            <td>LUCY PHAN</td>
            <td>12:45:00</td>
            <td>13:07:00</td>
            <td>None</td>
            <td>614 TULLY RD SAN JOSE CA 95111</td>
            <td>1125 MALLOW TERRACE SAN JOSE CA 95133</td>
         </tr>
         <tr>
            <td>MARCUS JONES</td>
            <td>11:28:00</td>
            <td>12:00:00</td>
            <td>None</td>
            <td>809 FREMONT AVE LOS ALTOS CA 94024</td>
            <td>450 BROADWAY ST REDWOOD CITY CA 94063</td>
         </tr>
         <tr>
            <td>KEVIN HOANG</td>
            <td>13:45:00</td>
            <td>14:00:00</td>
            <td>None</td>
            <td>705 PINTO DR SAN JOSE CA 95111</td>
            <td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td>
         </tr>
         <tr>
            <td>KABIR SANDHU</td>
            <td>09:11:00</td>
            <td>09:30:00</td>
            <td>None</td>
            <td>1147 LEIGH AVE SAN JOSE CA 95126</td>
            <td>14651 S BASCOM AVE LOS GATOS CA 95032</td>
         </tr>
         <tr>
            <td>WILBERT LUNA</td>
            <td>15:25:00</td>
            <td>15:42:00</td>
            <td>None</td>
            <td>1450 S WHITE RD SAN JOSE CA 95127</td>
            <td>180 N JACKSON AVE SAN JOSE CA 95116</td>
         </tr>
         <tr>
            <td>CENTRAL AVENUE 2</td>
            <td>08:35:00</td>
            <td>09:00:00</td>
            <td>None</td>
            <td>361 HAMILTON AVE MENLO PARK CA 94025</td>
            <td>270 ESCUELA AVE MOUNTAIN VIEW CA 94040</td>
         </tr>
         <tr>
            <td>ETHAN BRADFORD</td>
            <td>12:45:00</td>
            <td>13:00:00</td>
            <td>None</td>
            <td>1267 MERIDIAN AVE SAN JOSE CA 95125</td>
            <td>2101 FOREST AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>PETER ZHANG</td>
            <td>08:41:00</td>
            <td>09:00:00</td>
            <td>None</td>
            <td>60 N 3RD ST SAN JOSE CA 95112</td>
            <td>125 CIRO AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>MARIA SANTOS</td>
            <td>06:39:00</td>
            <td>07:00:00</td>
            <td>None</td>
            <td>10150 TORRE AVE CUPERTINO CA 95014</td>
            <td>301 OLD SAN FRANCISCO RD SUNNYVALE CA 94086</td>
         </tr>
         <tr>
            <td>DAVID WONG</td>
            <td>14:50:00</td>
            <td>15:09:00</td>
            <td>None</td>
            <td>2121 ALEXIAN DR SAN JOSE CA 95116</td>
            <td>12260 BERRYESSA RD SAN JOSE CA 95133</td>
         </tr>
         <tr>
            <td>KRISHNA PATEL</td>
            <td>14:26:00</td>
            <td>14:45:00</td>
            <td>None</td>
            <td>1695 MENDENHALL DR SAN JOSE CA 95130</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
         </tr>
         <tr>
            <td>NICHOLAS DAWSON</td>
            <td>10:15:00</td>
            <td>10:30:00</td>
            <td>None</td>
            <td>2220 MOORPARK AVE SAN JOSE CA 95128</td>
            <td>900 LINCOLN AVE SAN JOSE CA 95126</td>
         </tr>
         <tr>
            <td>JASON NGUYEN</td>
            <td>11:54:00</td>
            <td>12:15:00</td>
            <td>None</td>
            <td>2991 SAMARIA PL SAN JOSE CA 95111</td>
            <td>393 BLOSSOM HILL RD SAN JOSE CA 95123</td>
         </tr>
      </tbody>
   </table>
</div>
<br>
</details>

### Scheduled Rides
<details>
<summary>Click here to see AI scheduled rides</summary>
<div style="max-height: 200px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; font-size:0.8em"><table border="1" style="width: 100%; border-collapse: collapse;"><thead><tr><th>RIDER</th><th>PICKUP</th><th>APPT_TIME</th><th>ASSET</th><th>PICKUP ADDRESS</th><th>DROPOFF ADDRESS</th></tr></thead><tbody><tr><td>MAY LANE</td><td>04:45:00</td><td>05:05:00</td><td style="color: orange;">SC101_A</td><td>180 N JACKSON AVE SAN JOSE CA 95116</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td></tr><tr><td>LUCIAS SOLIS</td><td>09:02:00</td><td>09:15:00</td><td style="color: orange;">SC101_A</td><td>260 N BAYVIEW AVE SUNNYVALE CA 94086</td><td>610 N PASTORIA AVE SUNNYVALE CA 94085</td></tr><tr><td>ARMANDO VARGAS</td><td>10:35:00</td><td>10:58:00</td><td style="color: orange;">SC101_A</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td><td>2160 INTERBAY DR SAN JOSE CA 95122</td></tr><tr><td>ELIZA HARPER</td><td>11:06:00</td><td>11:45:00</td><td style="color: orange;">SC101_A</td><td>1889 MIDFIELD AVE SAN JOSE CA 95122</td><td>450 BROADWAY ST REDWOOD CITY CA 94063</td></tr><tr><td>PRIYA KAPOOR</td><td>13:40:00</td><td>13:57:00</td><td style="color: orange;">SC101_A</td><td>610 N PASTORIA AVE SUNNYVALE CA 94085</td><td>1150 TILTON DR SUNNYVALE CA 94087</td></tr><tr><td>HAROLD GRAY</td><td>14:33:00</td><td>15:00:00</td><td style="color: orange;">SC101_A</td><td>1002 W FREMONT AVE SUNNYVALE CA 94087</td><td>450 BROADWAY ST REDWOOD CITY CA 94063</td></tr><tr><td>HAROLD GRAY</td><td>16:15:00</td><td>16:41:00</td><td style="color: orange;">SC101_A</td><td>450 BROADWAY ST REDWOOD CITY CA 94063</td><td>1002 W FREMONT AVE SUNNYVALE CA 94087</td></tr><tr><td>NICHOLAS DAWSON</td><td>05:45:00</td><td>06:00:00</td><td style="color: orange;">SC103_A</td><td>900 LINCOLN AVE SAN JOSE CA 95126</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td></tr><tr><td>CARMEN ORTEGA</td><td>06:03:00</td><td>06:15:00</td><td style="color: orange;">SC103_A</td><td>2065 FOREST AVE SAN JOSE CA 95128</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td></tr><tr><td>EZRA TEKLAY</td><td>08:58:00</td><td>09:15:00</td><td style="color: orange;">SC103_A</td><td>649 UNIVERSITY AVE PALO ALTO CA 94301</td><td>1040 HAMILTON CT MENLO PARK CA 94025</td></tr><tr><td>ELIZA HARPER</td><td>12:45:00</td><td>13:25:00</td><td style="color: orange;">SC103_A</td><td>450 BROADWAY ST REDWOOD CITY CA 94063</td><td>1889 MIDFIELD AVE SAN JOSE CA 95122</td></tr><tr><td>ETHAN BRADFORD</td><td>14:00:00</td><td>14:16:00</td><td style="color: orange;">SC103_A</td><td>2101 FOREST AVE SAN JOSE CA 95128</td><td>1267 MERIDIAN AVE SAN JOSE CA 95125</td></tr><tr><td>RAFAEL CRUZ</td><td>14:47:00</td><td>15:05:00</td><td style="color: orange;">SC103_A</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td><td>2121 ALEXIAN DR SAN JOSE CA 95116</td></tr><tr><td>RAFAEL CRUZ</td><td>18:35:00</td><td>18:54:00</td><td style="color: orange;">SC103_A</td><td>2121 ALEXIAN DR SAN JOSE CA 95116</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td></tr><tr><td>ADRIAN NAVARRO</td><td>06:28:00</td><td>06:45:00</td><td style="color: orange;">SC104</td><td>1103 AUDUBON DR SAN JOSE CA 95122</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td></tr><tr><td>FELIX GOMEZ</td><td>08:36:00</td><td>08:45:00</td><td style="color: orange;">SC104</td><td>1919 FRUITDALE AVE SAN JOSE CA 95128</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td></tr><tr><td>AMAR SINGH</td><td>09:50:00</td><td>10:10:00</td><td style="color: orange;">SC104</td><td>1515 MARBURG WAY SAN JOSE CA 95133</td><td>1450 S WHITE RD SAN JOSE CA 95127</td></tr><tr><td>MINH TRAN</td><td>10:18:00</td><td>10:35:00</td><td style="color: orange;">SC104</td><td>890 MOSS DR SAN JOSE CA 95116</td><td>1450 S WHITE RD SAN JOSE CA 95127</td></tr><tr><td>LUIS RAMIREZ</td><td>10:50:00</td><td>11:10:00</td><td style="color: orange;">SC104</td><td>3133 COLDWATER DR SAN JOSE CA 95148</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td></tr><tr><td>FELIX GOMEZ</td><td>12:25:00</td><td>12:36:00</td><td style="color: orange;">SC104</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td><td>1919 FRUITDALE AVE SAN JOSE CA 95128</td></tr><tr><td>KABIR SANDHU</td><td>13:45:00</td><td>14:04:00</td><td style="color: orange;">SC104</td><td>14651 S BASCOM AVE LOS GATOS CA 95032</td><td>1147 LEIGH AVE SAN JOSE CA 95126</td></tr><tr><td>ANJALI VERMA</td><td>14:31:00</td><td>14:45:00</td><td style="color: orange;">SC104</td><td>2063 FOREST AVE SAN JOSE CA 95128</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td></tr><tr><td>OLIVER LEE</td><td>14:46:00</td><td>15:00:00</td><td style="color: orange;">SC104</td><td>1300 W SAN CARLOS ST SAN JOSE CA 95126</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td></tr><tr><td>DYLAN HUNTER</td><td>15:11:00</td><td>15:25:00</td><td style="color: orange;">SC104</td><td>2063 FOREST AVE SAN JOSE CA 95128</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td></tr><tr><td>CONNOR REYNOLDS</td><td>15:45:00</td><td>16:08:00</td><td style="color: orange;">SC104</td><td>1450 KOOSER RD SAN JOSE CA 95118</td><td>2063 FOREST AVE SAN JOSE CA 95128</td></tr><tr><td>MARIA SANTOS</td><td>06:39:00</td><td>07:00:00</td><td style="color: orange;">SC105</td><td>10150 TORRE AVE CUPERTINO CA 95014</td><td>301 OLD SAN FRANCISCO RD SUNNYVALE CA 94086</td></tr><tr><td>LUCY PHAN</td><td>08:55:00</td><td>09:15:00</td><td style="color: orange;">SC105</td><td>1125 MALLOW TERRACE SAN JOSE CA 95133</td><td>614 TULLY RD SAN JOSE CA 95111</td></tr><tr><td>SOPHIA HOVSEPIAN</td><td>10:03:00</td><td>10:15:00</td><td style="color: orange;">SC105</td><td>340 NORTHLAKE DR SAN JOSE CA 95117</td><td>4360 STEVENS CREEK BLVD SAN JOSE CA 95119</td></tr><tr><td>KIM NGUYEN</td><td>10:33:00</td><td>10:50:00</td><td style="color: orange;">SC105</td><td>555 UMBARGER RD SAN JOSE CA 95111</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td></tr><tr><td>TONY VU</td><td>11:30:00</td><td>11:49:00</td><td style="color: orange;">SC105</td><td>696 E SANTA CLARA ST SAN JOSE CA 95112</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td></tr><tr><td>ALEX PARKER</td><td>12:31:00</td><td>13:00:00</td><td style="color: orange;">SC105</td><td>6780 MEADOW VISTA CT SAN JOSE CA 95135</td><td>751 S BASCOM AVE SAN JOSE CA 95128</td></tr><tr><td>HENRY NGUYEN</td><td>13:41:00</td><td>14:00:00</td><td style="color: orange;">SC105</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td><td>1450 S WHITE RD SAN JOSE CA 95127</td></tr><tr><td>KRISHNA PATEL</td><td>14:26:00</td><td>14:45:00</td><td style="color: orange;">SC105</td><td>1695 MENDENHALL DR SAN JOSE CA 95130</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td></tr><tr><td>MANUEL HERRERA</td><td>15:10:00</td><td>15:35:00</td><td style="color: orange;">SC105</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td><td>340 NORTHLAKE DR SAN JOSE CA 95117</td></tr><tr><td>VICTOR NGO</td><td>16:00:00</td><td>16:17:00</td><td style="color: orange;">SC105</td><td>266 N JACKSON AVE SAN JOSE CA 95116</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td></tr><tr><td>KEVIN HOANG</td><td>17:00:00</td><td>17:16:00</td><td style="color: orange;">SC105</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td><td>705 PINTO DR SAN JOSE CA 95111</td></tr><tr><td>ARMANDO VARGAS</td><td>06:43:00</td><td>07:05:00</td><td style="color: orange;">SC106</td><td>2160 INTERBAY DR SAN JOSE CA 95122</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td></tr><tr><td>ANNIE TRAN</td><td>08:15:00</td><td>08:30:00</td><td style="color: orange;">SC106</td><td>3209 KNIGHTSWOOD WAY SAN JOSE CA 95148</td><td>1450 S WHITE RD SAN JOSE CA 95127</td></tr><tr><td>MAY LANE</td><td>08:35:00</td><td>08:58:00</td><td style="color: orange;">SC106</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td><td>180 N JACKSON AVE SAN JOSE CA 95116</td></tr><tr><td>DANIEL MENDOZA</td><td>09:14:00</td><td>09:30:00</td><td style="color: orange;">SC106</td><td>680 WILLIS AVE SAN JOSE CA 95125</td><td>125 CIRO AVE SAN JOSE CA 95128</td></tr><tr><td>TONY VU</td><td>10:12:00</td><td>10:30:00</td><td style="color: orange;">SC106</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td><td>696 E SANTA CLARA ST SAN JOSE CA 95112</td></tr><tr><td>CARLOS RIVERA</td><td>10:28:00</td><td>10:45:00</td><td style="color: orange;">SC106</td><td>1161 FRITZEN ST SAN JOSE CA 95122</td><td>2121 ALEXIAN DR SAN JOSE CA 95116</td></tr><tr><td>MIGUEL TORRES</td><td>11:05:00</td><td>11:21:00</td><td style="color: orange;">SC106</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td><td>987 PREVOST ST SAN JOSE CA 95125</td></tr><tr><td>ISABEL MARTINEZ</td><td>12:15:00</td><td>12:34:00</td><td style="color: orange;">SC106</td><td>751 S BASCOM AVE SAN JOSE CA 95128</td><td>561 VERMONT ST SAN JOSE CA 95110</td></tr><tr><td>CENTRAL AVENUE 1</td><td>14:00:00</td><td>14:31:00</td><td style="color: orange;">SC106</td><td>270 ESCUELA AVE MOUNTAIN VIEW CA 94040</td><td>188 DUANE ST REDWOOD CITY CA 94062</td></tr><tr><td>MIGUEL TORRES</td><td>06:49:00</td><td>07:05:00</td><td style="color: orange;">SC107</td><td>987 PREVOST ST SAN JOSE CA 95125</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td></tr><tr><td>PETER ZHANG</td><td>08:41:00</td><td>09:00:00</td><td style="color: orange;">SC107</td><td>60 N 3RD ST SAN JOSE CA 95112</td><td>125 CIRO AVE SAN JOSE CA 95128</td></tr><tr><td>NANCY BISHOP</td><td>09:35:00</td><td>10:00:00</td><td style="color: orange;">SC107</td><td>1102 W FREMONT AVE SUNNYVALE CA 94087</td><td>420 BROADWAY ST REDWOOD CITY CA 94063</td></tr><tr><td>NANCY BISHOP</td><td>11:15:00</td><td>11:41:00</td><td style="color: orange;">SC107</td><td>420 BROADWAY ST REDWOOD CITY CA 94063</td><td>1102 W FREMONT AVE SUNNYVALE CA 94087</td></tr><tr><td>LUCY PHAN</td><td>12:45:00</td><td>13:07:00</td><td style="color: orange;">SC107</td><td>614 TULLY RD SAN JOSE CA 95111</td><td>1125 MALLOW TERRACE SAN JOSE CA 95133</td></tr><tr><td>JUAN GARCIA</td><td>13:45:00</td><td>14:00:00</td><td style="color: orange;">SC107</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td><td>3748 UNDERWOOD DR SAN JOSE CA 95117</td></tr><tr><td>CHARLES THAI</td><td>14:23:00</td><td>14:45:00</td><td style="color: orange;">SC107</td><td>1216 FLICKINGER AVE SAN JOSE CA 95131</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td></tr><tr><td>SOPHIA HOVSEPIAN</td><td>15:00:00</td><td>15:11:00</td><td style="color: orange;">SC107</td><td>4360 STEVENS CREEK BLVD SAN JOSE CA 95119</td><td>340 NORTHLAKE DR SAN JOSE CA 95117</td></tr><tr><td>CHARLES THAI</td><td>18:30:00</td><td>18:51:00</td><td style="color: orange;">SC107</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td><td>1216 FLICKINGER AVE SAN JOSE CA 95131</td></tr><tr><td>MARIA SANTOS</td><td>08:00:00</td><td>08:22:00</td><td style="color: orange;">SC108</td><td>301 OLD SAN FRANCISCO RD SUNNYVALE CA 94086</td><td>10150 TORRE AVE CUPERTINO CA 95014</td></tr><tr><td>JOSHUA LOPEZ</td><td>10:05:00</td><td>10:30:00</td><td style="color: orange;">SC108</td><td>2268 QUIMBY RD SAN JOSE CA 95122</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td></tr><tr><td>ANDREW CARTER</td><td>10:53:00</td><td>11:15:00</td><td style="color: orange;">SC108</td><td>2000 MONTEREY HWY SAN JOSE CA 95112</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td></tr><tr><td>AMAR SINGH</td><td>13:30:00</td><td>13:49:00</td><td style="color: orange;">SC108</td><td>1450 S WHITE RD SAN JOSE CA 95127</td><td>1515 MARBURG WAY SAN JOSE CA 95133</td></tr><tr><td>CARLOS RIVERA</td><td>14:15:00</td><td>14:32:00</td><td style="color: orange;">SC108</td><td>2121 ALEXIAN DR SAN JOSE CA 95116</td><td>1161 FRITZEN ST SAN JOSE CA 95122</td></tr><tr><td>KIM NGUYEN</td><td>14:50:00</td><td>15:08:00</td><td style="color: orange;">SC108</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td><td>555 UMBARGER RD SAN JOSE CA 95111</td></tr><tr><td>JASON NGUYEN</td><td>15:50:00</td><td>16:10:00</td><td style="color: orange;">SC108</td><td>393 BLOSSOM HILL RD SAN JOSE CA 95123</td><td>2991 SAMARIA PL SAN JOSE CA 95111</td></tr><tr><td>ROBERT ESCOBAR</td><td>08:07:00</td><td>08:30:00</td><td style="color: orange;">SC109</td><td>2000 MONTEREY HWY SAN JOSE CA 95112</td><td>2005 NAGLEE AVE SAN JOSE CA 95128</td></tr><tr><td>CARMEN ORTEGA</td><td>09:45:00</td><td>09:57:00</td><td style="color: orange;">SC109</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td><td>2065 FOREST AVE SAN JOSE CA 95128</td></tr><tr><td>JUAN GARCIA</td><td>10:00:00</td><td>10:15:00</td><td style="color: orange;">SC109</td><td>3748 UNDERWOOD DR SAN JOSE CA 95117</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td></tr><tr><td>DANIEL MENDOZA</td><td>10:30:00</td><td>10:50:00</td><td style="color: orange;">SC109</td><td>125 CIRO AVE SAN JOSE CA 95128</td><td>680 WILLIS AVE SAN JOSE CA 95125</td></tr><tr><td>LINDA TRAN</td><td>11:25:00</td><td>11:38:00</td><td style="color: orange;">SC109</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td><td>3067 OAKBRIDGE DR SAN JOSE CA 95121</td></tr><tr><td>JASON NGUYEN</td><td>11:54:00</td><td>12:15:00</td><td style="color: orange;">SC109</td><td>2991 SAMARIA PL SAN JOSE CA 95111</td><td>393 BLOSSOM HILL RD SAN JOSE CA 95123</td></tr><tr><td>CHRISTINA VO</td><td>12:36:00</td><td>13:00:00</td><td style="color: orange;">SC109</td><td>1001 S MAIN ST MILPITAS CA 95035</td><td>751 S BASCOM AVE SAN JOSE CA 95128</td></tr><tr><td>ALEX PARKER</td><td>14:00:00</td><td>14:30:00</td><td style="color: orange;">SC109</td><td>751 S BASCOM AVE SAN JOSE CA 95128</td><td>6780 MEADOW VISTA CT SAN JOSE CA 95135</td></tr><tr><td>DAVID WONG</td><td>14:50:00</td><td>15:09:00</td><td style="color: orange;">SC109</td><td>2121 ALEXIAN DR SAN JOSE CA 95116</td><td>12260 BERRYESSA RD SAN JOSE CA 95133</td></tr><tr><td>ANDREW CARTER</td><td>15:45:00</td><td>16:05:00</td><td style="color: orange;">SC109</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td><td>2000 MONTEREY HWY SAN JOSE CA 95112</td></tr><tr><td>KRISHNA PATEL</td><td>18:15:00</td><td>18:34:00</td><td style="color: orange;">SC109</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td><td>1695 MENDENHALL DR SAN JOSE CA 95130</td></tr><tr><td>LINDA TRAN</td><td>08:23:00</td><td>08:35:00</td><td style="color: orange;">SC201</td><td>3067 OAKBRIDGE DR SAN JOSE CA 95121</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td></tr><tr><td>KABIR SANDHU</td><td>09:11:00</td><td>09:30:00</td><td style="color: orange;">SC201</td><td>1147 LEIGH AVE SAN JOSE CA 95126</td><td>14651 S BASCOM AVE LOS GATOS CA 95032</td></tr><tr><td>DANIEL MENDOZA</td><td>10:10:00</td><td>10:35:00</td><td style="color: orange;">SC201</td><td>120 JOSE FIGUERES AVE SAN JOSE CA 95116</td><td>393 BLOSSOM HILL RD SAN JOSE CA 95123</td></tr><tr><td>CONNOR REYNOLDS</td><td>10:52:00</td><td>11:15:00</td><td style="color: orange;">SC201</td><td>2063 FOREST AVE SAN JOSE CA 95128</td><td>1450 KOOSER RD SAN JOSE CA 95118</td></tr><tr><td>MICHAEL LAM</td><td>12:00:00</td><td>12:18:00</td><td style="color: orange;">SC201</td><td>200 JOSE FIGUERES AVE SAN JOSE CA 95116</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td></tr><tr><td>LUCIAS SOLIS</td><td>12:45:00</td><td>12:58:00</td><td style="color: orange;">SC201</td><td>610 N PASTORIA AVE SUNNYVALE CA 94085</td><td>260 N BAYVIEW AVE SUNNYVALE CA 94086</td></tr><tr><td>ROBERT ESCOBAR</td><td>13:15:00</td><td>13:38:00</td><td style="color: orange;">SC201</td><td>2005 NAGLEE AVE SAN JOSE CA 95128</td><td>2000 MONTEREY HWY SAN JOSE CA 95112</td></tr><tr><td>MINH TRAN</td><td>14:05:00</td><td>14:22:00</td><td style="color: orange;">SC201</td><td>1450 S WHITE RD SAN JOSE CA 95127</td><td>890 MOSS DR SAN JOSE CA 95116</td></tr><tr><td>BEATRICE SERRANO</td><td>14:45:00</td><td>14:59:00</td><td style="color: orange;">SC201</td><td>7019 REALM DR SAN JOSE CA 95119</td><td>5927 SOUTHRIDGE CT SAN JOSE CA 95138</td></tr><tr><td>WILBERT LUNA</td><td>15:25:00</td><td>15:42:00</td><td style="color: orange;">SC201</td><td>1450 S WHITE RD SAN JOSE CA 95127</td><td>180 N JACKSON AVE SAN JOSE CA 95116</td></tr><tr><td>HENRY NGUYEN</td><td>16:30:00</td><td>16:49:00</td><td style="color: orange;">SC201</td><td>1450 S WHITE RD SAN JOSE CA 95127</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td></tr><tr><td>CENTRAL AVENUE 1</td><td>08:30:00</td><td>09:00:00</td><td style="color: orange;">SC202</td><td>188 DUANE ST REDWOOD CITY CA 94062</td><td>270 ESCUELA AVE MOUNTAIN VIEW CA 94040</td></tr><tr><td>PRIYA KAPOOR</td><td>10:07:00</td><td>10:25:00</td><td style="color: orange;">SC202</td><td>1150 TILTON DR SUNNYVALE CA 94087</td><td>610 N PASTORIA AVE SUNNYVALE CA 94085</td></tr><tr><td>MARCUS JONES</td><td>11:28:00</td><td>12:00:00</td><td style="color: orange;">SC202</td><td>809 FREMONT AVE LOS ALTOS CA 94024</td><td>450 BROADWAY ST REDWOOD CITY CA 94063</td></tr><tr><td>EZRA TEKLAY</td><td>13:15:00</td><td>13:33:00</td><td style="color: orange;">SC202</td><td>1040 HAMILTON CT MENLO PARK CA 94025</td><td>649 UNIVERSITY AVE PALO ALTO CA 94301</td></tr><tr><td>CENTRAL AVENUE 2</td><td>14:00:00</td><td>14:30:00</td><td style="color: orange;">SC202</td><td>270 ESCUELA AVE MOUNTAIN VIEW CA 94040</td><td>2170 STERLING AVE MENLO PARK CA 94025</td></tr><tr><td>CENTRAL AVENUE 2</td><td>08:35:00</td><td>09:00:00</td><td style="color: orange;">SC203</td><td>361 HAMILTON AVE MENLO PARK CA 94025</td><td>270 ESCUELA AVE MOUNTAIN VIEW CA 94040</td></tr><tr><td>PETER ZHANG</td><td>10:00:00</td><td>10:20:00</td><td style="color: orange;">SC203</td><td>125 CIRO AVE SAN JOSE CA 95128</td><td>60 N 3RD ST SAN JOSE CA 95112</td></tr><tr><td>NICHOLAS DAWSON</td><td>10:15:00</td><td>10:30:00</td><td style="color: orange;">SC203</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td><td>900 LINCOLN AVE SAN JOSE CA 95126</td></tr><tr><td>MANUEL HERRERA</td><td>10:45:00</td><td>11:10:00</td><td style="color: orange;">SC203</td><td>340 NORTHLAKE DR SAN JOSE CA 95117</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td></tr><tr><td>ANNIE TRAN</td><td>12:00:00</td><td>12:15:00</td><td style="color: orange;">SC203</td><td>1450 S WHITE RD SAN JOSE CA 95127</td><td>3209 KNIGHTSWOOD WAY SAN JOSE CA 95148</td></tr><tr><td>ETHAN BRADFORD</td><td>12:45:00</td><td>13:00:00</td><td style="color: orange;">SC203</td><td>1267 MERIDIAN AVE SAN JOSE CA 95125</td><td>2101 FOREST AVE SAN JOSE CA 95128</td></tr><tr><td>KEVIN HOANG</td><td>13:45:00</td><td>14:00:00</td><td style="color: orange;">SC203</td><td>705 PINTO DR SAN JOSE CA 95111</td><td>1620 E CAPITOL EXPY SAN JOSE CA 95121</td></tr><tr><td>VICTOR NGO</td><td>14:41:00</td><td>15:00:00</td><td style="color: orange;">SC203</td><td>2501 ALVIN AVE SAN JOSE CA 95121</td><td>266 N JACKSON AVE SAN JOSE CA 95116</td></tr><tr><td>ANJALI VERMA</td><td>18:15:00</td><td>18:28:00</td><td style="color: orange;">SC203</td><td>888 S BASCOM AVE SAN JOSE CA 95128</td><td>2063 FOREST AVE SAN JOSE CA 95128</td></tr><tr><td>OLIVER LEE</td><td>18:30:00</td><td>18:44:00</td><td style="color: orange;">SC203</td><td>2220 MOORPARK AVE SAN JOSE CA 95128</td><td>1300 W SAN CARLOS ST SAN JOSE CA 95126</td></tr></tbody></table></div>
<BR>
</details>

## Training

<!-- The training process uses a flavor of the Reinforcement Learning algorithm Proximal Policy Optimization (PPO) that retains long term memory of best practices from day to day using a carefully tuned learning rate. The agent is rewarded for completing rides on time, minimizing mileage, and distributing rides efficiently across the assets. The agent learns from its interactions with the environment and gradually improves its scheduling policy. -->

Each episode (iteration) during training, the agent loops the rides, taking actions that are an advantage in maximizing the cumulative reward.

![Ride Assignments Animation](./animations/ride_assignments_with_rewards.gif)



### Performance
<div style="margin-left: 130px;">TensorBoard performance metrics for the final training phase, all results are in the intended range.</div>

<table>
   <!-- <tr>
    <td style="text-align: center;">
      <img src="./graphs/Aggregate_Reward_Avg.svg" alt="Aggregate Reward Avg" width="300" />
      <div style="margin-left:40px;">Cumulative Rewards Avg</div>
   </td>
   </tr>  -->
  <tr>
    <td style="text-align: center;">
      <img src="./graphs/mile_reward_avg.svg" alt="Mile Difference Avg" width="300" />
      <div style="margin-left:40px;">Mile Reward Avg</div>
    </td>
        <td style="text-align: center;">
      <img src="./graphs/mile_diff_avg.svg" alt="On-Time Performance Reward Avg.svg" width="300" />
      <div style="margin-left:40px;">Mile Difference Avg</div>
    </td>
    <td style="text-align: center;">
      <img src="./graphs/mileage_std.svg" alt="mileage_std.svg" width="300" />
      <div style="margin-left:60px;">Mileage Standard Deviation</div>

  </tr>
  <tr>
  </tr>
    <tr>
      <td style="text-align: center;">
      <img src="./graphs/load_balance_reward_avg.svg" alt="load_balance_reward_avg.svg" width="300" />
      <div style="margin-left:60px;">Load Balance Reward Avg</div>
    </td>
       <td style="text-align: center;">
      <img src="./graphs/load_std.svg" alt="load_std.svg" width="300" />
      <div style="margin-left:60px;">Load Balance Standard Deviation</div>
    </td>
   <td style="text-align: center;">
      <img src="./graphs/on_time_rewards.svg" alt="on_time_rewards.svg" width="300" />
      <div style="margin-left:60px;">On-Time Performance Reward Avg</div>
    </td>

  </tr>

  
</table>








<!-- ## Usage

1. **Training the agent:**
   Run the training script to train RL agents:

   ```bash
   python src/main.py --train
   ```

2. **Evaluating Performance:**
   Test the trained agent on new data:

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
   ``` -->

---

## Metrics Tracked

### **1. Ride Completion Rate:**
- Depending on shift durations and specific rule parameters around time allowances, mileage restrictions, etc., there can be a small set of rides that go unscheduled for a given set.

### **2. Efficiency Metrics**
- **Miles Per Ride:** Average distance traveled per ride.
- **Idle Time Minimization:** Percentage of time assets spend idle during their shifts.
- **Average Utilization Rate:** Time spent on rides versus total available shift time for assets.
![Ride Assignments Animation](./graphs/efficiency_metrics.png)


### **3. Distance Efficiency and Agent Behavior**

   <img src="./animations/ride_clustering.gif" style="width: 100%;" > 

Above, we can see the agent's scheduling decisions for each asset. Notice that the agent focuses on clustering rides together, and that long trips tend to lead to clusters of rides. It’s important to note that the agent will select rides further away if time rewards can be enhanced by combining them with available mileage and load balance rewards, ultimately achieving a higher cumulative reward. 

The agent is able to use historical traffic patterns to very closely predict the approximate travel time at a given time day and even along a given route based on several features within the dataset. This allows the agent's decisions to be more in line with reality.

### **4. Cost Reduction**
- **Fuel Cost Reduction:** The agent solves the problem of maximizing fuel efficiency by custering rides based on mileage, long legs will often lead to clusters, but time composition is the primary determing factor that influences location outcomes.

- **Driver Hours Reduction:** From June 2024 to December 2024, while the number of drivers has remained relatively stable, the focus has shifted toward improving the quality of work. The company using ALTR has started emphasizing hiring practices that prioritize driver capability, particularly their ability to meet the schedules generated by the agent. Over time, this approach may reduce some labor costs, but it is more likely to result in an increase in the number of drivers as improved efficiency drives company growth.

### **5. Scalability**

- **Time to Converge:** Convergence in the current version takes approximately 140,000 steps, improvement is observed every 20,000.
- **Inference Time:** Each schedule on the current hardware used takes about 1 minute (with multi-loading)

### **6. Performance in Edge Cases:**

-  Edge cases are handled through the reward system. If the agent is insufficiently incentivized, it passes the task to a human scheduler. The agent adapts by selecting high-mileage rides that lead to clusters of low-mileage, time-efficient rides, ultimately generating a substantial reward. It also waits for low-mileage opportunities when no other rewards are available, maximizing cumulative reward. For example, if an asset drops off at a dialysis clinic and sufficient rewards are present from that state, the agent waits for the next advantageous time reward, creating small gaps that offer flexibility to human schedulers while ensuring baseline efficiency.

---

### **7. Human Intervention**
- **Skipped Rides:** The agent sometimes skips rides if they can't be fit into an optimal long-term plan, leaving human schedulers to handle adjustments outside the agent's rules. While there are quantifiable rules, some non-quantifiable ones are better managed by humans for now. Future versions will aim to reduce human intervention through a cooperative multi-agent system, where each agent has special rules and can generate "what if" scenarios, such as showing how the schedule might look with additional assets when there aren't enough available.


---

### **8. Multi-Loading**

- **Efficiency of Multi-Loading Assets:** Multi-loading enhances efficiency by strategically pairing compatible rides into "batches," which the agent then processes as a single unit. This approach minimizes the likelihood of skipped rides by ensuring that each asset operates at its fullest potential, without overlooking opportunities for pairing that might otherwise go unused. By grouping rides in a way that optimizes mileage, time and load balance, the system reduces inefficiencies and allows for better use of available assets, ultimately leading to a smoother, more streamlined scheduling process. However a positional multi-load and pre-load system is being planned for future versions.

### **9. Pre-Loading and Asset Ride Assignment**
- Pre-loading is an upcoming feature designed to assign specific rides to designated assets, with the goal of enabling preference-based scheduling. This feature is not fully tested or implemented, but will be integrated into the system in future versions.

### **10. Scheduled Breaks**

- **Integrated Breaks for Planned Downtime:** Not yet fully implemented, future versions will include user specified breaks for each asset. The agent will seamlessly schedule around these time blocks with the same level of efficiency in mileage and OTP.


## Interactive Dashboard
Coming soon <span style="font-size: 2em;">👨‍🔬</span>


## Future Work

- Integration with real-world datasets for live scheduling.
- Enhanced scalability to handle thousands of rides.
- Improved multi-agent collaboration for global optimization.
