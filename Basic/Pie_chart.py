import matplotlib.pyplot as plt

branches = ['CSE Core', 'CSE (Specialization)', 'Integrated MTech','Other Branches']
number = [40, 30, 20, 10] 
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'] 
shadow = True
autopct = '%1.1f%%'

plt.figure(figsize=(8, 6)) 
plt.pie(
    number,
    labels=branches,
    colors=colors,
    autopct=autopct,
    shadow=shadow
)

plt.title('Student of different branches in a college')
plt.show()
