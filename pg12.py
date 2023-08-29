import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rainfall = [50, 45, 60, 80, 100, 120, 130, 110, 90, 80, 70, 60]
temperature = [10, 12, 15, 18, 22, 26, 29, 28, 25, 20, 15, 12]
plt.figure(figsize=(10, 6))  
plt.plot(months, temperature, marker='o', linestyle='-', color='b', label='Temperature (°C)')
plt.title('Monthly Temperature Data')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))  
plt.scatter(months, rainfall, color='g', label='Rainfall (mm)', marker='o')
plt.title('Monthly Rainfall Data')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.grid(True)
plt.show()
