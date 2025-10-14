"""
Test script for Calorie Counter App accuracy verification
Tests the application with common foods to verify data accuracy
"""

import sys
import os
from nutrition_api import NutritionAPIManager

def test_common_foods():
    """Test the app with common foods to verify accuracy"""
    
    # Test foods with known calorie values
    test_foods = [
        "apple",
        "banana", 
        "chicken breast",
        "rice",
        "bread",
        "milk",
        "egg",
        "broccoli",
        "salmon",
        "potato"
    ]
    
    print("Testing Calorie Counter Accuracy")
    print("=" * 50)
    
    # Load configuration
    config = load_test_config()
    api_manager = NutritionAPIManager(config)
    
    if not api_manager.apis:
        print("No APIs configured. Please set up API keys in config.py")
        return
    
    print(f"Loaded {len(api_manager.apis)} API(s)")
    print()
    
    for food in test_foods:
        print(f"Testing: {food}")
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
            else:
                print("No results found")
            
            print()
            
        except Exception as e:
            print(f"Error: {e}")
            print()

def load_test_config():
    """Load configuration for testing"""
    config = {}
    
    # Try to load from config.py
    try:
        import config
        config = {
            'USDA_API_KEY': getattr(config, 'USDA_API_KEY', ''),
            'EDAMAM_APP_ID': getattr(config, 'EDAMAM_APP_ID', ''),
            'EDAMAM_APP_KEY': getattr(config, 'EDAMAM_APP_KEY', ''),
            'SPOONACULAR_API_KEY': getattr(config, 'SPOONACULAR_API_KEY', '')
        }
    except ImportError:
        print("⚠️  config.py not found. Using environment variables or empty config.")
        config = {
            'USDA_API_KEY': os.getenv('USDA_API_KEY', ''),
            'EDAMAM_APP_ID': os.getenv('EDAMAM_APP_ID', ''),
            'EDAMAM_APP_KEY': os.getenv('EDAMAM_APP_KEY', ''),
            'SPOONACULAR_API_KEY': os.getenv('SPOONACULAR_API_KEY', '')
        }
    
    return config

def test_api_connectivity():
    """Test API connectivity"""
    print("Testing API Connectivity")
    print("=" * 30)
    
    config = load_test_config()
    api_manager = NutritionAPIManager(config)
    
    if not api_manager.apis:
        print("No APIs configured")
        return False
    
    # Test with a simple food
    try:
        results = api_manager.search_food("apple")
        if results:
            print("API connectivity test passed")
            return True
        else:
            print("API responded but no results")
            return False
    except Exception as e:
        print(f"API connectivity test failed: {e}")
        return False

if __name__ == "__main__":
    print("Calorie Counter - Accuracy Test")
    print("=" * 40)
    print()
    
    # Test API connectivity first
    if test_api_connectivity():
        print()
        test_common_foods()
    else:
        print("\nCannot proceed with accuracy tests due to API connectivity issues")
        print("Please check your API configuration in config.py")
