invnt = [ ("Fruits", "Apple", 150, 250, "Fresh Farms"),
        ( "Fruits", "Banana", 200, 120, "Organic Suppliers"),
        ( "Fruits", "Orange", 180, 230, "Citrus Co."),
        ( "Fruits", "Mango", 100, 500, "Tropical Exports"),
        ( "Vegetables", "Potato", 300, 80, "Green Fields"),
        ( "Vegetables", "Onion", 250, 100, "Local Farmers"),
        ( "Vegetables", "Tomato", 180, 150, "Red Farm Co."),
        ( "Dairy", "Milk (1L)", 400, 180, "DairyBest"),
        ( "Dairy", "Cheese (500g)", 150, 700, "CheeseWorks"),
        ( "Dairy", "Yogurt (500g)", 200, 160, "DairyBest"),
        ( "Bakery", "Bread (500g)", 250, 120, "Bakers Delight"),
        ( "Bakery", "Croissant", 100, 200, "Bakers Delight"),
        ( "Bakery", "Cake", 50, 1200, "Sweet Treats"),
        ( "Meat", "Chicken (1kg)", 100, 750, "Poultry Farms"),
        ( "Meat", "Beef (1kg)", 80, 1200, "Butcher's Choice"),
        ( "Meat", "Mutton (1kg)", 50, 2000, "Premium Meats"),
        ( "Beverages", "Coca-Cola (1.5L)", 300, 180, "Coca-Cola Co."),
        ( "Beverages", "Pepsi (1.5L)", 280, 175, "PepsiCo"),
        ( "Beverages", "Juice (1L)", 200, 250, "Juicy Delights"),
        ( "Frozen", "Frozen Peas (500g)", 150, 400, "Frozen Foods Ltd."),
        ( "Frozen", "Ice Cream (1L)", 200, 850, "Cold Treats"),
        ( "Snacks", "Chips (150g)", 300, 150, "Crunchy Bites"),
        ( "Snacks", "Chocolate (100g)", 250, 300, "Sweet Cocoa"),
        ( "Snacks", "Biscuits (300g)", 400, 180, "Golden Biscuits"),
        ( "Household", "Dishwashing Liquid (1L)", 150, 500, "Clean Homes"),
        ( "Household", "Laundry Detergent (2kg)", 200, 850, "Fresh Clothes"),
        ( "Household", "Tissue Box", 300, 120, "Soft Touch"),
        ( "Canned Goods", "Baked Beans (400g)", 100, 350, "Canned Delights"),
        ( "Canned Goods", "Tuna (200g)", 150, 450, "Seafood Co."),
        ( "Canned Goods", "Corn (400g)", 200, 300, "Farm Fresh"),
        ( "Personal Care", "Shampoo (500ml)", 200, 700, "HairCare Ltd."),
        ( "Personal Care", "Soap (100g)", 400, 120, "Glow Skincare"),
        ( "Personal Care", "Toothpaste (150g)", 250, 300, "Dental Fresh"),
        ( "Spices", "Black Pepper (100g)", 150, 400, "Spice World"),
        ( "Spices", "Salt (1kg)", 500, 80, "Himalayan Salt Co."),
        ( "Spices", "Turmeric Powder (250g)", 180, 350, "Golden Spices"),
        ( "Grains", "Rice (5kg)", 250, 1500, "Rice Mills"),
        ( "Grains", "Wheat Flour (5kg)", 300, 1200, "Farm Fresh"),
        ( "Grains", "Lentils (1kg)", 200, 600, "Pulse Exports"),
        ( "Baby Care", "Baby Diapers (Pack of 30)", 100, 1800, "Baby Comfort"),
        ( "Baby Care", "Baby Powder (500g)", 150, 400, "Gentle Baby"),
        ( "Pet Supplies", "Dog Food (2kg)", 100, 2500, "Pet Nutrition"),
        ( "Pet Supplies", "Cat Food (1.5kg)", 120, 2200, "Feline Feast"),
        ( "Electronics", "LED Bulb (10W)", 300, 600, "Bright Lights"),
        ( "Electronics", "Battery (AA, Pack of 4)", 250, 300, "PowerCharge"),
        ( "Medicines", "Paracetamol (500mg, Pack of 10)", 200, 150, "HealthFirst"),
        ( "Medicines", "Vitamin C Tablets (Pack of 30)", 150, 600, "Wellness Co."),
        ( "Kitchen Essentials", "Cooking Oil (1L)", 250, 700, "Pure Oils"),
        ( "Kitchen Essentials", "Sugar (2kg)", 300, 900, "Sweet Source"),
        ( "Kitchen Essentials", "Tea (500g)", 200, 500, "Tea Gardens"),
    ]


import sqlite3 as sql
import os
import platform
conn = sql.connect('inventory_table.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS inventory_table(category TEXT,
                        item_name TEXT,
                        Quant INTEGER,
                        price REAL,
                        Supplier TEXT)""")

def initialize_database():
    cursor.executemany("INSERT OR REPLACE INTO inventory_table VALUES(?,?,?,?,?)", invnt)
    cursor.execute("SELECT rowid,* from inventory_table")

def clear_screen():
    system_name = platform.system()
    if system_name == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def show_database():
    clear_screen()
    cursor.execute("SELECT rowid,* from inventory_table")
    results = cursor.fetchall()
    header = f"{'ID':<5} {'Category':<15} {'Product':<35} {'Quantity':<10} {'Price (PKR)':<12} {'Supplier':<25}"
    print("=" * len(header))
    print(header)
    print("=" * len(header))

    current_category = ""
    for item in results:
        if item[1] != current_category:
            print("\n" + "-" * 80)
            current_category = item[1]
            print(f"{'Category:':<10} | {item[1]:<70} |")
            print("-" * 80)

        print(f"{item[0]:<5} | {item[2]:<35} | {item[3]:<10} | {item[4]:<12} | {item[5]:<25} |")

    print("=" * len(header))

def stock_decrease(p_nt, dec):
    cursor.execute("SELECT * FROM inventory_table WHERE item_name = ?", (p_nt,))
    cursor.execute("UPDATE inventory_table SET Quant = Quant-? WHERE item_name = ?", (dec, p_nt))
    conn.commit()
    if dec <= 0:
        print("Enter A Valid Quantity")
    elif dec == 1:
        print(f"{dec} {p_nt} Was Removed From Stock")
    else:
        print(f"{dec} {p_nt} Were Removed From Stock")

def increase_stock(p_nt, inc):
    cursor.execute("SELECT * FROM inventory_table WHERE item_name = ?", (p_nt,))
    cursor.execute("UPDATE inventory_table SET Quant = Quant + ? WHERE item_name = ?", (inc, p_nt))
    conn.commit()
    if inc <= 0:
        print("Enter A Valid Quantity")
    elif inc == 1:
        print(f"{inc} {p_nt} Was Added To Stock")
    else:
        print(f"{inc} {p_nt} Were Added To Stock")

def add_item(category: str, item_name: str, Quant: int, price: float, supplier: str):
    if not isinstance(category, str) or not isinstance(item_name, str) or not isinstance(supplier, str):
        print("Please enter string values for category, item_name, and supplier.")
        return
    if not isinstance(Quant, int) or Quant <= 0:
        print("Enter a valid integer value for Quantity (must be greater than 0).")
        return
    if not isinstance(price, (int, float)) or price <= 0:
        print("Enter a valid price (must be a positive number).")
        return

    cursor.execute("INSERT INTO inventory_table VALUES (?, ?, ?, ?, ?)", (category, item_name, Quant, price, supplier))
    conn.commit()
    print(f"Item '{item_name}' added successfully to inventory.")

def remove_item(categor: str, item_nam: str, Quan: int, pric: float, supplie: str):
    if not isinstance(categor, str) or not isinstance(item_nam, str) or not isinstance(supplie, str):
        print("Please Enter String Values In Parameter")
        return
    if not isinstance(Quan, int):
        print("Enter an integer value for Quantity ")
        return
    if not isinstance(pric, float):
        print("Please enter a float value for price")
        return
    cursor.execute("DELETE from inventory_table WHERE category = ? AND item_name = ? AND Quant = ? AND price = ? AND supplier = ? ", (categor, item_nam, Quan, pric, supplie))
    conn.commit()
    if cursor.rowcount == 0:
        print("Item Was Not Found")
    else:
        print("Item Was Deleted")

def threshold():
    threshold = 50
    cursor.execute("SELECT * from inventory_table WHERE Quant < ?", (threshold,))
    items = cursor.fetchall()
    if len(items) > 0:
        print("-" * 24)
        print("Item Name         Quantity")
        for item in items:
            print(f"{item[0]:<20}{item[2]:<20}")
    else:
        print("Each Item Is Above The Threshold Limit")
cursor.execute("SELECT COUNT(*) FROM inventory_table")
if cursor.fetchone()[0] == 0:
    initialize_database()
while True:
    print("\nWelcome to the Inventory Management System")
    print("1. Show Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Increase Stock")
    print("5. Decrease Stock")
    print("6. View Low Stock Items")
    print("7. Exit")
    
    choice = input("Please enter your choice: ")

    if choice == '1':
        show_database()
    elif choice == '2':
        category = input("Enter category: ")
        item_name = input("Enter item name: ")
        Quant = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        supplier = input("Enter supplier: ")
        add_item(category, item_name, Quant, price, supplier)
    elif choice == '3':
        categor = input("Enter category: ")
        item_nam = input("Enter item name: ")
        Quan = int(input("Enter quantity: "))
        pric = float(input("Enter price: "))
        supplie = input("Enter supplier: ")
        remove_item(categor, item_nam, Quan, pric, supplie)
    elif choice == '4':
        p_nt = input("Enter product name: ")
        inc = int(input("Enter quantity to add: "))
        increase_stock(p_nt, inc)
    elif choice == '5':
        p_nt = input("Enter product name: ")
        dec = int(input("Enter quantity to remove: "))
        stock_decrease(p_nt, dec)
    elif choice == '6':
        threshold()
    elif choice == '7':
        break
    else:
        print("Invalid choice, please try again.")











