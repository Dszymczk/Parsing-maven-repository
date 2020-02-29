import requests
from bs4 import BeautifulSoup

URL = "https://mvnrepository.com/artifact/org.jboss.byteman/byteman/4.0.10"

def printRepoLink(url):
    r = requests.get(url)
    r = r.text
    soup = BeautifulSoup(r, 'html.parser')
    #print(soup.prettify())

    for link in soup.find_all('a'):
        if link.string == "View All":
            print(link.get("href"))

def getJarLink(url):
    r = requests.get(url)
    r = r.text
    jarLink = "none"
    soup = BeautifulSoup(r, 'html.parser')
    for link in soup.find_all(class_="vbtn"):
        if len(link['class']) == 1:
            jarLink = link.get("href")
    return jarLink


def printRepoLinksFromFile(fileName):
    f = open(fileName, "r")
    if f.mode == 'r':
        for line in f:
            #print(line.strip())
            printRepoLink(line.strip())
        f.close()
    else:
        print("Opening file not working")


def printJarLinkFromFile(fileName):
    f = open(fileName, "r")
    if f.mode == 'r':
        for line in f:
            print(line.strip())
            print(getJarLink(line.strip()))
        f.close()
    else:
        print("Opening file not working")
            

if __name__ == "__main__":

    print("Repo Links:")
    printRepoLinksFromFile("links.txt")
    print("\n\n Jar links:")
    printJarLinkFromFile("links.txt")
    


