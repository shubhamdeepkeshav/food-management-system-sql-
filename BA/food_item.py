# food_item.py

import mysql.connector
from DBConnection import get_connection  # Make sure your db_connection.py has a function that returns a connection

# 1. Add Food Item
def add_food_item():
    conn = get_connection()
    cur = conn.cursor()
    item_name = input("Enter Food Item Name: ")
    unit_price = float(input("Enter Unit Price: "))
    stock_kg = float(input("Enter Stock (in kg): "))
    cur.execute("INSERT INTO food_item (item_name, unit_price, stock_kg) VALUES (%s, %s, %s)",
                (item_name, unit_price, stock_kg))
    conn.commit()
    print("✅ Food item added successfully!")
    conn.close()

# 2. View All Food Items
def view_food_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM food_item")
    records = cur.fetchall()
    print("\n===== FOOD ITEMS LIST =====")
    for row in records:
        print(row)
    conn.close()

# 3. Update Food Item
def update_food_item():
    conn = get_connection()
    cur = conn.cursor()
    item_id = int(input("Enter Food Item ID to Update: "))
    new_name = input("Enter New Item Name: ")
    new_price = float(input("Enter New Unit Price: "))
    new_stock = float(input("Enter New Stock (in kg): "))
    cur.execute("UPDATE food_item SET item_name=%s, unit_price=%s, stock_kg=%s WHERE id=%s",
                (new_name, new_price, new_stock, item_id))
    conn.commit()
    print("✅ Food item updated successfully!")
    conn.close()

# 4. Delete Food Item
def delete_food_item():
    conn = get_connection()
    cur = conn.cursor()
    item_id = int(input("Enter Food Item ID to Delete: "))
    cur.execute("DELETE FROM food_item WHERE id=%s", (item_id,))
    conn.commit()
    print("✅ Food item deleted successfully!")
    conn.close()
