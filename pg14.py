import pandas as pd
data = {
    'customer_age': [25, 30, 35, 25, 40, 30, 35, 30, 45, 25, 35, 40]
}
sales_data = pd.DataFrame(data)
age_freq = sales_data['customer_age'].value_counts().reset_index()
age_freq.columns = ['Age', 'Frequency']
age_freq = age_freq.sort_values(by='Age')
print(age_freq)
