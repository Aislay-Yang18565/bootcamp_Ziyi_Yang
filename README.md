# bootcamp_Ziyi_Yang

# Homework 0 Bootcamp Repository
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



# Homework 1 Project Title: **Textile Import-Export Profitability Optimizer**  
**Stage:** Problem Framing & Scoping  

# Problem Statement  
Textile traders experience 18-22% profit erosion due to cotton price volatility and inefficient logistics routes. Current manual forecasting methods result in 30% procurement decision errors, causing annual losses of $2.4M for mid-sized enterprises.  

# Stakeholder & User  
- **Decision-maker**: CFO (approves cotton purchases >500MT)  
- **End-users**:  
  - Procurement team (schedules orders based on forecasts)  
  - Logistics managers (implements recommended shipping routes)  
- **Critical timing**: Reports required 2 weeks before quarterly supplier negotiations  

# Useful Answer & Decision  
- **Analysis type**: Predictive  
- **Key metrics**:  
  - Cotton price prediction accuracy (±5% error margin)  
  - Logistics cost reduction percentage  
- **Deliverable**: Dashboard containing:  
  - 90-day price forecast curves  
  - Optimal shipping route maps  

# Assumptions & Constraints  
- **Data**: Access to ICE Futures history but no supplier contracts (NDA-protected)  
- **Latency**: Weekly data updates must process within ≤2 hours  
- **Compliance**: Must follow INCOTERMS 2020 regulations  

## Lifecycle Mapping
| Goal                  | Stage     | Deliverable                     |
|-----------------------|-----------|---------------------------------|
| Define cost drivers   | Stage 01  | Cotton market analysis report   |
| Predict price trends  | Stage 02  | Time-series forecasting model   |
| Optimize logistics    | Stage 03  | Route optimization API          |

# Repo Plan   
- **data/**:  
  - **raw/**: ICE Futures historical data (CSV) 
  - **processed/**: Cleaned price trajectories (Parquet)
- **src/**: Python scripts for SAP data extraction 
- **notebooks/**: Dashboard containing:  
  - **price_forecasting.ipynb**
  - **route_optimization.ipynb**
- **docs/**: Dashboard containing:  
  - **stakeholder_memo.md**: Stakeholder communication
  - **incoterms_compliance.pdf**: Trade regulations

| Directory    | Purpose                  | Update Frequency |  
|--------------|--------------------------|------------------|  
| /data/raw    | Raw ICE Futures data     | Weekly           |  
| /notebooks/  | Price forecasting models | Biweekly         |  


