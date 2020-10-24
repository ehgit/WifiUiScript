from wifi import Wifi

wificlicker = Wifi()
wificlicker.initialize()
wificlicker.driver.find_element_by_css_selector('#iwlanRadio2G1').click() #wifi 2,5 ghz
wificlicker.driver.find_element_by_css_selector('#iwlanRadio5G1').click() #wifi 5 ghz

wificlicker.end()
