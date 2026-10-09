
import math
import pandas as pd
import matplotlib.pyplot as plt


# Function to calculate correlation coefficient manually
def correlation_coefficient(x, y):

    if len(x) != len(y):
        raise ValueError("Both variables must have equal lengths.")

    n = len(x)

    if n < 2:
        raise ValueError("At least two observations are required.")

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(a * b for a, b in zip(x, y))
    sum_x2 = sum(a * a for a in x)
    sum_y2 = sum(b * b for b in y)

    numerator = n * sum_xy - sum_x * sum_y

    denominator_x = n * sum_x2 - sum_x ** 2
    denominator_y = n * sum_y2 - sum_y ** 2

    denominator = math.sqrt(denominator_x * denominator_y)

    if denominator == 0:
        raise ValueError("Correlation is undefined for constant data.")

    return numerator / denominator


# Example 1: Positive correlation
x = [1, 2, 3, 4, 5]
y_positive = [2, 4, 6, 8, 10]

r_positive = correlation_coefficient(x, y_positive)
print("Positive Correlation:", round(r_positive, 3))


# Example 2: Negative correlation
y_negative = [10, 8, 6, 4, 2]

r_negative = correlation_coefficient(x, y_negative)
print("Negative Correlation:", round(r_negative, 3))


# Example 3: Zero correlation
y_zero = [2, 5, 3, 1, 4]

r_zero = correlation_coefficient(x, y_zero)
print("Zero Correlation:", round(r_zero, 3))


# Example 4: Use the provided EV Energy Consumption dataset
import os
base = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base, "EV_Energy_Consumption_Dataset.csv"))

# Select two numerical columns and remove missing values
data = df[["Speed_kmh", "Energy_Consumption_kWh"]].dropna()

speed = data["Speed_kmh"].tolist()
energy = data["Energy_Consumption_kWh"].tolist()

r_dataset = correlation_coefficient(speed, energy)

print(
    "Dataset Correlation (Speed vs Energy Consumption):",
    round(r_dataset, 3)
)


# Plot four scatter plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Positive correlation
axes[0, 0].scatter(x, y_positive)
axes[0, 0].set_title(f"Positive Correlation (r = {r_positive:.3f})")
axes[0, 0].set_xlabel("X")
axes[0, 0].set_ylabel("Y")

# Negative correlation
axes[0, 1].scatter(x, y_negative)
axes[0, 1].set_title(f"Negative Correlation (r = {r_negative:.3f})")
axes[0, 1].set_xlabel("X")
axes[0, 1].set_ylabel("Y")

# Zero correlation
axes[1, 0].scatter(x, y_zero)
axes[1, 0].set_title(f"Zero Correlation (r = {r_zero:.3f})")
axes[1, 0].set_xlabel("X")
axes[1, 0].set_ylabel("Y")

# Actual dataset
axes[1, 1].scatter(speed, energy, alpha=0.5, s=12)
axes[1, 1].set_title(
    f"Speed vs Energy Consumption (r = {r_dataset:.3f})"
)
axes[1, 1].set_xlabel("Speed (km/h)")
axes[1, 1].set_ylabel("Energy Consumption (kWh)")

for ax in axes.flat:
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

