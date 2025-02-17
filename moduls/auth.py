import os
from msal import ConfidentialClientApplication
from dotenv import load_dotenv

# 🌍 Umgebungsvariablen laden
load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

def get_access_token():
    """Holt ein Zugriffstoken für Microsoft Graph API"""
    app = ConfidentialClientApplication(CLIENT_ID, CLIENT_SECRET, AUTHORITY)
    token_response = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    
    if "access_token" in token_response:
        return token_response["access_token"]
    else:
        raise Exception("Fehler beim Abrufen des Tokens:", token_response)
