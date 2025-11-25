import random

class Data():

    numShuffles = 10
    data = []

    def __init__(self):
        self.BuildData()
        self.Shuffle()
        self.BuildDef()

    def BuildData(self):
        self.data.append(Word("abberation", "n", "a deviation from the standard; not typical"))
        self.data.append(Word("access", "n", "a means of approach or admittance"))
        self.data.append(Word("accord", "n", "an agreement"))
        self.data.append(Word("adage", "n", "wise proverb or saying"))
        self.data.append(Word("adversary", "n", "enemy, opponent"))
        self.data.append(Word("advocate", "n", "one who speaks in favor of or on behalf of another"))
        self.data.append(Word("affluence", "n", "wealth or abundance"))

    def Shuffle(self):
        for _ in range (0, self.numShuffles):
            random.shuffle(self.data)

    def BuildDef(self):
        for i in range(0, len(self.data)):
            defListLength = len(self.data[i].DefList)
            randCorrectIndex = random.randrange(defListLength)
            self.data[i].DefList[randCorrectIndex] = Definition(self.data[i].Def, True)
            for j in range(0, defListLength):
                if self.data[i].DefList[j] == None:
                    choice: Word = random.choice(self.data)
                    while choice.Def in self.data[i].DefList:
                        choice = random.choice(self.data)
                    self.data[i].DefList[j] = Definition(choice.Def, False)
                else:
                    continue

    def GetData(self):
        return self.data
    

class Word():

    Name = ""
    Type = ""
    Def = ""

    # list of definitions of type [def:str, correct:bool]
    DefList = None

    def __init__(self, Name: str, Type: str, Def: str):
        self.Name = Name
        self.Type = Type
        self.Def = Def
        self.DefList = [ None ] * 4

class Definition():
    Def = ""
    Correct = False

    def __init__(self, Def: str, Correct: bool):
        self.Def = Def
        self.Correct = Correct

    def __eq__(self, value):
        return self.Def == value