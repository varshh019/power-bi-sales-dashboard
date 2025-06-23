import pandas as pd

# --- Sample Data Lists ---
# These lists must be consistent with generate_data.py
products = {
    'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 'Camera', 'Monitor', 'Keyboard'],
    'Furniture': ['Chair', 'Desk', 'Table', 'Sofa', 'Bed', 'Bookshelf'],
    'Office Supplies': ['Pens', 'Notebook', 'Stapler', 'Printer Ink', 'Paper'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Shoes', 'Socks']
}

manufacturers = {
    'Electronics': ['TechCorp', 'Gadgetron', 'ElectroWorks'],
    'Furniture': ['FineWood', 'ComfyLiving', 'UrbanDesigns'],
    'Office Supplies': ['OfficePro', 'PaperMakers', 'InkWell'],
    'Clothing': ['StyleWear', 'CottonCo', 'UrbanThreads']
}

# --- Data Generation ---
product_details = []

# Flatten the products dictionary and assign a random manufacturer from the correct category
all_products = [product for sublist in products.values() for product in sublist]

import random

for product_name in all_products:
    category = [cat for cat, prod_list in products.items() if product_name in prod_list][0]
    manufacturer = random.choice(manufacturers[category])
    product_details.append({
        'Product': product_name,
        'Manufacturer': manufacturer
    })

# --- Create DataFrame and Save to CSV ---
df_details = pd.DataFrame(product_details)
df_details.to_csv('product_details.csv', index=False)

print(f"Successfully generated 'product_details.csv' with {len(df_details)} records.") 