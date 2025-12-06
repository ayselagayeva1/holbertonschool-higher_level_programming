from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- JSON oxuma funksiyası ---
def read_json():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# --- CSV oxuma funksiyası ---
def read_csv():
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except FileNotFoundError:
        return []

# --- SQLite oxuma funksiyası ---
def read_sqlite():
    products = []
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
        return products
    except sqlite3.Error as e:
        print("Database error:", e)
        return []

# --- Flask route ---
@app.route("/products")
def products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    elif source == "sql":
        data = read_sqlite()
    else:
        return render_template("product_display.html", error="Wrong source", products=[])

    # id filtrini tətbiq edirik
    if id_param:
        try:
            id_val = int(id_param)
            filtered = [item for item in data if item.get("id") == id_val]
            if not filtered:
                return render_template("product_display.html", error="Product not found", products=[])
            return render_template("product_display.html", products=filtered)
        except ValueError:
            return render_template("product_display.html", error="Invalid id", products=[])

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
