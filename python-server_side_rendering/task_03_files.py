from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# JSON oxuma funksiyası
def read_json():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# CSV oxuma funksiyası
def read_csv():
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # price və id tiplərini düzəldirik
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except FileNotFoundError:
        return []

@app.route("/products")
def products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
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
