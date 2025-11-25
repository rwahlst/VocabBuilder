# AFOQT Vocab Builder by Axel Wahlstrom
# Usage: python main.py

from data import Data, Word, Definition
import os

class Main():

    d = None
    wordList = None

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
        if char == "a":
            return 0
        if char == "b":
            return 1
        if char == "c":
            return 2
        if char == "d":
            return 3
        return 0
        
    def indexToalpha(self, n: int):
        if n == 0:
            return "a"
        if n == 1:
            return "b"
        if n == 2:
            return "c"
        if n == 3:
            return "d"
        return "a"

    def Begin(self):
        counter = 1
        print("Welcome to VocabBuilder.py")
        print("A Python Notecard System by Axel Wahlstrom")
        print("Select the best definition for the given word: a, b, c, or d")
        print("===========================================")
        while len(self.wordList) > 0:
            curr: Word = self.wordList.pop(0)
            print(str(counter) + ". " + curr.Type + " | " + curr.Name)
            print()
            for i in range(0, len(curr.DefList)):
                print(str(self.indexToalpha(i)) + ": " + curr.DefList[i].Def)
            
            uIn = input("> ")
            index = self.alphaToindex(uIn)
            result: Definition = curr.DefList[index]

            if result.Correct:
                print("Correct!")
            else:
                print("Incorrect!")
                print(curr.Name + " - " + curr.Def)
                self.wordList.append(curr)
            
            counter = counter + 1

            print("===========================================")
        
        print("Well Done! Scoring coming soon!")
        print("Exiting application... Goodbye!")






m = Main()