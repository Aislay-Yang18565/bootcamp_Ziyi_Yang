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



Here's a complete example for the traditional trade industry (focusing on textile export-import operations):

---

### # Project Title: **Textile Trade Profitability Optimizer**  
**Stage:** Problem Framing & Scoping (Stage 01)  

---

### # Problem Statement  
Traditional textile traders face 18-22% profit erosion due to volatile cotton prices and inefficient logistics routing. Manual price forecasting methods result in 30% inaccurate procurement decisions, causing $2.4M annual losses for mid-sized trading firms. The CFO (primary stakeholder) needs data-driven tools to optimize purchase timing and shipping routes before quarterly supplier negotiations in March/September.  

---

### # Stakeholder & User  
- **Decision-maker**: CFO - Approves bulk cotton purchases (>500MT) based on cost projections  
- **End-users**:  
  - Procurement team - Uses price forecasts to time orders  
  - Logistics managers - Implements recommended shipping routes  
- **Workflow**: Forecasts required 48hrs before biweekly procurement meetings  

---

### # Useful Answer & Decision  
- **Type**: Predictive analytics  
- **Metrics**:  
  - Cotton price prediction accuracy (±5% of actual)  
  - Logistics cost reduction (% saved vs current routes)  
- **Artifact**: Interactive dashboard showing:  
  - 90-day price trend forecasts  
  - Optimal shipping route maps  

---

### # Assumptions & Constraints  
- **Data**:  
  - Available: Historical cotton prices (ICE Futures), port fees, fuel costs  
  - Unavailable: Supplier-specific contract terms (NDA-protected)  
- **Technical**:  
  - Max 2hr processing time for weekly data refresh  
  - Must integrate with existing ERP system (SAP)  
- **Compliance**: Adhere to INCOTERMS 2020 trade rules  

---

### # Known Unknowns / Risks  
- **Volatility factors**:  
  - Unpredictable weather impacts on cotton yield  
  - Geopolitical disruptions to shipping lanes  
- **Mitigation**:  
  - Monitor USDA crop reports weekly  
  - Build 3 scenario models (optimistic/neutral/pessimistic)  

---

### # Lifecycle Mapping  
| Goal → | Stage → | Deliverable → |  
|--------|---------|---------------|  
| Define cost drivers | Stage 01 | Cotton market analysis report |  
| Predict price trends | Stage 02 | Time-series forecasting model |  
| Optimize logistics | Stage 03 | Route optimization API |  

---

### # Repo Plan  
- **/data/**:  
  - `raw/` - ICE Futures historical data (CSV)  
  - `processed/` - Cleaned price trajectories (Parquet)  
- **/src/**: Python scripts for SAP data extraction  
- **/notebooks/**:  
  - `price_forecasting.ipynb` (Prophet model)  
  - `route_optimization.ipynb` (OR-Tools)  
- **/docs/**:  
  - `stakeholder_memo.md`  
  - `incoterms_compliance.pdf`  

**Update cadence**:  
- Commit price data every Monday 9AM GMT  
- Push model improvements biweekly  

---

### Key Features for Traditional Trade:  
1. **Compliance-focused**: Built-in INCOTERMS rule checker  
2. **Double-layer validation**: Compare ML forecasts with veteran traders' intuition  
3. **Explainable outputs**: Audit-ready decision trails for customs compliance  

This template addresses unique pain points in physical commodity trading while meeting academic requirements. Would you like me to adjust any section (e.g., add more technical specifics for the predictive model)?
