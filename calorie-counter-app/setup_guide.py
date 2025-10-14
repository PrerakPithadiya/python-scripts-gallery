"""
Setup Guide for Calorie Counter App
Helps users configure API keys and test the application
"""

import os
import webbrowser
from pathlib import Path

def print_banner():
    """Print welcome banner"""
    print("🍎" + "=" * 50 + "🍎")
    print("    CALORIE COUNTER APP - SETUP GUIDE")
    print("🍎" + "=" * 50 + "🍎")
    print()

def check_config():
    """Check if config.py exists"""
    config_path = Path("config.py")
    if config_path.exists():
        print("✅ config.py found")
        return True
    else:
        print("❌ config.py not found")
        return False

def create_config():
    """Create config.py from template"""
    try:
        # Read template
        with open("config_example.py", "r") as f:
            template = f.read()
        
        # Write config.py
        with open("config.py", "w") as f:
            f.write(template)
        
        print("✅ Created config.py from template")
        return True
    except Exception as e:
        print(f"❌ Error creating config.py: {e}")
        return False

def get_api_instructions():
    """Print API setup instructions"""
    print("\n🔑 API SETUP INSTRUCTIONS")
    print("=" * 40)
    print()
    
    print("1. USDA FOODDATA CENTRAL (Recommended - Free)")
    print("   • Most authoritative source")
    print("   • No rate limits")
    print("   • Register at: https://fdc.nal.usda.gov/api-guide.html")
    print("   • Copy your API key to config.py")
    print()
    
    print("2. EDAMAM NUTRITION API (Free Tier)")
    print("   • 10,000 requests per month")
    print("   • Good accuracy")
    print("   • Register at: https://developer.edamam.com/")
    print("   • Copy App ID and App Key to config.py")
    print()
    
    print("3. SPOONACULAR API (Free Tier)")
    print("   • 150 requests per day")
    print("   • Comprehensive database")
    print("   • Register at: https://spoonacular.com/food-api")
    print("   • Copy API key to config.py")
    print()

def open_api_links():
    """Open API registration links in browser"""
    print("\n🌐 Opening API registration links...")
    
    apis = [
        ("USDA FoodData Central", "https://fdc.nal.usda.gov/api-guide.html"),
        ("Edamam", "https://developer.edamam.com/"),
        ("Spoonacular", "https://spoonacular.com/food-api")
    ]
    
    for name, url in apis:
        try:
            print(f"   Opening {name}...")
            webbrowser.open(url)
        except Exception as e:
            print(f"   ❌ Could not open {name}: {e}")

def test_setup():
    """Test the setup"""
    print("\n🧪 TESTING SETUP")
    print("=" * 20)
    
    # Check if config.py exists
    if not check_config():
        print("Creating config.py...")
        if not create_config():
            return False
    
    # Test imports
    try:
        import config
        print("✅ config.py imports successfully")
    except Exception as e:
        print(f"❌ Error importing config: {e}")
        return False
    
    # Check for API keys
    api_keys = {
        'USDA_API_KEY': getattr(config, 'USDA_API_KEY', ''),
        'EDAMAM_APP_ID': getattr(config, 'EDAMAM_APP_ID', ''),
        'EDAMAM_APP_KEY': getattr(config, 'EDAMAM_APP_KEY', ''),
        'SPOONACULAR_API_KEY': getattr(config, 'SPOONACULAR_API_KEY', '')
    }
    
    configured_apis = sum(1 for key, value in api_keys.items() 
                         if value and value != f"your_{key.lower()}_here")
    
    print(f"✅ {configured_apis} API(s) configured")
    
    if configured_apis == 0:
        print("⚠️  No API keys configured yet")
        return False
    
    return True

def run_accuracy_test():
    """Run accuracy test"""
    print("\n🧪 RUNNING ACCURACY TEST")
    print("=" * 30)
    
    try:
        import test_accuracy
        test_accuracy.test_api_connectivity()
    except Exception as e:
        print(f"❌ Error running accuracy test: {e}")

def main():
    """Main setup function"""
    print_banner()
    
    print("Welcome to the Calorie Counter App setup!")
    print("This guide will help you configure the application for accurate calorie counting.")
    print()
    
    # Check current setup
    if test_setup():
        print("\n✅ Setup looks good!")
        
        choice = input("\nWould you like to run an accuracy test? (y/n): ").lower()
        if choice == 'y':
            run_accuracy_test()
        
        print("\n🚀 You're ready to use the Calorie Counter App!")
        print("Run: python calorie_counter.py")
        
    else:
        print("\n📋 SETUP STEPS:")
        print("1. Get API keys from the links below")
        print("2. Edit config.py with your API keys")
        print("3. Run this setup guide again")
        print("4. Run the accuracy test")
        print("5. Start using the app!")
        
        choice = input("\nWould you like to open API registration links? (y/n): ").lower()
        if choice == 'y':
            open_api_links()
        
        get_api_instructions()

if __name__ == "__main__":
    main()
