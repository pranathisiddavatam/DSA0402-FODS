import pandas as pd
data = {
    'Product Name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product D', 'Product E', 'Product F', 'Product C', 'Product E'],
    'Quantity Sold': [10, 5, 8, 12, 6, 15, 9, 7, 8, 9]
}
sales_data = pd.DataFrame(data)
product_sales = sales_data.groupby('Product Name')['Quantity Sold'].sum()
top_5_products = product_sales.sort_values(ascending=False).head(5)
print("Top 5 products sold the most in the past month:")
print(top_5_products)
