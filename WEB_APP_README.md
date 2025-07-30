# TOTO Number Analysis - Web Application

## 🌐 Overview

This is a modern, interactive web application for analyzing Singapore TOTO lottery patterns. The application provides a beautiful, responsive interface for statistical analysis, data visualization, and strategy backtesting.

## ✨ Features

### 📊 Analysis Tools
- **Frequency Analysis**: Analyze number frequency distributions
- **Position Analysis**: Examine patterns by position (1st, 2nd, 3rd, etc.)
- **Grouped Analysis**: Compare distributions across positions
- **Confidence Intervals**: Statistical confidence analysis
- **Backtest Strategy**: Test prediction strategies on historical data

### 🎨 User Interface
- **Modern Design**: Beautiful gradient backgrounds and smooth animations
- **Responsive Layout**: Works on desktop, tablet, and mobile devices
- **Interactive Charts**: Dynamic matplotlib visualizations
- **Real-time Updates**: Live data processing and results display

### 📁 Data Management
- **Generate Data**: Create new simulated TOTO draws
- **Load Data**: Import existing CSV files
- **Export Results**: Download analysis data as CSV
- **Sample Data**: View and explore data samples

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Virtual environment support

### Installation

1. **Clone or download the project files**

2. **Create virtual environment**:
   ```bash
   python3 -m venv toto_venv
   ```

3. **Activate virtual environment**:
   ```bash
   # On Windows:
   toto_venv\Scripts\activate
   
   # On macOS/Linux:
   source toto_venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the web application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## 📖 Usage Guide

### 1. Data Management
- **Generate New Data**: Enter the number of draws (100-100,000) and click "Generate Data"
- **Load Existing Data**: Enter the filename (e.g., "simulated_draws.csv") and click "Load Data"

### 2. Running Analysis
Click any of the analysis buttons to perform different types of analysis:

- **Frequency Analysis**: Shows how often each number appears
- **Position Analysis**: Analyzes patterns by position in the draw
- **Grouped Analysis**: Compares distributions across positions
- **Confidence Intervals**: Statistical confidence analysis
- **Backtest Strategy**: Tests prediction strategies

### 3. Viewing Results
- **Charts**: Interactive matplotlib visualizations
- **Statistics**: Detailed numerical analysis
- **Sample Data**: View the actual data being analyzed
- **Download**: Export results as CSV files

## 🏗️ Architecture

### Backend (Flask)
- **app.py**: Main Flask application
- **API Endpoints**: RESTful endpoints for data processing
- **Analysis Integration**: Connects to existing analysis modules

### Frontend (HTML/CSS/JavaScript)
- **Bootstrap 5**: Modern responsive framework
- **Font Awesome**: Beautiful icons
- **Custom CSS**: Gradient backgrounds and animations
- **JavaScript**: Async API calls and dynamic updates

### Analysis Modules
- **clean_data.py**: Data loading and cleaning
- **toto_analysis.py**: Statistical analysis functions
- **monte_carlo.py**: Data simulation
- **backtest.py**: Strategy testing

## 📁 File Structure

```
toto-number-analysis/
├── app.py                 # Flask web application
├── templates/
│   └── index.html        # Main HTML template
├── toto_analysis.py      # Analysis functions
├── monte_carlo.py        # Data simulation
├── backtest.py           # Strategy testing
├── clean_data.py         # Data processing
├── requirements.txt      # Python dependencies
├── simulated_draws.csv   # Sample data
├── start_webapp.py       # Startup script
└── WEB_APP_README.md     # This file
```

## 🔧 Configuration

### Port Configuration
The application runs on port 5000 by default. To change this, modify `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=YOUR_PORT)
```

### Data File Location
The application looks for data files in the current directory. You can modify the file paths in the Flask routes.

## 🎯 Analysis Features

### Frequency Analysis
- Counts occurrences of each number (1-49)
- Identifies most and least frequent numbers
- Visualizes distribution patterns

### Position Analysis
- Analyzes patterns by position in the draw
- Calculates mean, standard deviation, and range
- Shows position-specific trends

### Statistical Analysis
- Confidence intervals for predictions
- Statistical significance testing
- Pattern recognition algorithms

### Strategy Backtesting
- Tests prediction strategies on historical data
- Calculates success rates and performance metrics
- Provides strategy recommendations

## 🛠️ Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   # Find and kill the process using port 5000
   lsof -ti:5000 | xargs kill -9
   ```

2. **Virtual environment not activated**:
   ```bash
   source toto_venv/bin/activate
   ```

3. **Missing dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Data file not found**:
   - Ensure `simulated_draws.csv` exists
   - Or generate new data using the web interface

### Error Messages

- **"No data loaded"**: Generate or load data first
- **"Failed to load data"**: Check file format and location
- **"Network error"**: Check if the Flask server is running

## 🔒 Security Notes

- The application runs in debug mode for development
- For production, disable debug mode and use proper WSGI server
- Consider adding authentication for sensitive data

## 📈 Performance

- **Data Generation**: 1000 draws in ~1 second
- **Analysis**: Most analyses complete in <5 seconds
- **Charts**: Generated dynamically with matplotlib
- **Memory**: Efficient pandas data handling

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational and research purposes. Please use responsibly.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the console output for error messages
3. Ensure all dependencies are installed
4. Verify data file format and location

---

**Enjoy analyzing TOTO patterns! 🎯**