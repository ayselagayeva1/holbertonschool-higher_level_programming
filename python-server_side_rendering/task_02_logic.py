#!/usr/bin/python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# --- Route to display items dynamically ---
@app.route('/items')
def items():
    items_file = 'items.json'

    # Default to empty list if file not found or empty
    items_list = []

    if os.path.exists(items_file):
        try:
            with open(items_file, 'r') as f:
                data = json.load(f)
                items_list = data.get('items', [])
        except json.JSONDecodeError:
            items_list = []

    return render_template('items.html', items=items_list)

# --- Run the server ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
