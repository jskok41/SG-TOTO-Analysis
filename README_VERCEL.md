# TOTO Number Analysis - Vercel Deployment

This is a web application version of the TOTO Number Analysis tool, designed to be deployed on Vercel.

## 🚀 Quick Deploy to Vercel

### Option 1: Deploy with Vercel CLI

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy the application**:
   ```bash
   vercel
   ```

4. **Follow the prompts**:
   - Set up and deploy: `Y`
   - Which scope: Select your account
   - Link to existing project: `N`
   - Project name: `toto-analysis` (or your preferred name)
   - Directory: `.` (current directory)
   - Override settings: `N`

### Option 2: Deploy via GitHub

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Add Vercel deployment files"
   git push origin main
   ```

2. **Go to [Vercel Dashboard](https://vercel.com/dashboard)**

3. **Click "New Project"**

4. **Import your GitHub repository**

5. **Configure the project**:
   - Framework Preset: `Other`
   - Build Command: Leave empty (Vercel will auto-detect)
   - Output Directory: Leave empty
   - Install Command: Leave empty

6. **Click "Deploy"**

## 📁 Project Structure

```
├── app.py                 # Flask web application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── templates/
│   └── index.html        # Web interface
├── toto_results.csv      # Sample TOTO data
├── main.py              # Original CLI application
├── toto_analysis.py     # Analysis functions
├── monte_carlo.py       # Monte Carlo simulation
├── backtest.py          # Backtesting functions
└── clean_data.py        # Data cleaning utilities
```

## 🌐 Web Interface Features

- **Data Loading**: Load real TOTO data or simulated data
- **Interactive Analysis**: 
  - Individual bar charts
  - Grouped bar charts
  - Overall frequency analysis
  - Confidence interval charts
  - Backtest analysis
- **Monte Carlo Simulation**: Generate new simulated data
- **Responsive Design**: Works on desktop and mobile devices

## 🔧 Configuration

The application uses the following configuration:

- **Flask**: Web framework
- **Pandas**: Data manipulation
- **Matplotlib**: Chart generation
- **Bootstrap**: UI framework
- **Vercel**: Deployment platform

## 📊 Data Requirements

The application expects TOTO data in CSV format with the following columns:
- `Draw_No`: Draw number
- `Draw_Date`: Date of the draw
- `Num1` to `Num6`: The 6 main numbers
- `Additional_Number`: Additional number (optional)

## 🛠️ Local Development

To run the application locally:

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Open your browser** and go to `http://localhost:5000`

## 📝 Notes

- The web version uses a simplified backtest that automatically selects the most frequent numbers
- Charts are generated as base64 images and displayed in the browser
- The application includes sample data for demonstration purposes
- All analysis functions from the original CLI tool are available through the web interface

## 🔗 Deployment URL

After deployment, your application will be available at:
`https://your-project-name.vercel.app`

## 📞 Support

If you encounter any issues with the deployment, check:
1. Vercel deployment logs
2. Python version compatibility (Vercel supports Python 3.9+)
3. All required files are present in the repository