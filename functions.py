# Missed Ingredients accounts for the ingredients that are a part of the recipe that the user did not specify. Missed ingredients do not account for staples such as sugar and water. Unused ingredients are ingredients that the user has specified that are not a part of the recipe.

def getRecipes(item):
    # simple data unpacking - numerical values
    title = item['title']
    image = item['image']
    numOfUsedIngredients = item['usedIngredientCount']
    numOfMissedIngredients = item['missedIngredientCount']
    numTotalIngredients = numOfMissedIngredients + numOfUsedIngredients
    matchVal =  (numOfUsedIngredients / numTotalIngredients) * 100
    matchPercent = str(round(matchVal / numTotalIngredients, 2)) + '%'

    # unpacking of lists, particular to list of ingredients

    usedIngredients = []
    missedIngredients = []

    for ingredient1 in item['missedIngredients']:
        missedIngredients.append(ingredient1['name'])

    for ingredient2 in item['usedIngredients']:
        usedIngredients.append(ingredient2['name'])

    allIngredients = missedIngredients + usedIngredients


    recipeInfo = {
        'title': title,
        'image': image,
        'numOfUsedIngredients': numOfUsedIngredients,
        'numOfMissedIngredients': numOfMissedIngredients,
        'usedIngredients': usedIngredients,
        'unusedIngredients': missedIngredients,
        'matchPercent': matchPercent,
        'allIngredients': allIngredients
    }
    # returns the dictionary of items
    return recipeInfo
