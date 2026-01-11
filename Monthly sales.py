import pandas as pd
import matplotlib.pyplot as plt

# ---------- STEP 1: CREATE SAMPLE CSV FILE ----------
file_name = "sales.csv"

data_text = """Date,Sales
2024-01-05,1200
2024-01-15,1800
2024-02-02,1500
2024-02-20,2200
2024-03-10,3000
2024-03-25,2800
2024-04-05,2500
2024-04-18,2700
2024-05-01,3200
2024-05-20,3500
"""

with open(file_name, "w") as file:
    file.write(data_text)

print("sales.csv file created successfully!\n")

# ---------- STEP 2: LOAD DATA ----------
data = pd.read_csv(file_name)

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract Month from Date
data['Month'] = data['Date'].dt.month_name()

# ---------- STEP 3: MONTHLY SALES CALCULATION ----------
monthly_sales = data.groupby('Month')['Sales'].sum()

print("----- Monthly Sales Summary -----")
print(monthly_sales)

# ---------- STEP 4: BEST & WORST MONTH ----------
best_month = monthly_sales.idxmax()
worst_month = monthly_sales.idxmin()

print("\nBest Month :", best_month, "=> Sales =", monthly_sales.max())
print("Worst Month:", worst_month, "=> Sales =", monthly_sales.min())

# ---------- STEP 5: PLOT GRAPH ----------
plt.figure()
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()
