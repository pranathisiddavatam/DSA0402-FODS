import pandas as pd
import scipy.stats as stats
data = pd.DataFrame({
    'Product': ['Laptop', 'Headphones', 'Phone', 'Sneakers', 'Dress', 'Book', 'Tablet', 'Shoes',
                'Smartwatch', 'Camera', 'Backpack', 'Watch', 'Speaker', 'Headset', 'Guitar', 'Ebook', 'Handbag'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Fashion', 'Fashion', 'Books', 'Electronics', 'Fashion',
                 'Electronics', 'Electronics', 'Fashion', 'Fashion', 'Electronics', 'Electronics', 'Music', 'Books', 'Fashion'],
    'Rating': [4.5, 4.2, 4.8, 4.6, 4.0, 4.3, 4.7, 4.5, 4.4, 4.9, 4.2, 4.7, 4.3, 4.6, 4.8, 4.5, 4.1]
})
product_category = 'Electronics'  
category_reviews = data[data['Category'] == product_category]
sample_mean = category_reviews['Rating'].mean()
sample_std = category_reviews['Rating'].std()
sample_size = len(category_reviews)
confidence_level = 0.95
t_critical = stats.t.ppf((1 + confidence_level) / 2, df=sample_size - 1)
margin_of_error = t_critical * (sample_std / (sample_size ** 0.5))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(f"Sample Mean Rating for {product_category}: {sample_mean:.2f}")
print(f"Confidence Interval ({confidence_level * 100}%): ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
