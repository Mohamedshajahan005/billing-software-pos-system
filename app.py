import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "simple_secret_key"

# ------------------ DB ------------------
def get_db_connection():
    conn = sqlite3.connect("database/billing.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            mrp REAL,
            selling_price REAL,
            unit TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_no INTEGER,
            bill_date TEXT,
            total REAL
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ------------------ Routes ------------------
@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin123":
            return redirect(url_for("billing"))
        return "Invalid Credentials"
    return render_template("login.html")

# ------------------ Billing ------------------
bill_counter = 1

@app.route("/billing", methods=["GET", "POST"])
def billing():
    global bill_counter
    
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    
    if request.method == "POST":
        items = request.form.getlist("item[]")
        quantities = request.form.getlist("quantity[]")
        prices = request.form.getlist("price[]")
        units = request.form.getlist("unit[]")

        bill = []
        grand_total = 0

        for i in range(len(items)):
            if not quantities[i] or not prices[i]:
                continue
            qty = float(quantities[i])
            price = float(prices[i])
            unit = units[i]

            if unit == "g":
                total = (qty / 1000) * price
            else:
                total = qty * price

            grand_total += total
            
            bill.append({
                "item": items[i],
                "quantity": qty,
                "unit": unit,
                "price": price,
                "total": round(total,2)
            })

        bill_no = bill_counter
        bill_counter += 1
        bill_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        
        return render_template("billing.html",
            products=products,
            bill=bill,
            grand_total = round(grand_total,2),
            bill_no=bill_no,
            bill_date=bill_date
        )

    return render_template("billing.html",
        products=products,
        bill=[],
        grand_total=0,
        bill_no=bill_counter,
        bill_date=datetime.now().strftime("%d-%m-%Y %H:%M")
    )

# ------------------ Product Master ------------------
@app.route("/products")
def products():
    conn = get_db_connection()
    prods = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return render_template("products.html", products=prods)

@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        mrp = float(request.form["mrp"])
        price = float(request.form["price"])
        unit = request.form["unit"]

        conn = get_db_connection()
        conn.execute(
            "INSERT OR IGNORE INTO products (name, mrp, selling_price, unit) VALUES (?, ?, ?, ?)",
            (name, mrp, price, unit)
        )
        conn.commit()
        conn.close()

        return redirect("/products")

    return render_template("add_product.html")

if __name__ == "__main__":
    app.run(debug=True)
