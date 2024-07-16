# Unsicheres Beispiel
# Passwort und API-Schlüssel sind im Quellcode hardcodiert
password = "123456789abcdef"
api_key = "123456789abcdef"


# Gesichertes Beispiel
# Passwort und API-Schlüssel werden aus den Umgebungsvariablen ausgelesen
import os
password = os.getenv("PASSWORD")
api_key = os.getenv("API_KEY")