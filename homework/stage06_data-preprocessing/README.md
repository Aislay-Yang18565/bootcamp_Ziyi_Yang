## Homework 6 Data Cleaning Strategy

### Processing Steps
1. **Drop excessive missing data**: Drop columns with more than 30% missing values, then drop any rows with remaining missing values
2. **Median imputation**: Fill remaining missing values in numerical variables using median
3. **Data normalization**: Apply Z-score normalization to numerical variables

### Assumptions and Decisions
- Prioritize data quality over data quantity
- Use median imputation for numerical variables as it's robust to outliers
- Normalize all numerical variables to prepare for machine learning modeling

### File Descriptions
- `cleaning.py`: Contains all data cleaning functions
- `stage06_data_preprocessing.ipynb`: Main notebook for data cleaning process
- `data/processed/cleaned_dataset.csv`: Cleaned dataset
- `data/processed/cleaning_report.txt`: Cleaning process report
- `data/processed/cleaning_assumptions.md`: Cleaning assumptions and decisions documentation