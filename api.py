# api.py
import requests

BASE_URL = "https://api.frankfurter.app"


def get(endpoint: str, params: dict | None = None) -> dict:
    """
    Generic helper to perform GET requests to the Frankfurter API.

    :param endpoint: API endpoint (e.g. '/latest', '/currencies')
    :param params: Optional query parameters
    :return: JSON response as a Python dict
    """
    url = f"{BASE_URL}{endpoint}"

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()     # Raises an error if API returns 4xx or 5xx
    return response.json()