import pandas as pd
data = {
    'Customer ID': [101, 102, 103, 104],
    'Order Date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04'],
    'Product Name': ['Product A', 'Product B', 'Product A', 'Product C'],
    'Order Quantity': [2, 1, 3, 2]
}
order_data = pd.DataFrame(data)
customer_order_counts = order_data['Customer ID'].value_counts()
print("Total number of orders made by each customer:\n", customer_order_counts)
average_order_quantity_per_product = order_data.groupby('Product Name')['Order Quantity'].mean()
print("Average order quantity for each product:\n", average_order_quantity_per_product)
earliest_order_date = order_data['Order Date'].min()
latest_order_date = order_data['Order Date'].max()
print("Earliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
OUTPUT:
Total number of orders made by each customer:
 Customer ID
101    1
102    1
103    1
104    1
Name: count, dtype: int64
Average order quantity for each product:
 Product Name
Product A    2.5
Product B    1.0
Product C    2.0
Name: Order Quantity, dtype: float64
Earliest Order Date: 2023-08-01
Latest Order Date: 2023-08-04
