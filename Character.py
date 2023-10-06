from bs4 import BeautifulSoup
import WebScrape
#character class that stores: string name, list normalMoves, list specialMoves
class Character:
    def __init__(self, name):
        self.name = name
        self.moves = WebScrape.getMoves(self.name)

    def printMoves(self):
        for x in self.moves:
            print(x)

Nagoriyuki = Character("Nagoriyuki")
Nagoriyuki.printMoves()





