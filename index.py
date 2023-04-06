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
        
        print("Meal Data :", meal)
        print("Dish Name :", dish_name)
        print("Recipe :", recipe)
    else:
        print(f"No meals found for '{dish_name_input}'.")
else:
    print("Failed to retrieve data from the API.")
