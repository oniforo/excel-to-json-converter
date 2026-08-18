import json
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
import pandas

load_dotenv()

app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    return render_template('upload.html')

# Define the route for handling the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request
    uploaded_file = request.files['file']

    if uploaded_file.filename.endswith('.xlsx'):
        # Process the file using a function that returns JSON results
        results = process_file(uploaded_file)
        return json.loads(results)

    return {
        'error': 'File is not an Excel spreadsheet.',
        'filename': uploaded_file.filename
    }

def process_file(file):
    # Add your file processing logic here
    df = pandas.read_excel(file)
    json_data = df.to_json(orient="records", force_ascii=False)
    return json_data

if __name__ == '__main__':
    app.run(
        debug=True, host="0.0.0.0",
        port=int(os.environ.get('PORT', 8080))
    )
