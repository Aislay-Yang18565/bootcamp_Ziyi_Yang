
### Format Choices
- **CSV** for raw data because:
  - Human-readable
  - Universally supported
  - Preserves exact source format
  
- **Parquet** for processed data because:
  - Binary format (smaller files)
  - Preserves data types
  - Columnar storage (faster queries)
  - Built-in compression

### Environment Configuration
Paths are configured in `.env`:
```ini
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed