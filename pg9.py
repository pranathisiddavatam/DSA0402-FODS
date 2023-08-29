import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'number_of_bedrooms': [3, 2, 5, 3, 5],
    'area_sqft': [1500, 1200, 1800, 1600, 2200],
    'listing_price': [250000, 180000, 320000, 275000, 420000]
}
property_data = pd.DataFrame(data)
average_price_by_location = property_data.groupby('location')['listing_price'].mean()
properties_with_more_than_four_bedrooms = len(property_data[property_data['number_of_bedrooms'] > 4])
property_with_largest_area = property_data[property_data['area_sqft'] == property_data['area_sqft'].max()]
print("Average Listing Price by Location:")
print(average_price_by_location)
print("\nNumber of Properties with More than Four Bedrooms:", properties_with_more_than_four_bedrooms)
print("\nProperty with the Largest Area:")
print(property_with_largest_area)
