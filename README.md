# WifiUiScript
Script zu Aktivierung / Deaktivierung des Wlans in der Oberfläche einer Connect Box


Hier könnte beispielsweise ein Raspberry Pi die Ausführung mittels eines Cron-Jobs übernehmen.
Prerequisites für eine erfolgreiche Ausführung:
- Python installiert
- Webdriver installiert (https://chromedriver.chromium.org/downloads)
- Verbindung über LAN


In der config.ini müssen folgende Angaben gemacht werden:

- URL = Hier die lokale IP des Routers (zB. http://192.168.0.1)
- Connectpwd = Das Passwort der Connect Box
- Webdriverpath = Der Pfad zum Webdriver von Chrome 

Zur Aktivierung das activate_wifi.py Script ausführen. Zur Deaktivierung das deactivate_wifi.py Script ausführen.
