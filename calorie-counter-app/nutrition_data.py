"""
Nutrition Data Models
Data classes for storing nutrition information
"""

from dataclasses import dataclass

@dataclass
class NutritionData:
    """Data class to store nutrition information"""
    food_name: str
    calories: float
    serving_size: str
    protein: float = 0.0
    carbs: float = 0.0
    fat: float = 0.0
    fiber: float = 0.0
    sugar: float = 0.0
    source: str = ""
    confidence: float = 0.0

