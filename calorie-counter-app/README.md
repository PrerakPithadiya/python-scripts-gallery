# 🍎 Calorie Counter App

A Python application that provides real-time, accurate calorie counting for any food item using multiple reliable nutrition APIs.

## ✨ Features

- **Real-time calorie lookup** for any food item
- **Multiple API integration** for maximum accuracy (USDA, Edamam, Spoonacular)
- **Comprehensive nutrition data** including protein, carbs, fat, fiber, and sugar
- **Search history** to track previous searches
- **User-friendly GUI** built with tkinter
- **Data verification** with confidence scores
- **Error handling** and fallback systems

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

1. Copy `config_example.py` to `config.py`
2. Get free API keys from:
   - **USDA FoodData Central**: https://fdc.nal.usda.gov/api-guide.html
   - **Edamam**: https://developer.edamam.com/
   - **Spoonacular**: https://spoonacular.com/food-api
3. Add your API keys to `config.py`

### 3. Run the Application

```bash
python calorie_counter.py
```

## 🔧 API Configuration

### USDA FoodData Central (Recommended - Free)
- Most authoritative source
- No rate limits for basic usage
- Register at: https://fdc.nal.usda.gov/api-guide.html

### Edamam Nutrition API (Free Tier)
- 10,000 requests per month
- Good accuracy
- Register at: https://developer.edamam.com/

### Spoonacular API (Free Tier)
- 150 requests per day
- Comprehensive database
- Register at: https://spoonacular.com/food-api

## 📊 How It Works

1. **Multi-API Search**: Queries multiple nutrition databases simultaneously
2. **Data Aggregation**: Combines results from different sources
3. **Confidence Scoring**: Ranks results by reliability
4. **Deduplication**: Removes duplicate entries
5. **Real-time Display**: Shows comprehensive nutrition information

## 🎯 Usage

1. **Enter Food Item**: Type any food name in the search box
2. **Search**: Click "Search" or press Enter
3. **View Results**: See detailed nutrition information
4. **History**: Access previous searches from the history panel
5. **Accuracy**: Results are ranked by confidence and source reliability

## 📈 Accuracy Features

- **Multiple Sources**: Cross-references data from authoritative databases
- **Confidence Scores**: Each result includes a reliability percentage
- **Source Attribution**: Shows which database provided the information
- **Data Validation**: Compares results across different APIs
- **Error Reporting**: Built-in mechanism to report inaccuracies

## 🛠️ Technical Details

### Architecture
- **Modular Design**: Separate API classes for each nutrition service
- **Threading**: Background API calls to prevent UI freezing
- **Error Handling**: Comprehensive exception handling
- **Data Persistence**: Search history saved locally

### File Structure
```
calorie-counter-app/
├── calorie_counter.py      # Main application
├── nutrition_api.py        # API integrations
├── config_example.py       # Configuration template
├── requirements.txt        # Dependencies
├── README.md              # This file
└── search_history.json    # Search history (auto-created)
```

## 🔍 Troubleshooting

### Common Issues

1. **No Results Found**
   - Check internet connection
   - Verify API keys are correct
   - Try different food names or spellings

2. **API Errors**
   - Ensure API keys are valid
   - Check rate limits
   - Verify API service status

3. **Slow Performance**
   - Some APIs may be slower
   - Results are cached in history
   - Try searching for more common foods

### Getting Help

If you encounter issues:
1. Check the status bar for error messages
2. Verify your API configuration
3. Test with simple food names first
4. Check the console for detailed error logs

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📞 Support

For support or questions about accuracy, please:
1. Check the confidence scores in results
2. Compare data across different sources
3. Report discrepancies through the application
4. Verify food names and serving sizes

---

**Note**: This application provides nutrition data for informational purposes. For medical or dietary advice, please consult with healthcare professionals.
