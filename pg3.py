import numpy as np
house_data = np.array([
    [5, 2000, 250000],
    [4, 1800, 220000],
    [6, 2200, 280000],
    [3, 1600, 180000],
    [5, 2100, 260000]
])
bedroom_condition = house_data[:, 0] > 4  
houses_more_than_four_bedrooms = house_data[bedroom_condition]
average_sale_price = np.mean(houses_more_than_four_bedrooms[:, 2])  

print("Average Sale Price of Houses with More than Four Bedrooms:", average_sale_price)
