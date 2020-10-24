class Config:
    url = ''
    wifipwd = ''
    webdriverPath = ""

    def __init__(self, url, wifipwd, webdriverPath):
        self.url = url
        self.wifipwd = wifipwd
        self.webdriverPath = webdriverPath