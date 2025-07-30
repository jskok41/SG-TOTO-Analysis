from flask import Flask, render_template, request, jsonify, send_file
import os
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import clean_data
import toto_analysis
import monte_carlo
import backtest

app = Flask(__name__)

# Global variable to store current data
current_data = None
current_column_names = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_data', methods=['POST'])
def load_data():
    global current_data, current_column_names
    
    data_type = request.form.get('data_type')
    
    if data_type == 'real':
        file = "toto_results.csv"
    else:
        # Generate simulated data if it doesn't exist
        if not os.path.exists("simulated_draws.csv"):
            monte_carlo.monte_carlo_simulation(10000)
        file = "simulated_draws.csv"
    
    try:
        results, column_names = clean_data.load_data(file)
        
        if results is None or column_names is None:
            return jsonify({'error': 'Failed to load data'})
        
        if data_type == 'real':
            current_data = clean_data.clean_data(results)
        else:
            current_data = results
            
        current_column_names = column_names
        
        return jsonify({
            'success': True,
            'message': f'Data loaded successfully. {len(current_data)} records found.',
            'data_type': data_type
        })
    except Exception as e:
        return jsonify({'error': f'Error loading data: {str(e)}'})

@app.route('/analyze', methods=['POST'])
def analyze():
    global current_data, current_column_names
    
    if current_data is None:
        return jsonify({'error': 'No data loaded. Please load data first.'})
    
    analysis_type = request.form.get('analysis_type')
    
    try:
        if analysis_type == 'individual_bar':
            return generate_chart('individual_bar')
        elif analysis_type == 'grouped_bar':
            return generate_chart('grouped_bar')
        elif analysis_type == 'overall_frequency':
            return generate_chart('overall_frequency')
        elif analysis_type == 'confidence_interval':
            return generate_chart('confidence_interval')
        elif analysis_type == 'backtest':
            return generate_backtest()
        else:
            return jsonify({'error': 'Invalid analysis type'})
    except Exception as e:
        return jsonify({'error': f'Error during analysis: {str(e)}'})

def generate_chart(chart_type):
    plt.figure(figsize=(12, 8))
    
    if chart_type == 'individual_bar':
        toto_analysis.individual_bar_chart(current_data, current_column_names)
    elif chart_type == 'grouped_bar':
        toto_analysis.grouped_bar_chart(current_data, current_column_names)
    elif chart_type == 'overall_frequency':
        toto_analysis.overall_frequency_chart(current_data)
    elif chart_type == 'confidence_interval':
        toto_analysis.confidence_interval(current_data)
    
    # Convert plot to base64 string
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight', dpi=300)
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return jsonify({
        'success': True,
        'image': plot_url,
        'analysis_type': chart_type
    })

def generate_backtest():
    # For web version, we'll use a simplified backtest that returns results
    try:
        # Use the most frequent numbers as prediction
        all_numbers = []
        for col in ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6']:
            if col in current_data.columns:
                all_numbers.extend(current_data[col].tolist())
        
        # Get frequency of each number
        number_counts = {}
        for num in all_numbers:
            if pd.notna(num):
                number_counts[num] = number_counts.get(num, 0) + 1
        
        # Get top 6 most frequent numbers
        predicted_numbers = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)[:6]
        predicted_numbers = [num for num, count in predicted_numbers]
        
        # Simple backtest
        matches = []
        winners = 0
        c_3 = c_4 = c_5 = c_6 = 0
        
        for idx, row in current_data.iterrows():
            row_numbers = [row[col] for col in ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6'] if col in current_data.columns and pd.notna(row[col])]
            matched = [num for num in row_numbers if num in predicted_numbers]
            match_count = len(matched)
            matches.append(match_count)
            
            if match_count >= 3:
                winners += 1
            
            if match_count == 3:
                c_3 += 1
            elif match_count == 4:
                c_4 += 1
            elif match_count == 5:
                c_5 += 1
            elif match_count == 6:
                c_6 += 1
        
        avg_hits = np.mean(matches)
        
        results = {
            'predicted_numbers': predicted_numbers,
            'total_draws': len(current_data),
            'average_hits': round(avg_hits, 2),
            'winning_draws': winners,
            'win_rate': round((winners / len(current_data)) * 100, 2),
            'match_counts': {
                '3_correct': c_3,
                '4_correct': c_4,
                '5_correct': c_5,
                '6_correct': c_6
            }
        }
        
        return jsonify({
            'success': True,
            'results': results,
            'analysis_type': 'backtest'
        })
    except Exception as e:
        return jsonify({'error': f'Error in backtest: {str(e)}'})

@app.route('/generate_simulation', methods=['POST'])
def generate_simulation():
    try:
        num_draws = int(request.form.get('num_draws', 10000))
        monte_carlo.monte_carlo_simulation(num_draws)
        
        return jsonify({
            'success': True,
            'message': f'Generated {num_draws} simulated draws'
        })
    except Exception as e:
        return jsonify({'error': f'Error generating simulation: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)