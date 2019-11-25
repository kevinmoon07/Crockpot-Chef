from flask import Flask, render_template, request
import spoonacular as sp
import app_config
from functions import getRecipes
# initializing api
apiKey = app_config.key
api = sp.API(apiKey)
# initializing app
app = Flask(__name__)

# using one app route    
@app.route('/results', methods=['POST'])
def sortRecipes():
	# request the input, using the input for our API
	ingredients = request.form['ingredients']
	ingredientsStringed = str(ingredients)
	# returns only the top 3 results as of right now
	response = api.search_recipes_by_ingredients(ingredientsStringed, number=3)
	recipeJson = response.json()

	recipeList = []
	for item in recipeJson:
		recipeList.append(getRecipes(item))

	return render_template('results.html', recipeList=recipeList, ingredients=ingredientsStringed)
	# recipeList=recipeList)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
