from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# requires chromedriver
path_to_chromedriver = './chromedriver'

options = Options()
options.add_argument('--proxy-server=97.77.104.22:80')
browser = webdriver.Chrome(path_to_chromedriver)
browser.get("http://sss.gov")
