import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# LOAD CLEANED DATA
# ==========================================

file_path = "Cleaned_Customer_Sales_Data.xlsx"

df = pd.read_excel(file_path)

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])


# ==========================================
# 1. REVENUE BY CATEGORY
# ==========================================

category_revenue = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

category_revenue.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()


# ==========================================
# 2. MONTHLY SALES TREND
# ==========================================

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

plt.show()


# ==========================================
# 3. TOP 10 PRODUCTS BY QUANTITY
# ==========================================

top_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(9, 5))

top_products.plot(kind="bar")

plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ==========================================
# 4. REVENUE BY PRODUCT
# ==========================================

product_revenue = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ==========================================
# 5. SALES BY PAYMENT METHOD
# ==========================================

payment_sales = (
    df.groupby("Payment_Method")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

payment_sales.plot(kind="bar")

plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue")
plt.xticks(rotation=30)

plt.tight_layout()

plt.show()


# ==========================================
# 6. SALES BY CITY
# ==========================================

city_sales = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ==========================================
# 7. SALES BY ORDER STATUS
# ==========================================

status_sales = (
    df.groupby("Order_Status")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(7, 5))

status_sales.plot(kind="bar")

plt.title("Sales by Order Status")
plt.xlabel("Order Status")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# ==========================================
# 8. TOP 10 CUSTOMERS BY REVENUE
# ==========================================

customer_sales = (
    df.groupby("Customer_Name")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

customer_sales.plot(kind="bar")

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


print("\n--- All Visualizations Completed Successfully ---")


import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load cleaned dataset
# -----------------------------
df = pd.read_excel("Cleaned_Customer_Sales_Data.xlsx")

# Make sure Total_Sales exists
if "Total_Sales" not in df.columns:
    df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]


# -----------------------------
# 1. Revenue by Category
# -----------------------------
category_revenue = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.show()


# -----------------------------
# 2. Sales by Payment Method
# -----------------------------
payment_sales = (
    df.groupby("Payment_Method")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
payment_sales.plot(kind="bar")
plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_by_payment_method.png")
plt.show()


# -----------------------------
# 3. Sales by Order Status
# -----------------------------
status_sales = (
    df.groupby("Order_Status")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
status_sales.plot(kind="bar")
plt.title("Sales by Order Status")
plt.xlabel("Order Status")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_order_status.png")
plt.show()


# -----------------------------
# 4. Monthly Sales Trend
# -----------------------------
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()


# -----------------------------
# 5. Top 10 Customers by Revenue
# -----------------------------
customer_sales = (
    df.groupby("Customer_Name")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
customer_sales.sort_values().plot(kind="barh")
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Customer")
plt.tight_layout()
plt.savefig("top_10_customers.png")
plt.show()


# -----------------------------
# 6. Sales by City
# -----------------------------
city_sales = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))
city_sales.plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_city.png")
plt.show()


# -----------------------------
# 7. Revenue by Product
# -----------------------------
product_revenue = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()


print("\n--- All Visualizations Completed Successfully ---")