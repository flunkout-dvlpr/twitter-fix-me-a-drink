import requests
import json
import yaml
import random
import webbrowser
import pprint

pp = pprint.PrettyPrinter(indent=2)

def getAvailableIngridients():
  availableIngridients = "https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list"
  try: 
    data = requests.get(availableIngridients)
    data_json = data.json()
    data_dict = yaml.safe_load(json.dumps(data_json))
  except:
    return {}
  if data_dict:
    availableIngirdients = [ingridient for item in data_dict['drinks'] for ingridient in item.values()] 
    return availableIngirdients


def getByIngredient(ingredients):
  drinksByIngredient = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={}".format(ingredients[0])
  try: 
    data = requests.get(drinksByIngredient)
    data_json = data.json()
    data_dict = yaml.safe_load(json.dumps(data_json))
  except:
    return {}

  if data_dict:
    drinks = data_dict['drinks']
    for drink in drinks:
      drink['drinkName'] = drink.pop('strDrink')
      drink['drinkPic']  = drink.pop('strDrinkThumb')
      drink['drinkID']   = drink.pop('idDrink')
    
    return drinks 

def getDrinkDetails(drinkID):
  drinkDetails = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(drinkID) 
  try:  
    data = requests.get(drinkDetails)
    data_json = data.json()
    data_dict = yaml.safe_load(json.dumps(data_json))
  except:
    return {}

  if data_dict:
    details = data_dict['drinks'][0]
    recipe = {'instructions': {},
              'ingredients' : [] 
             }

    for name, value in details.items():
      if 'Ingredient' in name and value:
        ingredient  = details[name]
        measurement = details[name.replace('Ingredient','Measure')]
        measurement = measurement if measurement else "To Liking"
        recipe['ingredients'].append([ingredient, measurement])
      recipe['instructions']['text'] = details['strInstructions']
      recipe['instructions']['charCount'] = len(details['strInstructions'])
    
    return recipe

def getTweetDrink(ingredients):

  drinks = getByIngredient(ingredients)
  numberOfDrinks = len(drinks)
  if numberOfDrinks > 0:
    randomDrink = random.randint(0, (numberOfDrinks-1))

    drinkName   = drinks[randomDrink]['drinkName']
    drinkID     = drinks[randomDrink]['drinkID']
    drinkRecipe =  getDrinkDetails(drinkID)

    print(drinkName)
    print(drinkRecipe)



# availableIngridients = getAvailableIngridients()
# print(availableIngridients)
ingredients = ['orange']
getTweetDrink(ingredients)





