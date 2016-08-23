###############################################################################
# The following is BeautifulSoup and in Python2
###############################################################################
# from bs4 import BeautifulSoup
# import urllib2
#
# seed_url = "https://www.udacity.com/cs101x/index.html"
# content = urllib2.urlopen(url).read()
# soup = BeautifulSoup(content)
# print(soup.prettify())

###############################################################################
# The following is BeautifulSoup and modified for Python3
###############################################################################
from bs4 import BeautifulSoup
from urllib.request import urlopen

seed_url = "https://www.udacity.com/cs101x/index.html"
httpresp = urlopen(seed_url)
soup = BeautifulSoup(httpresp)
soup = BeautifulSoup(httpresp, "html.parser")
print(soup.prettify())


###############################################################################

links = []

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if (start_link < 0):
        # print(None)
        # print(0)
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        # print(url)
        # print(end_quote)
        return url, end_quote

def get_all_links(page):
    while True:
        url, end_quote = get_next_target(page)
        if url:
            links.append(url)
            page = page[end_quote:]
        else:
            break

def crawl_web(seed):
    to_crawl = [seed]
    crawled = []
    while to_crawl:


# get_next_target(page)
