import requests

def forward_request_to_modelslab(url: str, headers: dict, payload: dict):
    """
    Forwards the request to the given full URL with the provided headers and JSON payload.
    """
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()
