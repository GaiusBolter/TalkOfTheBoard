from urllib.request import urlopen, urlretrieve, Request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
def validate():

    url = input("Enter the URL: ")
    validurl = urlparse(url)

    while validurl.scheme == "" or validurl.netloc == "" or validurl.path == "":
        url = input("Invalid URL. Enter correct URL: ")
        validurl = urlparse(url)

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #User agent required to avoid 403print("Incorrect URL.")
    html = urlopen(req)
    soup = BeautifulSoup(html, features="html.parser")

    return soup

def download():
    picsoup = validate()
    pics = picsoup.findAll("a", {"class": "fileThumb"})

    for pic in pics:
        filename=pic['href'].split("/")[-1]
        print("Downloading " + filename)
        urlretrieve("http:" + pic['href'], os.path.join(os.getcwd(), filename))
