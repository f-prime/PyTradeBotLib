from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.loginURL = "http://store.steampowered.com/login/"
        self.driver = webdriver.Firefox()

    def login(self):
        print "Logging in, make sure SteamGuard is disabled"
        self.driver.get(self.loginURL)
        username = self.driver.find_element_by_id("input_username")
        username.send_keys(self.username)
        password = self.driver.find_element_by_id("input_password")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        print "Logged in! I didn't check and make sure the username and password was correct, so make sure they are."
        raw_input("Press enter")
    
    def trade(self):
        self.driver.get("http://steamcommunity.com/profiles/76561198104150539")

