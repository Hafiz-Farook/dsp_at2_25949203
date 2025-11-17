# Building Currency Converter in Python – Data Science Practice (94692) AT2

**Student Name:** Hafiz Farook
**Student ID:** 25949203

---

## 📘 Project Description

This project is an interactive **Streamlit web application** that performs currency conversion using data from the open-source **Frankfurter API**.

Users can:

- Enter an amount they want to convert  
- Select a **source currency**  
- Select a **target currency**  
- Fetch the **latest conversion rate**  
- Select a **historical date** and fetch the **rate for that day**  
- View:
  - Conversion rate  
  - Converted amount  
  - Inverse conversion rate  

All results follow the required text format:

The conversion rate on <date> from <from currency> to <to currency> was <rate>.
So <from amount> in <from currency> correspond to <to amount> in <to currency>
The inverse rate was <inverse rate>.

---

## 📁 File Overview

Your project must contain **exactly five files** (no folders):

### **1. app.py**
- Main Streamlit application  
- Manages user input and UI  
- Calls functions from `frankfurter.py`  
- Displays latest and historical conversion results  

### **2. api.py**
- Contains the low-level function for making HTTP GET requests  
- Used internally by `frankfurter.py`  

### **3. frankfurter.py**
- Contains all functions that call the Frankfurter endpoints:
  - `get_currencies()`
  - `get_latest_rate()`
  - `get_historical_rate()`

### **4. currency.py**
- Contains the function that formats results into the required text style:
  - `format_conversion_text()`

### **5. README.md**
- Project documentation (this file)

---

## 🚀 How to Run the Web App

### **1. Install required packages**

Make sure you have Python 3.10+ installed.

In your terminal:

```bash
pip install streamlit requests

2. Run the Streamlit app

Inside the folder containing your project files:

streamlit run app.py

3. Open your browser

Streamlit will open automatically, or you can go to:

http://localhost:8501

Functions Summary
api.py
| Function                     | Description                                                         |
| ---------------------------- | ------------------------------------------------------------------- |
| `get(endpoint, params=None)` | Sends HTTP GET request to Frankfurter API and returns JSON response |

frankfurter.py
| Function                                                | Description                                 |
| ------------------------------------------------------- | ------------------------------------------- |
| `get_currencies()`                                      | Fetches all available currency codes        |
| `get_latest_rate(from_currency, to_currency)`           | Fetches the latest conversion rate and date |
| `get_historical_rate(date, from_currency, to_currency)` | Fetches conversion rate on a selected date  |

currency.py
| Function                   | Description                            |
| -------------------------- | -------------------------------------- |
| `format_conversion_text()` | Formats the output exactly as required |

Submission Files:

Submitted a ZIP file named: dsp_at2_25949203.zip

The zip file contains:
app.py
api.py
frankfurter.py
currency.py
README.md




