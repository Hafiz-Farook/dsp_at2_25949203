# Building Currency Converter in Python – Data Science Practice (94692) AT2

**Student name:** Hafiz Farook
**Student ID:** 25949203 

---

## Project Description

This project is a simple foreign-exchange (FX) converter web application built
with **Python** and **Streamlit**. It uses the public
[Frankfurter](https://www.frankfurter.app/) API to:

- Fetch the list of available currencies.
- Retrieve the latest conversion rate between two selected currencies.
- Retrieve the historical conversion rate on a user-selected date.
- Display the converted amount and the inverse exchange rate.

The application allows users to:

1. Enter an amount to be converted.  
2. Select a **from** currency and a **to** currency.  
3. Click **Get Latest Rate** to show the latest conversion information.  
4. Choose a past date and click **Conversion Rate** to show the historical
   conversion information.

The displayed message follows the convention:

> The conversion rate on \<date\> from \<from currency\> to \<to currency\> was \<rate\>.  
> So \<from amount\> in \<from currency\> correspond to \<to amount\> in \<to currency\>  
> The inverse rate was \<inverse rate\>.

---

## File Overview

### `app.py`
- Main Streamlit application.
- Handles user interface:
  - Amount input
  - Currency selection
  - Latest rate button and result box
  - Historical date input
  - Historical rate button and result box
- Uses functions from `frankfurter.py` and `currency.py`.

### `api.py`
- Low-level helper for calling the Frankfurter API.
- Functions:
  - `get(endpoint: str, params: dict | None = None) -> dict`  
    Makes a GET request and returns the parsed JSON response.

### `frankfurter.py`
- Contains functions specific to the Frankfurter API.
- Functions:
  - `get_currencies() -> dict` – returns all available currency codes and names.  
  - `get_latest_rate(from_currency: str, to_currency: str) -> (str, float)` – returns latest date and rate.  
  - `get_historical_rate(on_date, from_currency: str, to_currency: str) -> (str, float)` – returns date and rate for the requested (or nearest available) date.

### `currency.py`
- Contains formatting logic for display text.
- Functions:
  - `format_conversion_text(date_str, from_currency, to_currency, rate, from_amount) -> str`  
    Returns a string following the required text convention.

---

## How to Run the Web App

### 1. Install dependencies

Make sure you have Python 3.10+ installed.  
From the folder containing the files (`app.py`, `api.py`, `frankfurter.py`, `currency.py`, `README.md`):

```bash
pip install streamlit requests

