# app.py
import streamlit as st
from datetime import date

from frankfurter import (
    get_currencies,
    get_latest_rate,
    get_historical_rate,
)
from currency import format_conversion_text

st.set_page_config(page_title="Currency Converter", page_icon="💱")
st.title("Currency Converter")

# -----------------------
# Load currency list
# -----------------------

@st.cache_data
def load_codes():
    return sorted(get_currencies().keys())

currency_codes = load_codes()

# -----------------------
# User Inputs
# -----------------------

amount = st.number_input(
    "Enter amount to convert:",
    min_value=0.0,
    value=100.0,
    step=1.0
)

from_currency = st.selectbox("From Currency:", currency_codes)
to_currency = st.selectbox("To Currency:", currency_codes)

# -----------------------
# Latest Conversion Rate
# -----------------------

if st.button("Get Latest Rate"):
    try:
        rate_date, rate = get_latest_rate(from_currency, to_currency)
        text = format_conversion_text(rate_date, from_currency, to_currency, rate, amount)

        st.subheader("Latest Conversion Rate")
        st.text_area("Result:", text)

    except Exception as e:
        st.error(f"Error fetching latest rate: {e}")

st.write("---")

# -----------------------
# Historical Rate
# -----------------------

hist_date = st.date_input("Select a historical date:", value=date(2023, 1, 1))

if st.button("Conversion Rate"):
    try:
        rate_date, rate = get_historical_rate(hist_date, from_currency, to_currency)
        text = format_conversion_text(rate_date, from_currency, to_currency, rate, amount)

        st.subheader("Historical Conversion Rate")
        st.text_area("Result:", text)

    except Exception as e:
        st.error(f"Error fetching historical rate: {e}")
