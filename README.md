# Billing Software / POS System (Flask)

## Overview
A web-based Billing and Point of Sale (POS) system developed using Python Flask for small retail shops.  
The system supports product management, billing, and invoice generation with a simple and clean user interface.

## Features
- Secure shop login (Admin)
- Product Master module
  - Add products with MRP, selling price, and unit
  - View product list
- Billing module
  - Add multiple items to bill
  - Automatic bill number and date generation
  - Receipt-style invoice layout
- SQLite database integration
- Clean and lightweight UI

## Technology Stack
- Python
- Flask
- HTML, CSS
- SQLite

## Screenshots

### Login Page
![Login](screenshots/login.png)

### Add Product
![Add Product](screenshots/add_product.png)

### Product Master
![Product Master](screenshots/product_master.png)

### Billing Page
![Billing](screenshots/billing.png)

## Project Structure

billing-software-pos-system/
├── app.py
├── database/
│ └── billing.db
├── templates/
├── static/
│ └── style.css
└── screenshots/


## How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/billing-software-pos-system.git

css
Copy code
2. Navigate to project folder
cd billing-software-pos-system

markdown
Copy code
3. Install dependencies
pip install -r requirements.txt

markdown
Copy code
4. Run the application
python app.py

css
Copy code
5. Open browser and go to:
http://127.0.0.1:5000/login

markdown
Copy code

## Use Case
Designed for grocery shops, retail stores, and small businesses to manage products and generate bills digitally.

## Future Enhancements
- Sales reports & analytics
- User roles (Cashier / Admin)
- GST & tax calculation
- Invoice PDF download
- Cloud database support

## Author
Mohamed Shajahan
