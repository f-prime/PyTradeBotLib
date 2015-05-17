from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

class Bot:
    def __init__(self, username, password, steamid, debug=False):
        self.username = username
        self.password = password
        self.steamid = steamid
        self.loginURL = "http://store.steampowered.com/login/"
        if debug:
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.PhantomJS()
            self.driver.set_window_size(0, 0)

    def login(self):
        print "Logging in, make sure SteamGuard is disabled"
        self.driver.get(self.loginURL)
        username = self.driver.find_element_by_id("input_username")
        username.send_keys(self.username)
        password = self.driver.find_element_by_id("input_password")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        print "Logged in! I didn't check and make sure the username and password was correct, so make sure they are."
    
    def sendTrade(self, url):
        self.driver.get(url)
        print "Trade request sent"

    
    def incomingTrade(self):
        self.driver.get("http://steamcommunity.com/profiles/{}/tradeoffers/".format(self.steamid))
        tradeUrl = re.findall("javascript:ShowTradeOffer(.*);", self.driver.page_source)[0].replace("(", '').replace("'", '').replace(")",'').replace(" ", '')
        self.driver.get("https://steamcommunity.com/tradeoffer/{}/".format(tradeUrl))
        self.driver.find_element_by_id("you_notready").click() 
        self.driver.find_element_by_id("trade_confirmbtn").click()
