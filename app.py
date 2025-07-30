#!/usr/bin/env python3
"""
Flask Web Application for TOTO Number Analysis
Provides an interactive HTML interface for analyzing TOTO lottery data.
"""

from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from datetime import datetime
import os

# Import our analysis modules
import clean_data
import toto_analysis
import backtest
import monte_carlo

app = Flask(__name__)

# Global variable to store current data
current_data = None
current_columns = None

def generate_plot():
    """Generate a matplotlib plot and return as base64 string"""
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight', dpi=150)
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/generate_data', methods=['POST'])
def generate_data():
    """Generate new simulated data"""
    global current_data, current_columns
    
    try:
        num_draws = int(request.form.get('num_draws', 1000))
        monte_carlo.monte_carlo_simulation(num_draws)
        
        # Load the generated data
        current_data, current_columns = clean_data.load_data('simulated_draws.csv')
        
        if current_data is None:
            return jsonify({'success': False, 'error': 'Failed to load generated data'})
        
        return jsonify({
            'success': True,
            'message': f'Generated {num_draws} draws successfully!',
            'rows': len(current_data),
            'columns': list(current_columns)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/load_data', methods=['POST'])
def load_data():
    """Load existing data file"""
    global current_data, current_columns
    
    try:
        filename = request.form.get('filename', 'simulated_draws.csv')
        current_data, current_columns = clean_data.load_data(filename)
        
        if current_data is None:
            return jsonify({'success': False, 'error': 'Failed to load data file'})
        
        return jsonify({
            'success': True,
            'message': f'Loaded data from {filename} successfully!',
            'rows': len(current_data),
            'columns': list(current_columns)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/analyze_frequency')
def analyze_frequency():
    """Generate frequency analysis plot"""
    global current_data
    
    if current_data is None:
        return jsonify({'success': False, 'error': 'No data loaded'})
    
    try:
        # Create frequency analysis
        plt.figure(figsize=(12, 6))
        toto_analysis.overall_frequency_chart(current_data)
        plot_url = generate_plot()
        
        # Get frequency statistics
        all_numbers = []
        for col in current_columns:
            all_numbers.extend(current_data[col].tolist())
        
        number_counts = pd.Series(all_numbers).value_counts().sort_index()
        
        return jsonify({
            'success': True,
            'plot': plot_url,
            'stats': {
                'total_numbers': len(all_numbers),
                'unique_numbers': len(number_counts),
                'most_frequent': number_counts.head(5).to_dict(),
                'least_frequent': number_counts.tail(5).to_dict()
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/analyze_positions')
def analyze_positions():
    """Generate position analysis plot"""
    global current_data, current_columns
    
    if current_data is None:
        return jsonify({'success': False, 'error': 'No data loaded'})
    
    try:
        # Create position analysis
        plt.figure(figsize=(12, 6))
        toto_analysis.individual_bar_chart(current_data, current_columns)
        plot_url = generate_plot()
        
        # Get position statistics
        position_stats = {}
        for i, col in enumerate(current_columns, 1):
            position_stats[f'Position {i}'] = {
                'mean': float(current_data[col].mean()),
                'std': float(current_data[col].std()),
                'min': int(current_data[col].min()),
                'max': int(current_data[col].max())
            }
        
        return jsonify({
            'success': True,
            'plot': plot_url,
            'stats': position_stats
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/analyze_grouped')
def analyze_grouped():
    """Generate grouped analysis plot"""
    global current_data, current_columns
    
    if current_data is None:
        return jsonify({'success': False, 'error': 'No data loaded'})
    
    try:
        # Create grouped analysis
        plt.figure(figsize=(12, 6))
        toto_analysis.grouped_bar_chart(current_data, current_columns)
        plot_url = generate_plot()
        
        return jsonify({
            'success': True,
            'plot': plot_url
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/analyze_confidence')
def analyze_confidence():
    """Generate confidence interval analysis"""
    global current_data
    
    if current_data is None:
        return jsonify({'success': False, 'error': 'No data loaded'})
    
    try:
        # Create confidence interval analysis
        plt.figure(figsize=(12, 6))
        toto_analysis.confidence_interval(current_data)
        plot_url = generate_plot()
        
        return jsonify({
            'success': True,
            'plot': plot_url
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/run_backtest')
def run_backtest():
    """Run backtest analysis"""
    global current_data
    
    if current_data is None:
        return jsonify({'success': False, 'error': 'No data loaded'})
    
    try:
        # Run backtest (we'll capture the output)
        import sys
        from io import StringIO
        
        # Redirect stdout to capture backtest output
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        
        try:
            backtest.backtest(current_data)
            backtest_output = result.getvalue()
        finally:
            sys.stdout = old_stdout
        
        return jsonify({
            'success': True,
            'output': backtest_output
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get_sample_data')
def get_sample_data():
    """Get sample data for display"""
    global current_data
    
    if current_data is None:
        return jsonify({'success': False, 'error': 'No data loaded'})
    
    try:
        sample_data = current_data.head(10).to_dict('records')
        return jsonify({
            'success': True,
            'data': sample_data
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/download_data')
def download_data():
    """Download current data as CSV"""
    global current_data
    
    if current_data is None:
        return jsonify({'success': False, 'error': 'No data loaded'})
    
    try:
        # Save to temporary file
        filename = f"toto_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        current_data.to_csv(filename, index=False)
        
        return send_file(filename, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Set matplotlib to use non-interactive backend
    plt.switch_backend('Agg')
    
    # Generate initial data if it doesn't exist
    if not os.path.exists('simulated_draws.csv'):
        monte_carlo.monte_carlo_simulation(1000)
    
    # Load initial data
    current_data, current_columns = clean_data.load_data('simulated_draws.csv')
    
    print("Starting TOTO Analysis Web Application...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)