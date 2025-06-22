import pandas as pd
import random
from datetime import datetime, timedelta

# --- Configuration ---
NUM_RECORDS = 1000
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2023, 12, 31)

# --- Sample Data Lists ---
products = {
    'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 'Camera', 'Monitor', 'Keyboard'],
    'Furniture': ['Chair', 'Desk', 'Table', 'Sofa', 'Bed', 'Bookshelf'],
    'Office Supplies': ['Pens', 'Notebook', 'Stapler', 'Printer Ink', 'Paper'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Shoes', 'Socks']
}

regions = ['North', 'South', 'East', 'West']

# --- Data Generation ---
data = []

def get_random_date(start, end):
    """Generate a random datetime between `start` and `end`."""
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

for _ in range(NUM_RECORDS):
    category = random.choice(list(products.keys()))
    product = random.choice(products[category])
    region = random.choice(regions)
    
    # Generate a realistic sales price based on category
    if category == 'Electronics':
        price = round(random.uniform(50, 2000), 2)
    elif category == 'Furniture':
        price = round(random.uniform(100, 1500), 2)
    elif category == 'Clothing':
        price = round(random.uniform(10, 300), 2)
    else: # Office Supplies
        price = round(random.uniform(1, 100), 2)
        
    quantity = random.randint(1, 5)
    sale_date = get_random_date(START_DATE, END_DATE)

    data.append({
        'Date': sale_date.strftime('%Y-%m-%d'),
        'Category': category,
        'Product': product,
        'Price': price,
        'Quantity': quantity,
        'Sales': round(price * quantity, 2),
        'Region': region
    })

# --- Create DataFrame and Save to CSV ---
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)

print(f"Successfully generated 'sales_data.csv' with {NUM_RECORDS} records.") 