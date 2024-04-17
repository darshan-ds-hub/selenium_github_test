import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



main_url = 'https://www.google.com/'


options = Options()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get(main_url)

time.sleep(10)