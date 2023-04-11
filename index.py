import requests

dish_name_input = input("Enter the name of the dish: ")

url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={dish_name_input}"

try:
    response = requests.get(url)
except Exception as err:
    print("Some error has occured...\nExiting the program!")
    exit()

if response.status_code == 200:
    data = response.json()
    
    if data['meals']:
        meal = data['meals'][0] 
        dish_name = meal['strMeal']
        recipe = meal['strInstructions']
        
        ingredients = []
        for i in range(1, 21):
            ingredient_key = f'strIngredient{i}'
            measure_key = f'strMeasure{i}'
            ingredient = meal.get(ingredient_key, None)
            measure = meal.get(measure_key, None)
            if ingredient is not None and measure is not None:
                ingredient = ingredient.strip()
                measure = measure.strip()
                if ingredient:
                    ingredient_with_measure = f"{measure} {ingredient}"
                    ingredients.append(ingredient_with_measure)

        print(f"Dish Name: {dish_name}")
        print(f"Recipe: {recipe}")
        print("Ingredients:")
        for ingredient in ingredients:
            print(ingredient)
    else:
        print(f"No meals found for '{dish_name_input}'.")
else:
    print("Failed to retrieve data from the API.")
