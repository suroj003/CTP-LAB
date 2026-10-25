import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [45000, 52000, 48000, 61000, 58000, 65000,
         62000, 70000, 68000, 75000, 72000, 80000]

plt.plot(months, sales, marker="o", label="Line Chart")
plt.bar(months, sales, alpha=0.6, label="Bar Chart")

plt.xlabel("Months")
plt.ylabel("Sales (₹)")
plt.title("Monthly Sales")
plt.legend()
plt.show()

print("Highest Sales:", months[sales.index(max(sales))], max(sales))
print("Lowest Sales:", months[sales.index(min(sales))], min(sales))