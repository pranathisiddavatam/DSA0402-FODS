import numpy as np
fuel_efficiency = np.array([30.5, 28.2, 35.8, 32.0, 30.5, 29.8])
average_fuel_efficiency = np.mean(fuel_efficiency)
model_2_efficiency = fuel_efficiency[1]  
model_5_efficiency = fuel_efficiency[4] 
percentage_improvement = ((model_5_efficiency - model_2_efficiency) / model_2_efficiency) * 100
print("Average Fuel Efficiency:", average_fuel_efficiency, "MPG")
print("Percentage Improvement between Model 2 and Model 5:", percentage_improvement, "%")
OUTPUT:
Average Fuel Efficiency: 31.133333333333336 MPG
Percentage Improvement between Model 2 and Model 5: 8.156028368794328 %
