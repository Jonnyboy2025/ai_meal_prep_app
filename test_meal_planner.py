from services.meal_planner import (
    get_meal_plan_from_ai,
    get_recipes_from_spoonacular,
    generate_grocery_list
)

# Test get_meal_plan_from_ai
user_preferences = "vegetarian, high protein, no dairy"
meal_plan = get_meal_plan_from_ai(user_preferences)
print("Meal Plan from AI:")
print(meal_plan)

# Test get_recipes_from_spoonacular
ingredients = ["avocado", "bread", "lentils"]
diet = "vegetarian"
recipes = get_recipes_from_spoonacular(ingredients, diet)
print("\nRecipes from Spoonacular:")
print(recipes)

# Test generate_grocery_list
grocery_list = generate_grocery_list(meal_plan)
print("\nGenerated Grocery List:")
print(grocery_list)