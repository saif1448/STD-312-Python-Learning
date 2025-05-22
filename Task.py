import matplotlib.pyplot as plt
import numpy as np


import numpy as np
import matplotlib.pyplot as plt

# 1. Generate random marks (or load real data)
np.random.seed(42)
marks = np.random.randint(0, 101, size=200)  # 200 students, marks from 0 to 100

# 2. Define bracket labels and boundaries
brackets = ["0-44", "45-49", "50-59", "60-69", "70-79", "80-89", "90-100"]
counts = [
    np.sum((marks >= 0) & (marks <= 44)),
    np.sum((marks >= 45) & (marks <= 49)),
    np.sum((marks >= 50) & (marks <= 59)),
    np.sum((marks >= 60) & (marks <= 69)),
    np.sum((marks >= 70) & (marks <= 79)),
    np.sum((marks >= 80) & (marks <= 89)),
    np.sum((marks >= 90) & (marks <= 100)),
]

# 3. Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(brackets, counts, color='skyblue', edgecolor='black')
plt.title("Distribution of Student Marks by Bracket")
plt.xlabel("Mark Brackets")
plt.ylabel("Number of Students")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
    