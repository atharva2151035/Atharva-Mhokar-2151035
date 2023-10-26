import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data (replace with your actual data)
data = {
    'Date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
    'Time': ['09:00', '11:30', '15:45', '10:15', '18:30'],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Price': [20, 15, 20, 10, 15],
}
df = pd.DataFrame(data)

# Convert the 'Date' column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Analyze sales trends over time
sales_over_time = df.groupby('Date')['Price'].sum()
sales_over_time.plot(kind='line', title='Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# Create data visualizations, such as sales charts
product_sales = df.groupby('Product')['Price'].sum()
product_sales.plot(kind='bar', title='Product Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Identify peak sales hours
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
peak_sales_hours = df.groupby('Time')['Price'].sum()
peak_sales_hours.plot(kind='bar', title='Peak Sales Hours')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Sales')
plt.show()

# Identify popular products
popular_products = product_sales.idxmax()
print(f'Most Popular Product: {popular_products}')

# Generate reports for store management
total_sales = df['Price'].sum()
average_sales_per_transaction = df['Price'].mean()
report = f"Total Sales: ${total_sales:.2f}\nAverage Sales per Transaction: ${average_sales_per_transaction:.2f}"
print(report)
