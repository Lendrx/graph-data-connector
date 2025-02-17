import requests
import pandas as pd
from . import auth

GRAPH_API_URL = "https://graph.microsoft.com/v1.0/users?$select=mail"

def get_emails():
    """Ruft alle E-Mail-Adressen der Benutzer im Unternehmen ab"""
    access_token = auth.get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    emails = []
    url = GRAPH_API_URL

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            emails.extend(user["mail"] for user in data.get("value", []) if user.get("mail"))
            url = data.get("@odata.nextLink", None)  # Falls Paging notwendig ist
        else:
            raise Exception(f"Fehler beim Abrufen der E-Mail-Adressen: {response.json()}")

    return emails

def save_emails_to_csv(email_list, filename="emails.csv"):
    """Speichert die E-Mail-Adressen in eine CSV-Datei"""
    df = pd.DataFrame(email_list, columns=["E-Mail"])
    df.to_csv(filename, index=False)
    print(f"✅ {len(email_list)} E-Mail-Adressen gespeichert in '{filename}'.")
