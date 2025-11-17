# api.py
import requests

BASE_URL = "https://api.frankfurter.app"


def get(endpoint: str, params: dict | None = None) -> dict:
    """
    Generic helper to call the Frankfurter API.

    :param endpoint: Endpoint starting with '/' (e.g. '/latest')
    :param params: Optional query parameters
    :return: Parsed JSON response as dict
    :raises: requests.HTTPError for bad responses
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()
