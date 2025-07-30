from flask import Flask, render_template, request, jsonify, send_file
import clean_data
import toto_analysis
import monte_carlo
import backtest
import plotly.graph_objs as go
import plotly.utils
import json
import os
import io
import base64
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    analysis_type = data.get('type')
    data_source = data.get('data_source', 'toto_results.csv')
    
    try:
        # Load data
        results, column_names = clean_data.load_data(data_source)
        
        if results is None or column_names is None:
            return jsonify({'error': 'Failed to load data'}), 400
        
        # Clean data if using real TOTO results
        if data_source == "toto_results.csv":
            clean_results = clean_data.clean_data(results)
        else:
            clean_results = results
        
        # Generate plot based on analysis type
        if analysis_type == 'individual_bar':
            fig = toto_analysis.individual_bar_chart(clean_results, column_names, return_fig=True)
        elif analysis_type == 'grouped_bar':
            fig = toto_analysis.grouped_bar_chart(clean_results, column_names, return_fig=True)
        elif analysis_type == 'overall_frequency':
            fig = toto_analysis.overall_frequency_chart(clean_results, return_fig=True)
        elif analysis_type == 'confidence_interval':
            fig = toto_analysis.confidence_interval(clean_results, return_fig=True)
        elif analysis_type == 'backtest':
            fig = backtest.backtest(clean_results, return_fig=True)
        elif analysis_type == 'backtest_positional':
            position_ranges = [[1, 5], [7, 16], [16, 25], [25, 34], [35, 44], [40, 49]]
            fig = backtest.backtest_with_position_ranges(clean_results, position_ranges, return_fig=True)
        else:
            return jsonify({'error': 'Invalid analysis type'}), 400
        
        # Convert matplotlib figure to base64 string
        img = io.BytesIO()
        fig.savefig(img, format='png', bbox_inches='tight', dpi=300)
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close(fig)
        
        return jsonify({'plot': plot_url})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate_simulation', methods=['POST'])
def generate_simulation():
    data = request.get_json()
    num_draws = data.get('num_draws', 100000)
    
    try:
        monte_carlo.monte_carlo_simulation(num_draws)
        return jsonify({'message': f'Generated {num_draws} simulated draws'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)