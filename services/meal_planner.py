import openai
import os
import pandas as pd
import requests

# Set your API keys from environment variables for security
openai.api_key = os.getenv("OPENAI_API_KEY")
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

def get_meal_plan_from_ai(user_preferences):
    """
    Calls the LLM API to generate a meal plan based on user preferences.
    """
    prompt = f"""
    Create a 7-day meal plan for a person with the following preferences: {user_preferences}.
    The response should be a text list, with each item containing the meal name.
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",  # or your preferred model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        return "Sorry, I could not generate a meal plan at this time."

def get_recipes_from_spoonacular(ingredients, diet):
    """
    Searches the Spoonacular API for recipes based on ingredients and diet.
    (This is a placeholder function; a more robust version would be needed)
    """
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "includeIngredients": ",".join(ingredients),
        "diet": diet,
        "number": 5
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling Spoonacular API: {e}")
        return {"results": []}

def generate_grocery_list(meal_plan_text):
    """
    Extracts ingredients from a meal plan text to create a grocery list.
    (This is a simplified version and may require more advanced NLP for complex plans)
    """
    # Dummy implementation for now
    example_ingredients = ["avocado", "bread", "lentils", "carrots", "celery", "tofu", "onion", "spinach"]
    return [item for item in example_ingredients if item in meal_plan_text.lower()]
