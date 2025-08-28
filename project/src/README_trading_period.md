# Utility Functions Documentation

This document explains the reusable utility functions provided in `src/utils.py`.  
They are designed for use in trading and financial data analysis, especially when 
holiday effects or special rest periods need to be considered.

---

## `is_before_major_holiday(date)`

**Description:**  
Checks whether a given date falls within one week before major holidays.  
Currently, the major holidays included are:
- **National Day (October 1st)**  
- **Spring Festival (Chinese Lunar New Year, exact dates for 2019–2025)**  

**Arguments:**  
- `date` (str or datetime): The input date.

**Returns:**  
- `True` if the date is within 7 days before a major holiday.  
- `False` otherwise.  

**Future Use:**  
- Useful in trading strategies where market activity tends to decrease or increase before major holidays.  
- Can be extended by adding more holidays or automatically fetching holiday calendars from APIs.

---

## `is_rest_period(date)`

**Description:**  
Determines whether the given date falls within a "rest period" — defined as the 
week before, the week of, and the week after the 10th of **April, August, or December**.  

**Arguments:**  
- `date` (str or datetime): The input date.  

**Returns:**  
- `True` if the date falls in the rest period.  
- `False` otherwise.  

**Future Use:**  
- Designed to flag low-liquidity or inactive trading periods for agricultural products.  
- Can be generalized to other "blackout" or "no-trading" windows.  

---

## `is_next_day_rest_period(date)`

**Description:**  
Checks if the **next day** after the given date falls within a rest period.  
It builds on the `is_rest_period()` function.  

**Arguments:**  
- `date` (str or datetime): The input date.  

**Returns:**  
- `True` if the next day is a rest period.  
- `False` otherwise.  

**Future Use:**  
- Useful in backtesting or live trading strategies when deciding whether to hold a position overnight.  
- Can be combined with scheduling logic to automatically skip placing trades before rest days.  

---
