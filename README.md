# WifiUiScript
English Version

Script to activate / deactivate the Wifi in the web-userinterface of a Connect Box.

For this purpose you could use a raspberry pi to automatically manage activation with a cron-job.
Prerequisites for your success:
- Python installed
- Webdriver installed: (https://chromedriver.chromium.org/downloads)
- Connection via LAN

Within the config.ini you need to add the following information:

_ URL = The local IP Adress of your Router (e.g. http://192.168.0.1)
- Connectpwd = The Password for your Connect Box
- Webdriverpath = Path of your Webdriver for Chrome

German Version

Script zur Aktivierung / Deaktivierung des Wlans in der Oberfläche einer Connect Box


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

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?hosted_button_id=PH92ZYXQ94DA2)
