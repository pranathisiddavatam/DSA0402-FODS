import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [10000, 12000, 11000, 13000, 14000, 16000, 17000, 15000, 13000, 12000, 11000, 10000]
plt.figure(figsize=(10, 6))  
plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')  
plt.title('Monthly Sales Data')  
plt.xlabel('Month')  
plt.ylabel('Sales') 
plt.legend()  
plt.grid(True)  
plt.show()
plt.figure(figsize=(10, 6))  
plt.bar(months, sales, color='b', label='Monthly Sales') 
plt.title('Monthly Sales Data') 
plt.xlabel('Month')  
plt.ylabel('Sales') 
plt.legend() 
plt.grid(axis='y') 
plt.show()  
 OUTPUT:
C:\Users\DELL\OneDrive\Documents\New folder\10i.png
