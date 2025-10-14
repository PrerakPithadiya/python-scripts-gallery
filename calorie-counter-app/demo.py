"""
Demo script for Calorie Counter App
Shows how the application works with available data
"""

import sys
import os
from nutrition_api import NutritionAPIManager

def demo_search():
    """Demo the calorie counter with working examples"""
    
    print("Calorie Counter App - Demo")
    print("=" * 40)
    print()
    
    # Load configuration
    config = load_config()
    api_manager = NutritionAPIManager(config)
    
    if not api_manager.apis:
        print("No APIs configured. Please set up API keys in config.py")
        return
    
    print(f"Loaded {len(api_manager.apis)} API(s)")
    print()
    
    # Demo foods that work with free Spoonacular API
    demo_foods = [
        "apple",
        "banana", 
        "orange",
        "strawberry",
        "blueberry"
    ]
    
    for food in demo_foods:
        print(f"Searching for: {food}")
        print("-" * 30)
        
        try:
            results = api_manager.search_food(food)
            
            if results:
                best_result = results[0]
                print(f"Found: {best_result.food_name}")
                print(f"Calories: {best_result.calories} kcal per {best_result.serving_size}")
                print(f"Source: {best_result.source}")
                print(f"Confidence: {best_result.confidence:.0%}")
                print(f"Protein: {best_result.protein}g")
                print(f"Carbs: {best_result.carbs}g")
                print(f"Fat: {best_result.fat}g")
                print(f"Fiber: {best_result.fiber}g")
                print(f"Sugar: {best_result.sugar}g")
            else:
                print("No results found")
            
            print()
            
        except Exception as e:
            print(f"Error: {e}")
            print()

def load_config():
    """Load configuration"""
    config = {}
    
    try:
        import config
        config = {
            'USDA_API_KEY': getattr(config, 'USDA_API_KEY', ''),
            'EDAMAM_APP_ID': getattr(config, 'EDAMAM_APP_ID', ''),
            'EDAMAM_APP_KEY': getattr(config, 'EDAMAM_APP_KEY', ''),
            'SPOONACULAR_API_KEY': getattr(config, 'SPOONACULAR_API_KEY', '')
        }
    except ImportError:
        config = {
            'USDA_API_KEY': os.getenv('USDA_API_KEY', ''),
            'EDAMAM_APP_ID': os.getenv('EDAMAM_APP_ID', ''),
            'EDAMAM_APP_KEY': os.getenv('EDAMAM_APP_KEY', ''),
            'SPOONACULAR_API_KEY': os.getenv('SPOONACULAR_API_KEY', '')
        }
    
    return config

def show_usage_instructions():
    """Show usage instructions"""
    print("\nUSAGE INSTRUCTIONS:")
    print("=" * 30)
    print()
    print("1. GUI Application:")
    print("   python calorie_counter.py")
    print("   - Enter any food item in the search box")
    print("   - Click 'Search' or press Enter")
    print("   - View detailed nutrition information")
    print("   - Check search history")
    print()
    print("2. Command Line Demo:")
    print("   python demo.py")
    print("   - Shows working examples")
    print()
    print("3. Accuracy Test:")
    print("   python test_accuracy.py")
    print("   - Tests API connectivity and accuracy")
    print()
    print("4. Setup Guide:")
    print("   python setup_guide.py")
    print("   - Helps configure additional API keys")
    print()

if __name__ == "__main__":
    demo_search()
    show_usage_instructions()

