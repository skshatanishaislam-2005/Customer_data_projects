import pandas as pd

# Load cleaned dataset
file = "Cleaned_Customer_Sales_Data.xlsx"
df = pd.read_excel(file)

# Basic information
print("--- Dataset Information ---")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

print("\n--- Total Sales ---")
print("Total Revenue:", df["Total_Sales"].sum())

# Top-selling products by quantity
top_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Top-Selling Products ---")
print(top_products)

print("\n--- Revenue by Category ---")

df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

category_revenue = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)

print(category_revenue)

print("\n--- Sales by Payment Method ---")

payment_sales = df.groupby("Payment_Method")["Total_Sales"].sum().sort_values(ascending=False)

print(payment_sales)

print("\n--- Sales by Order Status ---")

status_sales = df.groupby("Order_Status")["Total_Sales"].sum().sort_values(ascending=False)

print(status_sales)

print("\n--- Monthly Sales ---")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)

print(monthly_sales)

# --- Top Customers by Revenue ---

customer_sales = df.groupby("Customer_Name")["Total_Sales"].sum().sort_values(ascending=False)

print("\n--- Top 10 Customers by Revenue ---")
print(customer_sales.head(10))

# --- Sales by City ---

city_sales = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Sales by City ---")
print(city_sales)

import pandas as pd

# ==========================================
# LOAD CLEANED DATASET
# ==========================================

file_path = "Cleaned_Customer_Sales_Data.xlsx"

df = pd.read_excel(file_path)

# Create Total_Sales column
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]


# ==========================================
# 1. DATASET INFORMATION
# ==========================================

print("\n--- Dataset Information ---")

print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==========================================
# 2. TOTAL SALES
# ==========================================

total_revenue = df["Total_Sales"].sum()

print("\n--- Total Sales ---")
print("Total Revenue:", total_revenue)


# ==========================================
# 3. TOP-SELLING PRODUCTS BY QUANTITY
# ==========================================

top_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Top-Selling Products ---")
print(top_products)


# ==========================================
# 4. REVENUE BY CATEGORY
# ==========================================

category_revenue = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Revenue by Category ---")
print(category_revenue)


# ==========================================
# 5. SALES BY PAYMENT METHOD
# ==========================================

payment_sales = (
    df.groupby("Payment_Method")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Sales by Payment Method ---")
print(payment_sales)


# ==========================================
# 6. SALES BY ORDER STATUS
# ==========================================

status_sales = (
    df.groupby("Order_Status")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Sales by Order Status ---")
print(status_sales)


# ==========================================
# 7. MONTHLY SALES
# ==========================================

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)

print("\n--- Monthly Sales ---")
print(monthly_sales)


# ==========================================
# 8. TOP 10 CUSTOMERS BY REVENUE
# ==========================================

customer_sales = (
    df.groupby("Customer_Name")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Top 10 Customers by Revenue ---")
print(customer_sales.head(10))


# ==========================================
# 9. SALES BY CITY
# ==========================================

city_sales = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Sales by City ---")
print(city_sales)


# ==========================================
# 10. REVENUE BY PRODUCT
# ==========================================

product_revenue = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Revenue by Product ---")
print(product_revenue)


# ==========================================
# END
# ==========================================

print("\n--- Analysis Completed Successfully ---")