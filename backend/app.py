from flask import Flask, request, jsonify
from flask_cors import CORS
from data_processing.excel_reader import read_excel_file
from nlp.intent_parser import parse_intent
from code_generation.pandas_generator import generate_pandas_code
from code_generation.matplotlib_generator import generate_matplotlib_code
from code_generation.numpy_generator import generate_numpy_code
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and file.filename.endswith('.xlsx'):
        df = read_excel_file(file)
        return jsonify({'message': 'File uploaded successfully', 'columns': df.columns.tolist()}), 200
    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/generate_code', methods=['POST'])
def generate_code():
    data = request.json
    intent = data.get('intent')
    df = pd.read_json(data.get('data'))
    
    parsed_intent = parse_intent(intent)
    
    code = ""
    if parsed_intent['library'] == 'pandas':
        code = generate_pandas_code(parsed_intent, df)
    elif parsed_intent['library'] == 'matplotlib':
        code = generate_matplotlib_code(parsed_intent, df)
    elif parsed_intent['library'] == 'numpy':
        code = generate_numpy_code(parsed_intent, df)
    
    result = None
    if parsed_intent['library'] == 'matplotlib':
        plt.clf()  # Clear the current figure
        exec(code)
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        result = base64.b64encode(img.getvalue()).decode()
    else:
        result = eval(code)
    
    explanation = generate_explanation(code)
    
    return jsonify({
        'code': code,
        'result': result,
        'explanation': explanation
    })

def generate_explanation(code):
    # This function would generate an explanation for the code
    # For now, we'll return a placeholder
    return "This code uses pandas/matplotlib/numpy to process and visualize your data. [Detailed explanation to be implemented]"

if __name__ == '__main__':
    app.run(debug=True)