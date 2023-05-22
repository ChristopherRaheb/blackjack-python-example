import requests
import textwrap

def showTitle():
    print("My Recipe Program\n")

def showMenu():
    print("COMMAND MENU")
    print("1 - List all categories")
    print("2 - List all meals for categories")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - Search Meals by Area")
    print("7 - Menu")
    print("0 - Exit the application\n")

def listCategories():
    categories = requests.getCategories()

    if categories is None:
        print("Technical difficulties, please try again later")
    else:
        print("\nCATEGORIES")
        for i in range(len(categories)):
            category = categories[i]
            print(" " + category.getName())
        print()

def listMeals(title, meals):
    if meals is None:
        print("Technical difficulties, please try again later")
    else:
        print()
        print(title.upper(), "MEALS")
        for i in range(len(meals)):
            meal = meals[i]
            print(" " + meal.getName())
        print()

def listMealsByCategory():
    lookupCategory = input("Enter a category: ")

    categories = requests.getCategories()
    found = False

    if categories is None:
        print("Technical difficulties, please try again later")
    else:
        for i in range(len(categories)):
            category = categories[i]
            if category.getName().lower() == lookupCategory.lower():
                found = True
                break

    if found:
        meals = requests.getMealsByCategory(lookupCategory)
        listMeals(lookupCategory, meals)
    else:
        print("Invalid Category, please try again.")

def printInstructions(instructions):
    print("\nRecipe:  " + instructions.getName())
    print("\nInstructions:\n")
    wrapper = textwrap.TextWrapper(width=80)
    instructionsList = wrapper.wrap(text=instructions.getInstructions())
    for line in instructionsList:
        print(line)
    print("\nIngredients:")
    ingredients = instructions.getIngredients()
    measures = instructions.getMeasures()
    detailedIngredients = []
    for i in range(len(ingredients)):
        detailedIngredients.append(measures[i] + " " + ingredients[i])
        if detailedIngredients[i] == None:
            detailedIngredients.pop(i)
    i = 1
    longestWord = ""
    for item in detailedIngredients:
        if len(longestWord) < len(item):
            longestWord = item
    dashLength = len(longestWord) * 3
    if dashLength < 80:
        dashLength = 80
    print("-" * dashLength)
    for item in detailedIngredients:
        columnLength = len(longestWord) - len(item) + 1
        if len(item) + 1 < 27:
            columnLength = 27 - len(item)
        print(item + (" " * columnLength), end="")
        if i % 3 == 0:
            print()
        i += 1
    print()

def searchMealByName():
    lookupName = input("Enter Meal Name: ")

    instructions = requests.getMealByName(lookupName)
    if instructions != None:
        printInstructions(instructions)
    else:
        print("Invalid name, please try again.")

def getRandomMeal():
    instructions = requests.getRandomMeal()
    printInstructions(instructions)

def listAreas():
    areas = requests.getAreas()

    if areas is None:
        print("Technical difficulties, please try again later")
    else:
        print("\nAREAS:")
        for i in range(len(areas)):
            area = areas[i]
            print(" " + area.getName())
        print()

def listMealsByArea():
    lookupArea = input("Enter an Area: ")

    areas = requests.getAreas()
    found = False

    if areas is None:
        print("Technical difficulties, please try again later")
    else:
        for i in range(len(areas)):
            area = areas[i]
            if area.getName().lower() == lookupArea.lower():
                found = True
                break

    if found:
        meals = requests.getMealsByArea(lookupArea)
        listMeals(lookupArea, meals)
    else:
        print("Invalid Area, please try again.")

def main():
    showTitle()
    showMenu()

    while True:
        command = input("What would you like to do? ")
        if command == "1":
            listCategories()
        elif command == "2":
            listMealsByCategory()
        elif command == "3":
            searchMealByName()
        elif command == "4":
            getRandomMeal()
        elif command == "5":
            listAreas()
        elif command == "6":
            listMealsByArea()
        elif command == "7":
            showMenu()
        elif command == "0":
            print("Thank you for dining with us!")
            break

if __name__ == "__main__":
    main()