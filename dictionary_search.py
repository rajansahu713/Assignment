import requests
import json

class Dic_search:
    # intializing class constructor 
    def __init__(self, word):  
        self.word = word  

    # Methode to display the meaning of a word    
    def result(self):
        word=self.word
        req = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word)
        t=req.json()
        meanings = t[0]["meanings"]

        for i in range(0, len(meanings)):
            print(f'Meaning {i + 1} :')
            print(f'{word.title()}. {meanings[i]["partOfSpeech"].title()}. {meanings[i]["definitions"][0]["definition"].title()}.\n')


if __name__ == "__main__":
    # Taking a word from user
    word=input("Word? ")
    # Calling constructor of the class
    S1 = Dic_search(word)  
    # showing result      
    S1.result() 