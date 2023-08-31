item_prices = [2.5, 1.0, 3.0, 4.5] 
item_quantities = [3, 2, 1, 4]      
discount_rate = 10 
tax_rate = 7.5     
total_cost_before_discount = sum([price * quantity for price, quantity in zip(item_prices, item_quantities)])
discount = (discount_rate / 100) * total_cost_before_discount
total_cost_after_discount = total_cost_before_discount - discount
tax_amount = (tax_rate / 100) * total_cost_after_discount
final_total_cost = total_cost_after_discount + tax_amount
print("Total Cost Before Discount: $", total_cost_before_discount)
print("Discount Amount: $", discount)
print("Total Cost After Discount: $", total_cost_after_discount)
print("Tax Amount: $", tax_amount)
print("Final Total Cost: $", final_total_cost)
OUTPUT:
Total Cost Before Discount: $ 30.5
Discount Amount: $ 3.0500000000000003
Total Cost After Discount: $ 27.45
Tax Amount: $ 2.05875
Final Total Cost: $ 29.50875
