# Utility Functions Documentation

This document provides an overview of the reusable functions implemented in `src/utils.py`.  
These utilities are designed to simplify common data preprocessing tasks such as cleaning column names and parsing dates.

---

## 1. `clean_column_names(df)`
**Description:**  
Cleans the column names of a pandas DataFrame by converting them to lowercase, stripping whitespace, and replacing spaces with underscores.  
This ensures consistent and standardized column naming across different datasets.

**Parameters:**
- `df` (*pd.DataFrame*): The input DataFrame whose columns need to be cleaned.

**Returns:**
- *pd.DataFrame*: A DataFrame with cleaned column names.

**Example Usage:**
```python
from src.utils import clean_column_names
import pandas as pd

data = pd.DataFrame({
    "First Name": ["Alice", "Bob"],
    " Last Name ": ["Smith", "Jones"]
})

cleaned_df = clean_column_names(data)
print(cleaned_df.columns)
# Output: ['first_name', 'last_name']
