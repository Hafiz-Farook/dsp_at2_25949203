# frankfurter.py
from datetime import date
from api import get


def get_currencies():
    """
    Returns a dictionary of available currencies from Frankfurter.
    Example: {"AUD": "Australian Dollar", "USD": "US Dollar"}
    """
    return get("/currencies")


def get_latest_rate(from_currency, to_currency):
    """
    Fetch the latest conversion rate between two currencies.

    Returns:
        (date_string, rate_float)
    """
    # If the currencies are the same, the rate is 1
    if from_currency == to_currency:
        today = date.today().isoformat()
        return today, 1.0

    data = get("/latest", params={"from": from_currency, "to": to_currency})
    rate = data["rates"][to_currency]
    return data["date"], float(rate)


def get_historical_rate(chosen_date, from_currency, to_currency):
    """
    Fetch the historical conversion rate on a selected date.

    chosen_date must be a datetime.date
    """
    date_str = chosen_date.isoformat()

    if from_currency == to_currency:
        return date_str, 1.0

    data = get(f"/{date_str}", params={"from": from_currency, "to": to_currency})
    rate = data["rates"][to_currency]

    # The API may return a different date (nearest business day)
    api_date = data.get("date", date_str)

    return api_date, float(rate)
