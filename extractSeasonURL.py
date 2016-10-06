# probably need to learn selenium and wait for the other libaries to update
# phantomJS, Chrome, Firefox and dryscrape
from bs4 import BeautifulSoup
from selenium import webdriver
import time


url = "http://xmovies8.tv/movie/breaking-bad-season-2-2009-160922/watching.html?episode_id=16320"
episodeFile = 'breakingBadS2url.txt'

# browser = webdriver.PhantomJS(executable_path='')
path_to_chromedriver = '/Users/macbook/Desktop/projectUniInfo/chromedriver'

browser = webdriver.Chrome(path_to_chromedriver)


# stuff to run always here such as class/def
def main():

     browser.get(url)
     time.sleep(5)

     html = browser.page_source

     pageUrls = []

     soup = BeautifulSoup(html, 'html.parser')

     urlBlock = soup.body.find('div', "ep_link full")

     for x in urlBlock.findAll('a'):
          pageUrls.append("http:" + x.get('href').encode('ascii', 'ignore'))

     print pageUrls
     f = open(episodeFile, 'w')
     for link in pageUrls:
          f.write(str(link) + "\n")
     f.close()

     print "--All Episode Pages Secured--"

     time.sleep(5)
     browser.quit()

if __name__ == "__main__":
     # stuff only to run when not called via 'import' here
     main()