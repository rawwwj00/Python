import matplotlib.pyplot as plt

data = [(170, 65), (180, 80), (175, 75), (160, 55), (165, 60), (185, 90)]
heights, weights = zip(*data)

plt.figure(figsize=(8, 6))
plt.scatter(heights, weights, color='red', marker='o')

for i, (height, weight) in enumerate(data):
    plt.annotate(f'Person {i + 1}', (height, weight), textcoords="offset points", xytext=(0,5), ha='center')

plt.title('Height vs. Weight with Annotations')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)

plt.show()