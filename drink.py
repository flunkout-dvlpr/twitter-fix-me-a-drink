import requests
import json
import yaml
import random

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


def getDrinksByIngredient(ingredient):
  drinksByIngredient = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={}".format(ingredient)
  try: 
    data = requests.get(drinksByIngredient)
    data_json = data.json()
    data_dict = yaml.safe_load(json.dumps(data_json))
  except:
    return {}

  if data_dict:
    drinks = data_dict['drinks']
    for drink in drinks:
      drink['name']     = drink.pop('strDrink')
      drink['image']    = drink.pop('strDrinkThumb')
      drink['drinkID']  = drink.pop('idDrink')
    
    return drinks 

def getRecipe(drinkID):
  drinkDetails = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(drinkID) 
  try:  
    data = requests.get(drinkDetails)
    data_json = data.json()
    data_dict = yaml.safe_load(json.dumps(data_json))
  except:
    return {}

  if data_dict:
    details = data_dict['drinks'][0]
    recipe = {'instructions': '',
              'ingredients' : [] 
             }

    for name, value in details.items():
      if 'Ingredient' in name and value:
        ingredient  = details[name]
        measurement = details[name.replace('Ingredient','Measure')]
        measurement = measurement if measurement else "To Liking"
        recipe['ingredients'].append("* {} - {}".format(ingredient,measurement))
      recipe['instructions'] = details['strInstructions']
    
    return recipe

def downloadDrinkImage(imageURL):
  filename = 'temp.jpg'
  request = requests.get(imageURL, stream=True)
  if request.status_code == 200:
    with open(filename, 'wb') as image:
      for chunk in request:
        image.write(chunk)
    return filename

  else:
    return False


def getDrinkData(ingredient):

  drinks = getDrinksByIngredient(ingredient)
  numberOfDrinks = len(drinks)
  if numberOfDrinks > 0:
    randomDrink = random.randint(0, (numberOfDrinks-1))

    name        = drinks[randomDrink]['name']
    imageURL    = drinks[randomDrink]['image']
    image       = downloadDrinkImage(imageURL)
    drinkID     = drinks[randomDrink]['drinkID']
    recipe      = getRecipe(drinkID)
    ingredients = ("\n").join(recipe['ingredients'])


    message = "Try out: {}!\n{}".format(name, ingredients)
    instructions = recipe['instructions']

    data = {'message': message,
            'instructions': instructions,
            'image': image}

    return data


