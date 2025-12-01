# AFOQT Vocab Builder by Axel Wahlstrom
# Usage: python main.py

from data import Data, Word, Definition
import time
import os

class Main():

    d = None
    wordList = None
    APP_VERSION = "1.0.4"

    def ClearTerminal(self):
        # 'nt' for Windows, 'posix' for Linux/macOS
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def __init__(self):
        self.ClearTerminal()
        self.d = Data()
        self.wordList = self.d.GetData()
        self.Begin()

    def alphaToindex(self, char: str):
        if char.lower() == "a":
            return 0
        if char.lower() == "b":
            return 1
        if char.lower() == "c":
            return 2
        if char.lower() == "d":
            return 3
        return -1
        
    def indexToalpha(self, n: int):
        if n == 0:
            return "a"
        if n == 1:
            return "b"
        if n == 2:
            return "c"
        if n == 3:
            return "d"
        return "z"
    
    def GetTypeString(self, string: str):
        if string == "n":
            return "noun"
        elif string == "a":
            return "adjective"
        elif string == "v":
            return "verb"
        elif string == "pn":
            return "pronoun"
        elif string == "pv":
            return "proverb"
        elif string == "av":
            return "adverb"
        else:
            return "unknown"
    
    def PrintWelcome(self, listLen: int, remainingLen: int):
        print("Welcome to VocabBuilder.py")
        print("A Python Notecard System")
        print("v." + self.APP_VERSION)
        print("Select the best definition for the given word: a, b, c, or d")
        print("===========================================")
        print("Total words: " + str(listLen))
        print("Words remaining: " + str(remainingLen))
        print("===========================================")

    def Begin(self):
        counter = 1
        label = 1
        originalLen = len(self.wordList)
        numCorrect = 0
        sleepTime = 0

        while len(self.wordList) > 0:
            self.PrintWelcome(originalLen, len(self.wordList))
            curr: Word = self.wordList.pop(0)
            print(str(label) + ". " + self.GetTypeString(curr.Type) + " | " + curr.Name)
            print()
            for i in range(0, len(curr.DefList)):
                print(str(self.indexToalpha(i)) + ": " + curr.DefList[i].Def)
            
            uIn = input("> ")
            index = self.alphaToindex(uIn)
            result: Definition = None
            
            while index == -1:
                uIn = input("> ")
                index = self.alphaToindex(uIn)
                
            result = curr.DefList[index]

            if result != None and result.Correct:
                print("Correct!")
                numCorrect = numCorrect + 1
                sleepTime = 1
            else:
                print("Incorrect!")
                print(curr.Name + " - " + curr.Def)
                curr.Redo = True
                self.wordList.append(curr)
                sleepTime = 2.5
            
            if not curr.Redo:
                counter = counter + 1
            label = label + 1

            print("===========================================")
            time.sleep(sleepTime)
            self.ClearTerminal()
        
        score = numCorrect / originalLen
        pct = str(score * 100) + "%"
        print("Well Done!")
        print("Score: " + pct)
        print("Exiting application... Goodbye!")


m = Main()