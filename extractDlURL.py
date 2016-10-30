from bs4 import BeautifulSoup
from selenium import webdriver
import time
import extractSeasonURL

# requires chromedriver
path_to_chromedriver = './chromedriver'
dlFile = 'breakingBadS2dl.txt'
listOfLinks = []

def extractURL(url):
    browser = webdriver.Chrome(path_to_chromedriver)
    browser.get(url)
    time.sleep(5)

    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')
    videoUrlChunk =  soup.body.find(id="player-embed")
    dlUrl = videoUrlChunk.find(id='m-dl-button')

    print "----\n", dlUrl.get('href')

    listOfLinks.append(dlUrl.get('href').encode('ascii', 'ignore'))

    print "--Episode Download Link Secured--"

    time.sleep(5)
    browser.quit()

with open(extractSeasonURL.episodeFile, 'r') as file:
    data = [line.strip() for line in file]
    print data, "\n-----"
    for url in data:
        extractURL(url)

    print "--All Episode DL Secured--"
    f = open(dlFile, 'w')
    for link in listOfLinks:
        f.write(str(link + "\n"))
    f.close()