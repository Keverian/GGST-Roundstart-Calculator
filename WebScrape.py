from bs4 import BeautifulSoup

import requests

#scrape all character name from dustloop
def getAllName():
    characterList = []
    #load dustloop main page
    url = "https://www.dustloop.com/w/GGST"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    nameSection = soup.find('div', class_='add-hover-effect')
    nameSection = nameSection.find('p')
    nameList = nameSection.find_all('a')

    for x in nameList:
        characterList.append(x['title'])

    return characterList




def getMoves(name):
    moves = []
    url = "https://www.dustloop.com/w/GGST/" + name
    #create soup
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")


    #get normal moves
    normalTags = soup.find('ul', id="toc-Normal_Moves-sublist")
    allNormalTags = normalTags.find_all("li")
    for x in allNormalTags:
        name2 = x.find('a')
        name3 = name2.find('div', class_="citizen-toc__text")
        name4 = name3.find_all('span')
        moves.append(name4[1].text)

    #get special moves
    tags = soup.find('section', class_='section-collapsible', id='section-collapsible-4')
    allSpecialTags = tags.find_all('span', class_='input-badge')
    for x in allSpecialTags:
        moves.append(x.find('span').text)

    return moves


"""
def getSpecial(name, specialMoves, url):
    #specialMoves = []
    tags = soup.find('section', class_='section-collapsible', id='section-collapsible-4')
    allSpecialTags = tags.find_all('span', class_='input-badge')
    for x in allSpecialTags:
        specialMoves.append(x.find('span').text)
    print(specialMoves)


def getNormal(name, normalMoves, url):
    
    result = requests.get(url)
    
    soup = BeautifulSoup(result.text, "html.parser")
    normalTags = soup.find('ul', id="toc-Normal_Moves-sublist")

    # scrape all normal moves of a character into a string list
    allNormalTags = normalTags.find_all("li")
    #normalMoves = []
    for x in allNormalTags:
        name2 = x.find('a')
        name3 = name2.find('div', class_="citizen-toc__text")
        name4 = name3.find_all('span')
        normalMoves.append(name4[1].text)
"""
