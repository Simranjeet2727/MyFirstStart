from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Initializing Brave browser options
brave_options = Options()
brave_options.binary_location = '/Applications/Brave Browser.app'

# Initializing webdriver with Brave options
driver = webdriver.Chrome(options=brave_options)

# Open URL and maximize window
driver.get('https://www.amazon.in/')
driver.maximize_window()
