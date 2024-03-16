from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-data', methods=['POST'])
def generate_data():
    if request.method == 'POST':
        # Get form data
        rows = int(request.form['rows'])
        columns = []
        for i in range(1, 6):  # Assuming a maximum of 5 columns
            column_name = request.form.get(f'columns_{i}', None)
            data_type = request.form.get(f'column_{i}_data_type', None)
            if column_name and data_type:
                columns.append({'name': column_name, 'data_type': data_type})

        # Generate dummy data using pandas and numpy
        dummy_data = {}
        for column in columns:
            if column['data_type'] == 'int':
                dummy_data[column['name']] = np.random.randint(0, 100, size=rows)
            elif column['data_type'] == 'decimal':
                dummy_data[column['name']] = np.random.rand(rows)
            elif column['data_type'] == 'text':
                dummy_data[column['name']] = ['dummy_text'] * rows  # Replace with AI generated text
            elif column['data_type'] == 'full_names':
                dummy_data[column['name']] = ['John Doe'] * rows  # Replace with full names generator
        
        # Create DataFrame
        df = pd.DataFrame(dummy_data)

        # Export DataFrame to CSV
        file_path = 'dummy_data.csv'
        df.to_csv(file_path, index=False)

        # Send file for download
        response = send_file(file_path, as_attachment=True)

        # Delete file from system
        # os.remove(file_path)

        return response

if __name__ == '__main__':
    app.run(debug=True)
