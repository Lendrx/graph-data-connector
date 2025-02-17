Hier ist die überarbeitete **README.md** mit zusätzlichen Details zu den benötigten API-Berechtigungen und einer klareren Struktur:  

---

# **Microsoft Graph - Data Collector**  

Dieses **Python-Skript** nutzt die **Microsoft Graph API**, um wichtige Unternehmensdaten aus **Microsoft Entra ID (Azure AD)** abzurufen, darunter:  

✅ **Mitarbeiterdaten** – Name, E-Mail, Position  
✅ **Geräteinformationen** – Mit Azure AD verbundene Geräte  
✅ **Sicherheitswarnungen** – Bedrohungen aus Microsoft Defender  
✅ **E-Mail-Adressen** – Unternehmensweite E-Mail-Adressen  

---

## **🚀 Installation**  

### **1️⃣ Repository klonen**  
```bash
git clone https://github.com/DEIN_USERNAME/employee-data-collector.git
cd employee-data-collector
```

### **2️⃣ Virtuelle Umgebung erstellen & aktivieren**  
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### **3️⃣ Abhängigkeiten installieren**  
```bash
pip install -r requirements.txt
```

---

## **⚙️ Einrichtung**  

### **1️⃣ .env-Datei erstellen**  
Erstelle im Hauptverzeichnis eine **`.env`**-Datei mit folgenden Inhalten:  
```ini
TENANT_ID=DEIN_TENANT_ID
CLIENT_ID=DEIN_CLIENT_ID
CLIENT_SECRET=DEIN_CLIENT_SECRET
```
> **🔴 Wichtig:** Teile diese Datei **nicht öffentlich**, da sie sensible Zugangsdaten enthält!  

### **2️⃣ Microsoft Entra (Azure AD) API-Berechtigungen setzen**  
Damit das Skript auf die Microsoft Graph API zugreifen kann, müssen in **Microsoft Entra ID (Azure AD)** die richtigen Berechtigungen gesetzt werden.  

#### **🔹 Erforderliche API-Berechtigungen:**  
| API-Berechtigung            | Typ              | Beschreibung |
|-----------------------------|------------------|-------------|
| `User.Read.All`             | **Application**  | Alle Benutzerprofile abrufen |
| `Device.Read.All`           | **Application**  | Alle Geräte abrufen |
| `SecurityEvents.Read.All`   | **Application**  | Zugriff auf Sicherheitswarnungen (Defender) |
| `Mail.Read`                 | **Delegated**    | Zugriff auf E-Mail-Postfächer |

#### **🔹 Admin-Zustimmung erteilen:**  
Nachdem die Berechtigungen hinzugefügt wurden, muss ein **Administrator** sie genehmigen:  
1. Gehe in **Azure Portal** → **App-Registrierungen**  
2. Wähle deine App aus  
3. Klicke auf **„API-Berechtigungen“**  
4. Klicke auf **„Admin-Zustimmung für … erteilen“**  

---

## **📌 Nutzung**  
Das Skript bietet ein interaktives Menü zur Auswahl der Funktionen.  
Starte das Programm mit:  
```bash
python main.py
```
Wähle eine der folgenden Optionen:  
```
📌 Wähle eine Funktion:
1️⃣ Mitarbeiterdaten abrufen
2️⃣ Geräte abrufen
3️⃣ Sicherheitswarnungen abrufen
4️⃣ E-Mail-Adressen abrufen
5️⃣ Alle Funktionen ausführen
6️⃣ Beenden
👉 Eingabe:
```

---

## **🛠 Fehlerbehebung**  
Falls `SecurityEvents.Read.All` oder andere API-Aufrufe fehlschlagen:  
1. Überprüfe die **API-Berechtigungen** in **Azure AD**  
2. Stelle sicher, dass die **Admin-Zustimmung** erteilt wurde  
3. Fordere ein neues Access-Token mit `auth.get_access_token()` an  
4. Prüfe die Berechtigungen im Token über **[jwt.ms](https://jwt.ms)**  