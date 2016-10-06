import urllib2
import os

for page in range(1, 58):
    url = "https://learnpythonthehardway.org/book/ex%s.html" % page
    webpage = urllib2.urlopen(url)
    webpage_content = webpage.read()
    with open(os.path.join('/Users/macbook/PycharmProjects/ProjXMovies/LPTHWhtml/' + str(page) +'.html'), 'wb') as file:
        file.write(webpage_content)
        print "File %d written" %page
        file.close()
print "All done!"