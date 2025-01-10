## **ALTR SCHEDULING PRESENTATION STRUCTURE**


0. INTRODUCTIONS
- How was your holiday break?
- So what's your vision for automated scheduling?
- The project is called ALTR, A-L-T-R **Advantage Leveraging Transit Reinforcement**
- Basically what it does is it automates ride scheduling with a focus on optimizing mileage reduction, on-time performance, and load balance across assets.

- **Summary of Key Points for the Current Version of ALTR:**  
    - **What ALTR Is:** A system that intelligently plans rides and asset usage across the day. It continuously learns from daily operations, updating its scheduling policies to adapt to daily, weekly, and monthly trends.  
    
    - **What ALTR Is Not:** It is not a real-time positional system that continuously tracks and optimizes based on the dynamic positions and loads of all assets. Although I have a plan for this enhancement in the near future.
    
    - **Current Focus:** Is the optimization of wheelchair-based rides. Support for ambulatory and gurney rides is in development as additional layers to the core intelligence system. 

- **Upcoming features:** 
    - Assigned breaks
    - Pre-loading
        - Imagine having a fixed contract with a school district where a specific asset is assigned to pick up students from the school at a designated time every day. With this system, you can effortlessly allocate specific rides to particular assets. The AI will seamlessly generate an optimized schedule around these fixed assignments, ensuring efficiency and accommodating other rides without conflict.

    - Live Dispatch
        - The AI continuously optimizes the schedule by fitting unassigned rides into it as changes occur, such as new ride requests or cancellations. For example, if a hospital requests a discharge, the AI evaluates feasibility and, if possible, updates the schedule accordingly. This dynamic approach ensures efficient scheduling and adaptability.

    - Ghost Assets: 
        - The system avoids discarding critical ride requests, such as hospital discharges. Instead, it informs the user of potential outcomes if additional assets were available. For scenarios with many unassigned rides, it generates a mock schedule for hypothetical "ghost assets," showing how all rides could fit into a complete schedule. This helps transportation providers understand the benefits of adding extra vehicles, or potential outsourcing opportunities.

1. LIVE DEMO WITH RIDES
    - Run Inference
    - Explain the Hour Distribution bar chart
    - **Calculated Means**:
        - **Average to understand the general performance.**
        - **Standard deviation to assess consistency.**
        - These are some key metrics that allow me to analyze the quality of a given schedule.
        - Load STD tells me how well the model did during a single run in terms of balancing the load
        - Mileage STD typical difference from the mean mileage
        - Episode cumulative reward is used for measuring against a string of days in order to acertain the learning trend.

    - **Schedule Generation**:
        - **6/3** has **118 rides** and **13 left out**
        - At the top you will notice under the asset column the word "Human"
        - **Human** is assigned to an asset when the AI can't fit it into the optimized schedule for some reason.

        - **Batching** rides can be batched together, but this isn’t true multi-loading in the sense that we're fitting rides to available positions at specific times while simultaneously understanding all other load situations across the assets to determine the best overall fit. While this is completely possible, it’s outside the scope of the current version of ALTR.

        - Instead, there’s an algorithm that searches for batching opportunities and selects the option with the highest value to pair a given ride with. The batching format is strictly one-to-one, meaning only two rides can be batched together at any given time.

    - **Estimated Return Times**
        - In ALTR, all rides have set pickup and dropoff times, eliminating will-call systems. Return ride pickups are treated as estimated times, with the dispatch module ensuring flexibility and adherence to broker rules. This approach minimizes wait times and ensures efficient returns within the required 30–45 minutes.


