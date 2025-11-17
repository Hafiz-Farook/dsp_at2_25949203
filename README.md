# Building Currency Converter in Python – Data Science Practice (94692) AT2

**Student Name:** Hafiz Farook  
**Student ID:** 25949203

---

## 📘 Project Description

This project is an interactive **Streamlit web application** that performs currency conversion using the open-source **Frankfurter API**.

The app allows users to:

- Enter an amount  
- Select a source and target currency  
- Fetch the **latest conversion rate**  
- Select a **historical date**  
- View:
  - Conversion rate  
  - Converted amount  
  - Inverse conversion rate  

All results follow this required format:
The conversion rate on <date> from <from currency> to <to currency> was <rate>.
So <from amount> in <from currency> correspond to <to amount> in <to currency>
The inverse rate was <inverse rate>


---

## 📁 File Overview

Your submission contains **five Python files** (no folders):

### `app.py`
Main Streamlit application.  
Handles:
- User input  
- Currency selection  
- Latest and historical conversions  
- Displaying results  

### `api.py`
Contains the low-level function:

- `get(endpoint, params=None)`  
  Performs HTTP GET requests to the Frankfurter API.

### `frankfurter.py`
Contains API-specific functions:
- `get_currencies()`
- `get_latest_rate(from_currency, to_currency)`
- `get_historical_rate(date, from_currency, to_currency)`

### `currency.py`
Contains:
- `format_conversion_text()`  
  Formats the output message exactly in the required style.

### `README.md`
Project documentation (this file).

---

## 🚀 How to Run the Web App

Follow these steps in your terminal:

### **1. Navigate to your project folder**
Replace `<path>` with the location of your files:

cd <path to your folder>

Example (Windows):
cd C:\Users\YourName\Documents\dsp_at2_25949203


---

### **2. Install required Python packages**

Run these commands:

pip install streamlit

pip install requests


If pip doesn't work, try:

python -m pip install streamlit

python -m pip install requests


---

### **3. Run the Streamlit application**

streamlit run app.py


Streamlit will open automatically in your browser.  
If not, open the link shown in the terminal:

http://localhost:8501


---

## 🔧 Functions Summary

### api.py
| Function | Description |
|----------|-------------|
| `get()` | Sends HTTP GET request to Frankfurter and returns JSON |

### frankfurter.py
| Function | Description |
|----------|-------------|
| `get_currencies()` | Returns currency list |
| `get_latest_rate()` | Latest FX rate and date |
| `get_historical_rate()` | Historical FX rate for selected date |

### currency.py
| Function | Description |
|----------|-------------|
| `format_conversion_text()` | Generates formatted output text |

---

## 📦 Submitted files

the submitted ZIP file is named:

dsp_at2_259203.zip


It contains only the following files:
app.py

api.py

frankfurter.py

currency.py

README.md


