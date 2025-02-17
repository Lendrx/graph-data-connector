import requests
import pandas as pd
from . import auth

GRAPH_API_URL = "https://graph.microsoft.com/v1.0/users?$select=displayName,mail,jobTitle"

def get_users():
    """Ruft alle Mitarbeiterdaten aus Azure AD ab"""
    access_token = auth.get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    users = []
    url = GRAPH_API_URL

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            users.extend(data.get("value", []))
            url = data.get("@odata.nextLink", None)  # Falls Paging notwendig ist
        else:
            raise Exception(f"Fehler beim Abrufen der Benutzerdaten: {response.json()}")

    return users

def save_to_dataframe(users):
    """Speichert die Daten in einen Pandas DataFrame"""
    df = pd.DataFrame(users, columns=["displayName", "mail", "jobTitle"])
    df.rename(columns={"displayName": "Name", "mail": "E-Mail", "jobTitle": "Position"}, inplace=True)
    return df
