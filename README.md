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
