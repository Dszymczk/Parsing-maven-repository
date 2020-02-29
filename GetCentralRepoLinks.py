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
            print(line)
            print(getJarLink(line))
        f.close()
    else:
        print("Opening file not working")
            

if __name__ == "__main__":
    #printRepoLinksFromFile("links.txt")
    #printJarLink("https://mvnrepository.com/artifact/com.sun.istack/istack-commons/3.0.8")
    #printJarLink("https://mvnrepository.com/artifact/org.glassfish.jaxb/jaxb-runtime/2.3.2")
    #printJarLinkFromFile("links.txt")
    print(getJarLink("https://repo1.maven.org/maven2/org/glassfish/jaxb/jaxb-runtime/2.3.2/jaxb-runtime-2.3.2.jar"))
    

    #print("\nJar link for JAXB Runtime » 2.3.2: ")
    #printJarLink("https://mvnrepository.com/artifact/org.glassfish.jaxb/jaxb-runtime/2.3.2")

    
