import requests
from . import auth

GRAPH_API_URL = "https://graph.microsoft.com/v1.0/devices"

def get_devices():
    """Ruft alle mit Azure AD verbundenen Geräte ab"""
    access_token = auth.get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(GRAPH_API_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("value", [])
    else:
        raise Exception(f"Fehler beim Abrufen der Geräte: {response.json()}")

