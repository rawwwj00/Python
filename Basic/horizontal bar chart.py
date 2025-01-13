import matplotlib.pyplot as plt 
categories = ['Mathematics' , 'Physics' , 'Chemistry', 'Biology' , 'Computer Science' ]
values = [120,85,75,90,150]

plt.bar(categories , values , color ='skyblue')
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Horizontal Bar Chart Example')
plt.show()