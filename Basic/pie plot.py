import matplotlib.pyplot as plt

categories = ['Rent', 'Utilities', 'Groceries', 'Entertainment']
expense = [1200, 300, 400, 200]
explode = (0.1, 0, 0, 0)

plt.figure(figsize=(8,8))
plt.pie(expense, explode=explode, labels=categories, autopct='%1.1f%%',startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
plt.title('Expense Distribution with Emphasized Largest Category')
plt.show()