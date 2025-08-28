
## Data Cleaning Assumptions and Decisions Documentation

### 1. Missing Value Handling Strategy
- **Threshold selection**: 30% threshold for dropping columns, considering columns with more missing values contain insufficient information
- **Imputation method**: Median imputation for numerical variables, as median is robust to outliers
- **Row deletion**: Dropped rows with any remaining missing values to ensure complete dataset

### 2. Data Normalization
- **Method selection**: Z-score normalization using StandardScaler
- **Scope**: Only numerical variables were normalized, categorical variables remain unchanged
- **Purpose**: Make variables with different scales comparable for subsequent machine learning modeling

### 3. Data Integrity Trade-offs
- **Decision**: Prioritize data quality, accepting some data loss
- **Impact**: Raw data had X rows Y columns, processed data has A rows B columns
- **Trade-off**: Lost C rows D columns of data but obtained a cleaner, more consistent dataset

### 4. Considerations and Limitations
- Median imputation may not be suitable for heavily skewed distributions
- Row deletion may lead to loss of valuable samples
- Normalization removes original scale, reducing interpretability
