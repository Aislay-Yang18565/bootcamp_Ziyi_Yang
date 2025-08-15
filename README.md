# bootcamp_Ziyi_Yang

# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.
## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.



Here's the professional English version of your textile trade project scoping document:

### # Project Title: **Textile Import-Export Profitability Optimizer**  
**Stage:** Problem Framing & Scoping  

### # Problem Statement  
Traditional textile traders experience 18-22% profit erosion due to cotton price volatility and inefficient logistics routes. Current manual forecasting methods result in 30% procurement decision errors, causing annual losses of approximately $2.4M for mid-sized enterprises.  

### # Stakeholder & User  
- **Decision-maker**: CFO (approves cotton purchases >500 metric tons)  
- **End-users**:  
  - Procurement team (schedules orders based on forecasts)  
  - Logistics managers (implements recommended shipping routes)  
- **Critical timing**: Reports must be generated 2 weeks before quarterly supplier negotiations  

### # Useful Answer & Decision  
- **Analysis type**: Predictive  
- **Key metrics**:  
  - Cotton price prediction accuracy (±5% error margin)  
  - Percentage reduction in logistics costs  
- **Deliverable**: Interactive dashboard containing:  
  - 90-day price forecast curves  
  - Optimal maritime shipping routes  

### # Assumptions & Constraints  
- **Data**: Access to ICE Futures historical data, but no supplier contract details (NDA-protected)  
- **Latency**: Weekly data updates must process within ≤2 hours  
- **Compliance**: Must adhere to INCOTERMS 2020 regulations  

### # Repo Plan  
| Directory      | Purpose                     | Update Frequency |  
|----------------|-----------------------------|------------------|  
| /data/raw      | Raw ICE Futures data         | Weekly (Mon 9AM) |  
| /notebooks/    | Price forecasting models     | Biweekly         |  

