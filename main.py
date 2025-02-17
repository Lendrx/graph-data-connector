import pandas as pd
from moduls import users, devices, security, emails

def fetch_users():
    """Mitarbeiterdaten abrufen und speichern"""
    print("🔍 Mitarbeiterdaten werden abgerufen...")
    user_list = users.get_users()
    df_users = users.save_to_dataframe(user_list)
    df_users.to_csv("Mitarbeiterliste.csv", index=False)
    print(f"✅ {len(df_users)} Mitarbeiter gespeichert in 'Mitarbeiterliste.csv'.")

def fetch_devices():
    """Gerätedaten abrufen und speichern"""
    print("🔍 Geräte werden abgerufen...")
    device_list = devices.get_devices()
    df_devices = pd.DataFrame(device_list)
    df_devices.to_csv("devices.csv", index=False)
    print(f"✅ {len(df_devices)} Geräte gespeichert in 'devices.csv'.")

def fetch_security_alerts():
    """Sicherheitswarnungen abrufen und speichern"""
    print("🔍 Sicherheitswarnungen werden abgerufen...")
    security_alerts = security.get_security_alerts()
    df_security = pd.DataFrame(security_alerts)
    df_security.to_csv("security_alerts.csv", index=False)
    print(f"✅ {len(df_security)} Sicherheitswarnungen gespeichert in 'security_alerts.csv'.")

def fetch_emails():
    """E-Mail-Adressen abrufen und speichern"""
    print("🔍 E-Mail-Adressen werden abgerufen...")
    email_list = emails.get_emails()
    emails.save_emails_to_csv(email_list)
    
def main():
    """Interaktives Menü zur Auswahl der gewünschten Funktion"""
    while True:
        print("\n📌 Wähle eine Funktion:")
        print("1️⃣ Mitarbeiterdaten abrufen")
        print("2️⃣ Geräte abrufen")
        print("3️⃣ Sicherheitswarnungen abrufen")
        print("4️⃣ E-Mail-Adressen abrufen")
        print("5️⃣ Alle Funktionen ausführen")
        print("6️⃣ Beenden")
        
        choice = input("👉 Eingabe: ").strip()
        
        if choice == "1":
            fetch_users()
        elif choice == "2":
            fetch_devices()
        elif choice == "3":
            fetch_security_alerts()
        elif choice == "4":
            fetch_emails()
        elif choice == "5":
            fetch_users()
            fetch_devices()
            fetch_security_alerts()
            fetch_emails()
        elif choice == "6":
            print("👋 Programm beendet.")
            break
        else:
            print("⚠️ Ungültige Eingabe. Bitte erneut versuchen.")

if __name__ == "__main__":
    main()
