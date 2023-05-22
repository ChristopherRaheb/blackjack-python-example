from urllib import request, parse
import json
from objects import Category, Area, Meal, Instructions

def getCategories():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for categoryData in data['meals']:
            category = Category(categoryData['strCategory'])
            categories.append(category)

    except(ValueError, KeyError, TypeError):
        return None

    return categories

def getMealsByCategory(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for mealData in data['meals']:
            meal = Meal(mealData['strMeal'])
            meals.append(meal)

    except(ValueError, KeyError, TypeError):
        return None

    return meals

def getMealByName(name):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + name
    url = url.replace(" ", "%20")
    f = request.urlopen(url)
    ingredients = []
    measures = []

    try:
        data = json.loads(f.read().decode('utf-8'))

        for mealData in data['meals']:
            name = mealData['strMeal']
            instructions = mealData['strInstructions']
            i = 1

            while i <= 20:
                ingredientNum = "strIngredient" + str(i)
                newIngredient = mealData[ingredientNum]
                if newIngredient != None:
                    ingredients.append(newIngredient)

                measureNum = "strMeasure" + str(i)
                newMeasure = mealData[measureNum]
                if newMeasure != None:
                    measures.append(newMeasure)
                i += 1

        mealInstructions = Instructions(name, instructions, ingredients, measures)

    except(ValueError, KeyError, TypeError):
        return None

    return mealInstructions

def getRandomMeal():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    f = request.urlopen(url)
    ingredients = []
    measures = []

    try:
        data = json.loads(f.read().decode('utf-8'))

        for mealData in data['meals']:
            name = mealData['strMeal']
            instructions = mealData['strInstructions']
            i = 1

            while i <= 20:
                ingredientNum = "strIngredient" + str(i)
                newIngredient = mealData[ingredientNum]
                if newIngredient != None:
                    ingredients.append(newIngredient)

                measureNum = "strMeasure" + str(i)
                newMeasure = mealData[measureNum]
                if newMeasure != None:
                    measures.append(newMeasure)
                i += 1

        mealInstructions = Instructions(name, instructions, ingredients, measures)

    except(ValueError, KeyError, TypeError):
        return None

    return mealInstructions

def getAreas():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for areaData in data['meals']:
            area = Area(areaData['strArea'])
            areas.append(area)

    except(ValueError, KeyError, TypeError):
        return None

    return areas

def getMealsByArea(area):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + area
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for mealData in data['meals']:
            meal = Meal(mealData['strMeal'])
            meals.append(meal)

    except(ValueError, KeyError, TypeError):
        return None

    return meals