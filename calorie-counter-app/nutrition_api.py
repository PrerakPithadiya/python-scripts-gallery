"""
Nutrition API Module for Calorie Counter App
Provides multiple API integrations for accurate calorie data
"""

import requests
import json
import time
from typing import Dict, List, Optional, Tuple
from nutrition_data import NutritionData
from free_nutrition_db import FreeNutritionDB

class NutritionAPI:
    """Base class for nutrition APIs"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CalorieCounterApp/1.0'
        })
    
    def search_food(self, food_name: str) -> List[NutritionData]:
        """Search for food and return nutrition data"""
        raise NotImplementedError

class USDAFoodDataAPI(NutritionAPI):
    """USDA FoodData Central API integration"""
    
    def __init__(self, api_key: str = None):
        super().__init__(api_key)
        self.base_url = "https://api.nal.usda.gov/fdc/v1"
    
    def search_food(self, food_name: str) -> List[NutritionData]:
        """Search USDA FoodData Central for food items"""
        try:
            # Search for foods
            search_url = f"{self.base_url}/foods/search"
            params = {
                'query': food_name,
                'pageSize': 10,
                'api_key': self.api_key
            }
            
            response = self.session.get(search_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for food in data.get('foods', []):
                nutrition_data = self._extract_nutrition_data(food)
                if nutrition_data:
                    results.append(nutrition_data)
            
            return results
            
        except Exception as e:
            print(f"USDA API Error: {e}")
            return []
    
    def _extract_nutrition_data(self, food: Dict) -> Optional[NutritionData]:
        """Extract nutrition data from USDA food item"""
        try:
            # Get basic info
            description = food.get('description', '')
            fdc_id = food.get('fdcId')
            
            # Get detailed nutrition info
            detail_url = f"{self.base_url}/food/{fdc_id}"
            params = {'api_key': self.api_key}
            
            detail_response = self.session.get(detail_url, params=params, timeout=10)
            detail_response.raise_for_status()
            detail_data = detail_response.json()
            
            # Extract nutrients
            nutrients = detail_data.get('foodNutrients', [])
            nutrient_dict = {n['nutrient']['name']: n['amount'] for n in nutrients if n.get('amount')}
            
            # Calculate calories per 100g
            calories = nutrient_dict.get('Energy', 0)
            if calories == 0:
                # Try alternative energy names
                for key in ['Calories', 'Total Energy', 'Energy (kcal)']:
                    if key in nutrient_dict:
                        calories = nutrient_dict[key]
                        break
            
            # Get serving size info
            serving_size = "100g"
            if 'servingSize' in detail_data:
                serving_size = f"{detail_data['servingSize']}g"
            
            return NutritionData(
                food_name=description,
                calories=round(calories, 2),
                serving_size=serving_size,
                protein=round(nutrient_dict.get('Protein', 0), 2),
                carbs=round(nutrient_dict.get('Carbohydrate, by difference', 0), 2),
                fat=round(nutrient_dict.get('Total lipid (fat)', 0), 2),
                fiber=round(nutrient_dict.get('Fiber, total dietary', 0), 2),
                sugar=round(nutrient_dict.get('Sugars, total including NLEA', 0), 2),
                source="USDA FoodData Central",
                confidence=0.95
            )
            
        except Exception as e:
            print(f"Error extracting USDA data: {e}")
            return None

class EdamamNutritionAPI(NutritionAPI):
    """Edamam Nutrition API integration"""
    
    def __init__(self, app_id: str, app_key: str):
        super().__init__()
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = "https://api.edamam.com/api/nutrition-data"
    
    def search_food(self, food_name: str) -> List[NutritionData]:
        """Search Edamam for nutrition data"""
        try:
            params = {
                'app_id': self.app_id,
                'app_key': self.app_key,
                'ingr': food_name
            }
            
            response = self.session.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'calories' in data:
                nutrition_data = self._extract_nutrition_data(data, food_name)
                return [nutrition_data] if nutrition_data else []
            
            return []
            
        except Exception as e:
            print(f"Edamam API Error: {e}")
            return []
    
    def _extract_nutrition_data(self, data: Dict, food_name: str) -> Optional[NutritionData]:
        """Extract nutrition data from Edamam response"""
        try:
            nutrients = data.get('totalNutrients', {})
            
            return NutritionData(
                food_name=food_name,
                calories=round(data.get('calories', 0), 2),
                serving_size="100g",
                protein=round(nutrients.get('PROCNT', {}).get('quantity', 0), 2),
                carbs=round(nutrients.get('CHOCDF', {}).get('quantity', 0), 2),
                fat=round(nutrients.get('FAT', {}).get('quantity', 0), 2),
                fiber=round(nutrients.get('FIBTG', {}).get('quantity', 0), 2),
                sugar=round(nutrients.get('SUGAR', {}).get('quantity', 0), 2),
                source="Edamam",
                confidence=0.90
            )
            
        except Exception as e:
            print(f"Error extracting Edamam data: {e}")
            return None

class SpoonacularAPI(NutritionAPI):
    """Spoonacular API integration for food ingredients"""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://api.spoonacular.com/food/ingredients"
    
    def search_food(self, food_name: str) -> List[NutritionData]:
        """Search Spoonacular for food ingredients"""
        try:
            # Search for ingredients
            search_url = f"{self.base_url}/search"
            params = {
                'query': food_name,
                'number': 10,
                'apiKey': self.api_key
            }
            
            response = self.session.get(search_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for ingredient in data.get('results', []):
                # Get detailed nutrition for each ingredient
                nutrition_data = self._get_ingredient_nutrition(ingredient['id'])
                if nutrition_data:
                    results.append(nutrition_data)
            
            return results
            
        except Exception as e:
            print(f"Spoonacular API Error: {e}")
            return []
    
    def _get_ingredient_nutrition(self, ingredient_id: int) -> Optional[NutritionData]:
        """Get detailed nutrition for a specific ingredient"""
        try:
            nutrition_url = f"{self.base_url}/{ingredient_id}/information"
            params = {
                'apiKey': self.api_key,
                'amount': 100,
                'unit': 'grams'
            }
            
            response = self.session.get(nutrition_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            nutrition = data.get('nutrition', {})
            nutrients = nutrition.get('nutrients', [])
            
            # Create nutrient dictionary
            nutrient_dict = {n['name']: n['amount'] for n in nutrients}
            
            return NutritionData(
                food_name=data.get('name', ''),
                calories=round(nutrient_dict.get('Calories', 0), 2),
                serving_size="100g",
                protein=round(nutrient_dict.get('Protein', 0), 2),
                carbs=round(nutrient_dict.get('Carbohydrates', 0), 2),
                fat=round(nutrient_dict.get('Fat', 0), 2),
                fiber=round(nutrient_dict.get('Fiber', 0), 2),
                sugar=round(nutrient_dict.get('Sugar', 0), 2),
                source="Spoonacular",
                confidence=0.85
            )
            
        except Exception as e:
            print(f"Error getting ingredient nutrition: {e}")
            return None

class NutritionAPIManager:
    """Manages multiple nutrition APIs for redundancy and accuracy"""
    
    def __init__(self, config: Dict[str, str]):
        self.apis = []
        
        # Initialize available APIs
        if config.get('USDA_API_KEY'):
            self.apis.append(USDAFoodDataAPI(config['USDA_API_KEY']))
        
        if config.get('EDAMAM_APP_ID') and config.get('EDAMAM_APP_KEY'):
            self.apis.append(EdamamNutritionAPI(
                config['EDAMAM_APP_ID'], 
                config['EDAMAM_APP_KEY']
            ))
        
        if config.get('SPOONACULAR_API_KEY'):
            self.apis.append(SpoonacularAPI(config['SPOONACULAR_API_KEY']))
        
        # Always add free database as fallback
        self.free_db = FreeNutritionDB()
    
    def search_food(self, food_name: str) -> List[NutritionData]:
        """Search all available APIs and return combined results"""
        all_results = []
        
        # Try external APIs first
        for api in self.apis:
            try:
                results = api.search_food(food_name)
                all_results.extend(results)
                time.sleep(0.1)  # Rate limiting
            except Exception as e:
                print(f"API Error: {e}")
                continue
        
        # If no results from external APIs, try free database
        if not all_results:
            try:
                free_results = self.free_db.search_food(food_name)
                all_results.extend(free_results)
            except Exception as e:
                print(f"Free DB Error: {e}")
        
        # Remove duplicates and sort by confidence
        unique_results = self._remove_duplicates(all_results)
        return sorted(unique_results, key=lambda x: x.confidence, reverse=True)
    
    def _remove_duplicates(self, results: List[NutritionData]) -> List[NutritionData]:
        """Remove duplicate food items based on name similarity"""
        unique_results = []
        seen_names = set()
        
        for result in results:
            # Simple deduplication based on name similarity
            name_lower = result.food_name.lower()
            if name_lower not in seen_names:
                seen_names.add(name_lower)
                unique_results.append(result)
        
        return unique_results
