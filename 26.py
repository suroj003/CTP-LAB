import matplotlib.pyplot as plt

hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]
scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

# Histogram
plt.hist(hours, bins=5, edgecolor="black")
plt.xlabel("Study Hours per Week")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")
plt.show()

# Scatter plot
plt.scatter(hours, scores)
plt.xlabel("Study Hours per Week")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Scores")
plt.show()