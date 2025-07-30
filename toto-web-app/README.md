# 🎯 TOTO Analysis & Prediction Web Application

A modern, interactive web application for analyzing Singapore TOTO lottery data and generating number predictions using statistical methods.

## 🚀 Features

### 📊 Statistical Analysis
- **Frequency Analysis**: Complete frequency distribution of all numbers (1-49)
- **Position Analysis**: Analysis by number position (1st, 2nd, 3rd, etc.)
- **Confidence Intervals**: 95% confidence intervals for statistical reliability
- **Hot/Cold Numbers**: Identification of frequently and rarely drawn numbers

### 🎲 Prediction Methods
- **Most Frequent Numbers**: Based on historical frequency analysis
- **Position-Based Analysis**: Selecting most frequent number for each position
- **Hot Numbers**: Based on recent draw patterns
- **Cold Numbers**: Based on least frequently drawn numbers
- **Balanced Approach**: Combination of hot and cold numbers

### 📈 Interactive Visualizations
- **Bar Charts**: Number frequency distribution
- **Area Charts**: Confidence intervals visualization
- **Real-time Updates**: Dynamic data loading and analysis

### 🎨 Modern UI/UX
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark/Light Theme**: Beautiful gradient backgrounds
- **Interactive Components**: Tabs, cards, progress bars, and badges
- **Loading States**: Smooth loading animations

## 🛠️ Technology Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui + Radix UI
- **Charts**: Recharts
- **Icons**: Lucide React
- **Date Handling**: date-fns

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd toto-web-app
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Copy TOTO data**:
   ```bash
   cp ../toto_results.csv public/
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   ```

5. **Open your browser**:
   Navigate to [http://localhost:3000](http://localhost:3000)

## 📁 Project Structure

```
toto-web-app/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   └── toto-data/
│   │   │       └── route.ts          # API endpoint for TOTO data
│   │   ├── globals.css               # Global styles
│   │   ├── layout.tsx                # Root layout
│   │   └── page.tsx                  # Main application page
│   ├── components/
│   │   └── ui/                       # shadcn/ui components
│   ├── lib/
│   │   ├── toto-analysis.ts          # TOTO analysis logic
│   │   └── utils.ts                  # Utility functions
│   └── types/
│       └── toto.ts                   # TypeScript type definitions
├── public/
│   └── toto_results.csv              # TOTO historical data
└── package.json
```

## 🎯 How It Works

### Data Processing
1. **CSV Loading**: Historical TOTO data is loaded from CSV file
2. **Data Parsing**: Raw data is parsed and converted to structured format
3. **Statistical Analysis**: Comprehensive analysis using multiple methods

### Prediction Algorithms
1. **Frequency Analysis**: Counts occurrences of each number
2. **Position Analysis**: Analyzes patterns by number position
3. **Trend Analysis**: Identifies recent patterns and trends
4. **Confidence Calculation**: Provides confidence levels for predictions

### Visualization
1. **Interactive Charts**: Real-time chart updates
2. **Responsive Design**: Adapts to different screen sizes
3. **Modern UI**: Clean, professional interface

## 📊 Analysis Methods

### Statistical Methods
- **Frequency Distribution**: Complete analysis of number frequencies
- **Confidence Intervals**: 95% confidence intervals for reliability
- **Position Analysis**: Pattern analysis by number position
- **Trend Analysis**: Recent draw pattern identification

### Prediction Methods
1. **Most Frequent**: Numbers that appear most often historically
2. **Position-Based**: Most frequent number for each position
3. **Hot Numbers**: Numbers appearing frequently in recent draws
4. **Cold Numbers**: Numbers that rarely appear
5. **Balanced**: Mix of hot and cold numbers

## 🎨 UI Components

### Main Sections
- **Predictions Tab**: Shows all prediction methods with confidence levels
- **Statistics Tab**: Detailed statistical analysis and frequency data
- **Charts Tab**: Interactive visualizations and graphs
- **Data Tab**: Raw historical data display

### Interactive Elements
- **Progress Bars**: Show confidence levels
- **Badges**: Display numbers and categories
- **Cards**: Organize information in clean sections
- **Tabs**: Navigate between different views

## 🔧 Customization

### Adding New Prediction Methods
1. Extend the `TotoAnalyzer` class in `src/lib/toto-analysis.ts`
2. Add new prediction logic to `generatePredictions()` method
3. Update TypeScript types in `src/types/toto.ts`

### Styling Customization
1. Modify Tailwind classes in components
2. Update global styles in `src/app/globals.css`
3. Customize shadcn/ui theme in `components.json`

### Data Source
1. Replace `public/toto_results.csv` with new data
2. Update data parsing logic if format changes
3. Modify API route in `src/app/api/toto-data/route.ts`

## 🚀 Deployment

### Vercel (Recommended)
1. Push code to GitHub
2. Connect repository to Vercel
3. Deploy automatically

### Other Platforms
1. Build the application: `npm run build`
2. Start production server: `npm start`
3. Deploy to your preferred platform

## 📈 Performance

- **Fast Loading**: Optimized data loading and processing
- **Responsive**: Works on all device sizes
- **Efficient**: Minimal bundle size with tree shaking
- **Scalable**: Can handle large datasets

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This application is for educational and entertainment purposes only. Lottery predictions are not guaranteed and should not be used as the sole basis for gambling decisions. Please gamble responsibly.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review the code comments

---

**Built with ❤️ using Next.js, TypeScript, and shadcn/ui**
