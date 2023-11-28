from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from InstaFollower import *


bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()


