import time
import configparser

from config import Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Wifi:     
    def initialize(self):
        self.options = Options()
        self.setConfiguration()		
        self.addArguments(['--window-size=1024,768', '--no-sandbox', 'disable-infobars', "--disable-extensions", '--headless'])
        self.driver = webdriver.Chrome(configuration.webdriverPath, options=self.options )
        self.driver.get(configuration.url)
        self.wait()
        self.confirmPw()
        self.wait()
        self.clickElements(['c_mu05', 'c_mu06', 'c_mu07']) # Erweiterte Einstellungen, Wlan, Wifi-Signal
        self.wait()

    def addArguments(self, arguments):
        for argument in arguments:
            self.options.add_argument(argument)

    def clickElements(self, elements):
        for element in elements:
            self.driver.find_element_by_id(element).click()

    def confirmPw(self):        
        search_box = self.driver.find_element_by_name('loginPassword')
        search_box.send_keys(configuration.wifipwd)
        search_box.send_keys(Keys.RETURN)

    def end(self):
        self.driver.find_element_by_id('c_02').click() # aenderungen uebernehmen
        self.wait()
        self.driver.find_element_by_id('c_mu30').click() #abmelden
        self.wait()
        self.driver.quit()

    def wait(self):
        time.sleep(7)
    
    def setConfiguration(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        configs = config['config']
        global configuration 
        configuration = Config(configs['URL'], configs['Connectpwd'], configs['Webdriverpath'])