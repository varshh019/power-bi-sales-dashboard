import requests
import json
import random
import time
from datetime import datetime

# --- Configuration ---
# PASTE YOUR POWER BI PUSH URL HERE
PUSH_URL = 'https://api.powerbi.com/beta/d60671b2-03a8-4a43-bde0-68c241b30050/datasets/d0bb0569-e964-4908-a036-7aaf967c58b1/rows?experience=power-bi&key=MWO1W90MKxR%2FlfGYGujeEZ4PA00h3a7D0I90D1x7GtMIkuuLX9l%2FkA8CS%2BcAsVSbwH5Q7nqxt1P%2FE%2BsghKZ9LQ%3D%3D'

# Sample product list
products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 'Camera', 'Monitor', 'Keyboard',
            'Chair', 'Desk', 'Table', 'Sofa', 'Bed', 'Bookshelf', 'Pens', 'Notebook', 'Stapler', 
            'Printer Ink', 'Paper', 'T-Shirt', 'Jeans', 'Jacket', 'Shoes', 'Socks']

# --- Main Loop ---
print("Starting real-time data stream to Power BI...")
print("Press Ctrl+C to stop.")

while True:
    try:
        # Generate random data
        product_sold = random.choice(products)
        sales_amount = round(random.uniform(5.00, 500.00), 2)
        current_time = datetime.now().isoformat()

        # Create the payload in the format Power BI expects (a list of dictionaries)
        data = [{
            "product": product_sold,
            "sales": sales_amount,
            "timestamp": current_time
        }]

        # Post the data to the Power BI API
        response = requests.post(PUSH_URL, json=data)

        # Check for a successful post
        if response.status_code == 200:
            print(f"Data pushed successfully: {product_sold}, Sales: ${sales_amount}")
        else:
            print(f"Error pushing data: {response.status_code} - {response.text}")

        # Wait for a few seconds before sending the next data point
        time.sleep(3)

    except KeyboardInterrupt:
        print("\nStream stopped by user.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break 