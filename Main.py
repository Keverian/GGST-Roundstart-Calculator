import Character, WebScrape

#create a list of character object that includes all characters
def creCharaObjList():
    nameList = WebScrape.getAllName()
    CharacterList = []
    for x in nameList:
        CharacterList.append(Character(x))
    return CharacterList

def main():



