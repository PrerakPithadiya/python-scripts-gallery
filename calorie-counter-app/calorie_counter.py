"""
Main Calorie Counter Application
Provides a user-friendly interface for real-time calorie counting
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import json
import os
from datetime import datetime
from typing import List, Optional
from nutrition_api import NutritionAPIManager, NutritionData

class CalorieCounterApp:
    """Main application class for the calorie counter"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Counter - Real-Time Nutrition Data")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Load configuration
        self.config = self._load_config()
        self.api_manager = NutritionAPIManager(self.config)
        
        # Search history
        self.search_history = []
        self.load_history()
        
        # Status
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Enter a food item to search")
        
        # Create UI
        self.create_widgets()
    
    def _load_config(self) -> dict:
        """Load API configuration"""
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
            # Use environment variables or defaults
            config = {
                'USDA_API_KEY': os.getenv('USDA_API_KEY', ''),
                'EDAMAM_APP_ID': os.getenv('EDAMAM_APP_ID', ''),
                'EDAMAM_APP_KEY': os.getenv('EDAMAM_APP_KEY', ''),
                'SPOONACULAR_API_KEY': os.getenv('SPOONACULAR_API_KEY', '')
            }
        
        return config
    
    def create_widgets(self):
        """Create the main UI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🍎 Calorie Counter", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Search frame
        search_frame = ttk.LabelFrame(main_frame, text="Search Food Item", padding="10")
        search_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        search_frame.columnconfigure(1, weight=1)
        
        # Food input
        ttk.Label(search_frame, text="Food Item:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.food_entry = ttk.Entry(search_frame, font=('Arial', 12))
        self.food_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.food_entry.bind('<Return>', lambda e: self.search_food())
        
        # Search button
        self.search_btn = ttk.Button(search_frame, text="Search", 
                                   command=self.search_food)
        self.search_btn.grid(row=0, column=2)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Nutrition Information", padding="10")
        results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(results_frame, height=15, 
                                                    font=('Consolas', 10),
                                                    wrap=tk.WORD)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # History frame
        history_frame = ttk.LabelFrame(main_frame, text="Search History", padding="10")
        history_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        history_frame.columnconfigure(0, weight=1)
        
        # History listbox
        self.history_listbox = tk.Listbox(history_frame, height=4, font=('Arial', 10))
        self.history_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.history_listbox.bind('<Double-Button-1>', self.on_history_select)
        
        # Clear history button
        ttk.Button(history_frame, text="Clear History", 
                  command=self.clear_history).grid(row=0, column=1, padx=(10, 0))
        
        # Status bar
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
        status_frame.columnconfigure(0, weight=1)
        
        self.status_label = ttk.Label(status_frame, textvariable=self.status_var, 
                                    anchor=tk.W)
        self.status_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Load history into listbox
        self.update_history_display()
    
    def search_food(self):
        """Search for food item and display results"""
        food_name = self.food_entry.get().strip()
        if not food_name:
            messagebox.showwarning("Warning", "Please enter a food item to search.")
            return
        
        # Disable search button and show loading
        self.search_btn.config(state='disabled', text='Searching...')
        self.status_var.set(f"Searching for '{food_name}'...")
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "Searching for nutrition data...\nPlease wait...")
        
        # Search in background thread
        thread = threading.Thread(target=self._search_food_thread, args=(food_name,))
        thread.daemon = True
        thread.start()
    
    def _search_food_thread(self, food_name: str):
        """Search for food in background thread"""
        try:
            # Search using API manager
            results = self.api_manager.search_food(food_name)
            
            # Update UI in main thread
            self.root.after(0, self._display_results, food_name, results)
            
        except Exception as e:
            error_msg = f"Error searching for food: {str(e)}"
            self.root.after(0, self._display_error, error_msg)
    
    def _display_results(self, food_name: str, results: List[NutritionData]):
        """Display search results"""
        self.search_btn.config(state='normal', text='Search')
        
        if not results:
            self.status_var.set("No results found")
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"No nutrition data found for '{food_name}'.\n\n")
            self.results_text.insert(tk.END, "Suggestions:\n")
            self.results_text.insert(tk.END, "• Check spelling\n")
            self.results_text.insert(tk.END, "• Try a more specific food name\n")
            self.results_text.insert(tk.END, "• Try alternative names (e.g., 'apple' instead of 'red apple')\n")
            return
        
        # Add to history
        self.add_to_history(food_name, results[0])
        
        # Display results
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"🍎 NUTRITION DATA FOR: {food_name.upper()}\n")
        self.results_text.insert(tk.END, "=" * 50 + "\n\n")
        
        for i, result in enumerate(results[:5], 1):  # Show top 5 results
            self.results_text.insert(tk.END, f"RESULT #{i}:\n")
            self.results_text.insert(tk.END, f"Food: {result.food_name}\n")
            self.results_text.insert(tk.END, f"Source: {result.source}\n")
            self.results_text.insert(tk.END, f"Confidence: {result.confidence:.0%}\n")
            self.results_text.insert(tk.END, f"Serving Size: {result.serving_size}\n\n")
            
            self.results_text.insert(tk.END, "NUTRITION PER 100g:\n")
            self.results_text.insert(tk.END, f"🔥 Calories: {result.calories} kcal\n")
            self.results_text.insert(tk.END, f"🥩 Protein: {result.protein} g\n")
            self.results_text.insert(tk.END, f"🍞 Carbohydrates: {result.carbs} g\n")
            self.results_text.insert(tk.END, f"🧈 Fat: {result.fat} g\n")
            self.results_text.insert(tk.END, f"🌾 Fiber: {result.fiber} g\n")
            self.results_text.insert(tk.END, f"🍯 Sugar: {result.sugar} g\n")
            
            if i < len(results):
                self.results_text.insert(tk.END, "\n" + "-" * 40 + "\n\n")
        
        self.status_var.set(f"Found {len(results)} result(s) for '{food_name}'")
    
    def _display_error(self, error_msg: str):
        """Display error message"""
        self.search_btn.config(state='normal', text='Search')
        self.status_var.set("Error occurred")
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"ERROR: {error_msg}\n\n")
        self.results_text.insert(tk.END, "Please check your internet connection and API configuration.")
    
    def add_to_history(self, food_name: str, result: NutritionData):
        """Add search to history"""
        history_item = {
            'food_name': food_name,
            'calories': result.calories,
            'timestamp': datetime.now().isoformat(),
            'source': result.source
        }
        
        # Remove duplicates
        self.search_history = [item for item in self.search_history 
                              if item['food_name'].lower() != food_name.lower()]
        
        # Add to beginning
        self.search_history.insert(0, history_item)
        
        # Keep only last 20 items
        self.search_history = self.search_history[:20]
        
        # Save and update display
        self.save_history()
        self.update_history_display()
    
    def update_history_display(self):
        """Update the history listbox"""
        self.history_listbox.delete(0, tk.END)
        for item in self.search_history:
            display_text = f"{item['food_name']} - {item['calories']} cal ({item['source']})"
            self.history_listbox.insert(tk.END, display_text)
    
    def on_history_select(self, event):
        """Handle history item selection"""
        selection = self.history_listbox.curselection()
        if selection:
            item = self.search_history[selection[0]]
            self.food_entry.delete(0, tk.END)
            self.food_entry.insert(0, item['food_name'])
            self.search_food()
    
    def clear_history(self):
        """Clear search history"""
        self.search_history = []
        self.save_history()
        self.update_history_display()
    
    def save_history(self):
        """Save search history to file"""
        try:
            with open('search_history.json', 'w') as f:
                json.dump(self.search_history, f, indent=2)
        except Exception as e:
            print(f"Error saving history: {e}")
    
    def load_history(self):
        """Load search history from file"""
        try:
            if os.path.exists('search_history.json'):
                with open('search_history.json', 'r') as f:
                    self.search_history = json.load(f)
        except Exception as e:
            print(f"Error loading history: {e}")
            self.search_history = []

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = CalorieCounterApp(root)
    
    # Center window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
