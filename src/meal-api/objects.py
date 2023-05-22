class Category:
    def __init__(self, category):
        self.__category = category

    def getName(self):
        return self.__category

class Area:
    def __init__(self, category):
        self.__category = category

    def getName(self):
        return self.__category

class Meal:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Instructions:
    def __init__(self, name, instructions, ingredients, measures):
        self.__name = name
        self.__instructions = instructions
        self.__ingredients = ingredients
        self.__measures = measures

    def getName(self):
        return self.__name

    def getInstructions(self):
        return self.__instructions

    def getIngredients(self):
        return self.__ingredients

    def getMeasures(self):
        return self.__measures