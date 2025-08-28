# Data Cleaning Assumptions and Rationale

1. **Filter out future dates:**  
   - Assumption: Excel files may contain projected or placeholder future values.  
   - Rationale: Only past and current market data should be used for strategy backtesting.  

2. **Convert columns to float:**  
   - Assumption: Price/volume columns should be numeric.  
   - Rationale: Ensures compatibility with calculations and prevents errors from mixed types.  

3. **Extract last 2 years of data:**  
   - Assumption: Recent data better reflects current market behavior.  
   - Rationale: Keeps datasets manageable and focuses on relevant trading periods.  

4. **Save as CSV in `/data/processed/`:**  
   - Assumption: Cleaned data will be reused across multiple experiments.  
   - Rationale: Avoids re-running preprocessing steps and standardizes data format.  
