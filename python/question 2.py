import sqlite3

# Initialize the SQLite database and create tables for sales and customers
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create the Sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sales (
        sale_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        sale_date DATE,
        item_name TEXT,
        item_price REAL
    )
''')

# Create the Customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        email TEXT
    )
''')

# Function to record each sale
def record_sale(customer_id, sale_date, item_name, item_price):
    cursor.execute('''
        INSERT INTO Sales (customer_id, sale_date, item_name, item_price)
        VALUES (?, ?, ?, ?)
    ''', (customer_id, sale_date, item_name, item_price))
    conn.commit()

# Function to calculate total sales for a specific period
def calculate_total_sales(start_date, end_date):
    cursor.execute('''
        SELECT SUM(item_price)
        FROM Sales
        WHERE sale_date BETWEEN ? AND ?
    ''', (start_date, end_date))
    total_sales = cursor.fetchone()[0]
    return total_sales if total_sales else 0

# Function to provide personalized discounts to frequent customers
def provide_discount(customer_id):
    # You can implement your discount logic here
    pass

# Function to generate a report of the store's top customers and sales trends
def generate_sales_report():
    cursor.execute('''
        SELECT c.customer_name, SUM(s.item_price) as total_sales
        FROM Sales s
        JOIN Customers c ON s.customer_id = c.customer_id
        GROUP BY c.customer_name
        ORDER BY total_sales DESC
    ''')
    top_customers = cursor.fetchall()

    for customer in top_customers:
        print(f'{customer[0]}: ${customer[1]:.2f}')

if __name__ == '__main__':
    # Sample usage
    # Record a sale
    record_sale(1, '2023-10-26', 'Product 1', 100.0)
    record_sale(2, '2023-10-26', 'Product 2', 50.0)
    record_sale(1, '2023-10-27', 'Product 3', 75.0)

    # Calculate total sales for a specific period
    total = calculate_total_sales('2023-10-26', '2023-10-27')
    print(f'Total Sales: Rs{total:.2f}')

    # Provide personalized discounts to frequent customers
    provide_discount(1)

    # Generate a report of the store's top customers and sales trends
    generate_sales_report()

    # Close the database connection
    conn.close()
