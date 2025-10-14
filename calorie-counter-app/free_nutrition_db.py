"""
Free Nutrition Database
Provides basic nutrition data for common foods as a fallback
"""

from typing import List, Optional
from nutrition_data import NutritionData

class FreeNutritionDB:
    """Free nutrition database with common foods"""
    
    def __init__(self):
        self.foods_db = {
            # Fruits
            'apple': {'calories': 52, 'protein': 0.3, 'carbs': 14, 'fat': 0.2, 'fiber': 2.4, 'sugar': 10},
            'banana': {'calories': 89, 'protein': 1.1, 'carbs': 23, 'fat': 0.3, 'fiber': 2.6, 'sugar': 12},
            'orange': {'calories': 47, 'protein': 0.9, 'carbs': 12, 'fat': 0.1, 'fiber': 2.4, 'sugar': 9},
            'strawberry': {'calories': 32, 'protein': 0.7, 'carbs': 8, 'fat': 0.3, 'fiber': 2, 'sugar': 4.9},
            'blueberry': {'calories': 57, 'protein': 0.7, 'carbs': 14, 'fat': 0.3, 'fiber': 2.4, 'sugar': 10},
            'grape': {'calories': 62, 'protein': 0.6, 'carbs': 16, 'fat': 0.2, 'fiber': 0.9, 'sugar': 16},
            'pear': {'calories': 57, 'protein': 0.4, 'carbs': 15, 'fat': 0.1, 'fiber': 3.1, 'sugar': 10},
            'peach': {'calories': 39, 'protein': 0.9, 'carbs': 10, 'fat': 0.3, 'fiber': 1.5, 'sugar': 8},
            
            # Vegetables
            'broccoli': {'calories': 34, 'protein': 2.8, 'carbs': 7, 'fat': 0.4, 'fiber': 2.6, 'sugar': 1.5},
            'carrot': {'calories': 41, 'protein': 0.9, 'carbs': 10, 'fat': 0.2, 'fiber': 2.8, 'sugar': 4.7},
            'spinach': {'calories': 23, 'protein': 2.9, 'carbs': 3.6, 'fat': 0.4, 'fiber': 2.2, 'sugar': 0.4},
            'tomato': {'calories': 18, 'protein': 0.9, 'carbs': 3.9, 'fat': 0.2, 'fiber': 1.2, 'sugar': 2.6},
            'potato': {'calories': 77, 'protein': 2, 'carbs': 17, 'fat': 0.1, 'fiber': 2.2, 'sugar': 0.8},
            'onion': {'calories': 40, 'protein': 1.1, 'carbs': 9, 'fat': 0.1, 'fiber': 1.7, 'sugar': 4.2},
            'cucumber': {'calories': 16, 'protein': 0.7, 'carbs': 4, 'fat': 0.1, 'fiber': 0.5, 'sugar': 1.7},
            'lettuce': {'calories': 15, 'protein': 1.4, 'carbs': 2.9, 'fat': 0.2, 'fiber': 1.3, 'sugar': 0.8},
            
            # Proteins
            'chicken breast': {'calories': 165, 'protein': 31, 'carbs': 0, 'fat': 3.6, 'fiber': 0, 'sugar': 0},
            'beef': {'calories': 250, 'protein': 26, 'carbs': 0, 'fat': 17, 'fiber': 0, 'sugar': 0},
            'salmon': {'calories': 208, 'protein': 25, 'carbs': 0, 'fat': 12, 'fiber': 0, 'sugar': 0},
            'egg': {'calories': 155, 'protein': 13, 'carbs': 1.1, 'fat': 11, 'fiber': 0, 'sugar': 1.1},
            'tofu': {'calories': 76, 'protein': 8, 'carbs': 1.9, 'fat': 4.8, 'fiber': 0.3, 'sugar': 0.6},
            'lentils': {'calories': 116, 'protein': 9, 'carbs': 20, 'fat': 0.4, 'fiber': 8, 'sugar': 1.8},
            'beans': {'calories': 127, 'protein': 8.7, 'carbs': 23, 'fat': 0.5, 'fiber': 6.4, 'sugar': 0.3},
            
            # Grains
            'rice': {'calories': 130, 'protein': 2.7, 'carbs': 28, 'fat': 0.3, 'fiber': 0.4, 'sugar': 0.1},
            'bread': {'calories': 265, 'protein': 9, 'carbs': 49, 'fat': 3.2, 'fiber': 2.7, 'sugar': 5.7},
            'pasta': {'calories': 131, 'protein': 5, 'carbs': 25, 'fat': 1.1, 'fiber': 1.8, 'sugar': 0.6},
            'oats': {'calories': 389, 'protein': 17, 'carbs': 66, 'fat': 7, 'fiber': 11, 'sugar': 1},
            'quinoa': {'calories': 120, 'protein': 4.4, 'carbs': 22, 'fat': 1.9, 'fiber': 2.8, 'sugar': 0.9},
            
            # Dairy
            'milk': {'calories': 42, 'protein': 3.4, 'carbs': 5, 'fat': 1, 'fiber': 0, 'sugar': 5},
            'cheese': {'calories': 113, 'protein': 7, 'carbs': 1, 'fat': 9, 'fiber': 0, 'sugar': 0.1},
            'yogurt': {'calories': 59, 'protein': 10, 'carbs': 3.6, 'fat': 0.4, 'fiber': 0, 'sugar': 3.6},
            
            # Nuts & Seeds
            'almonds': {'calories': 579, 'protein': 21, 'carbs': 22, 'fat': 50, 'fiber': 12, 'sugar': 4.4},
            'walnuts': {'calories': 654, 'protein': 15, 'carbs': 14, 'fat': 65, 'fiber': 6.7, 'sugar': 2.6},
            'peanuts': {'calories': 567, 'protein': 26, 'carbs': 16, 'fat': 49, 'fiber': 8.5, 'sugar': 4.7},
            
            # Common foods
            'pizza': {'calories': 266, 'protein': 11, 'carbs': 33, 'fat': 10, 'fiber': 2.3, 'sugar': 3.6},
            'hamburger': {'calories': 295, 'protein': 17, 'carbs': 33, 'fat': 10, 'fiber': 2.1, 'sugar': 6.2},
            'sandwich': {'calories': 300, 'protein': 15, 'carbs': 35, 'fat': 10, 'fiber': 2, 'sugar': 5},
        }
    
    def search_food(self, food_name: str) -> List[NutritionData]:
        """Search for food in the database"""
        food_name_lower = food_name.lower().strip()
        
        # Direct match
        if food_name_lower in self.foods_db:
            food_data = self.foods_db[food_name_lower]
            return [self._create_nutrition_data(food_name, food_data)]
        
        # Partial match
        results = []
        for db_food, data in self.foods_db.items():
            if food_name_lower in db_food or db_food in food_name_lower:
                results.append(self._create_nutrition_data(db_food, data))
        
        return results[:5]  # Return top 5 matches
    
    def _create_nutrition_data(self, food_name: str, data: dict) -> NutritionData:
        """Create NutritionData object from database entry"""
        return NutritionData(
            food_name=food_name.title(),
            calories=data['calories'],
            serving_size="100g",
            protein=data['protein'],
            carbs=data['carbs'],
            fat=data['fat'],
            fiber=data['fiber'],
            sugar=data['sugar'],
            source="Free Nutrition Database",
            confidence=0.80
        )
