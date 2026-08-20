import pandas as pd

file = "Messy_Customer_Sales_data.xlsx"

df = pd.read_excel(file, sheet_name= "Messy_Data")

#Besic information
print("Dataset size:", df.shape)

#missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

#Duplicate rows
print("\n--- Double Rows ---")
print("Number of Duplicates:" , df.duplicated().sum())


#clean Customer names
df["Customer_Name"] = (
    df["Customer_Name"]
    .str.strip()
    .str.title()
)

#Clean Cities
df["City"] = (
    df["City"]
    .str.strip()
    .str.title()
)

#Clean Order Status
df["Order_Status"] = (
    df["Order_Status"]
    .str.strip()
    .str.title()
)

#check cities
print("\n--- Cities ----")
print(df["City"].unique())


#check order status
print("\n--- Order Status ---")
print(df["Order_Status"].unique())

#Check quantities
print("\n--- Quantity Values ---")
print(df["Quantity"].describe())

# Find invalid quantities
print("\n--- Invalid Quantities ---")
print(df[df["Quantity"] <= 0][["Order_ID", "Customer_Name", "Quantity"]])

# Find unusually high quantities
print("\n--- High Quantities ---")
print(df[df["Quantity"] > 10][["Order_ID", "Customer_Name", "Quantity"]])

# Find missing values
print("\n--- Rows with Missing Values ---")
print(df[df.isnull().any(axis=1)].head(20))

# Remove duplicate rows
before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print("\n--- Duplicate Cleaning ---")
print("Rows before:", before_duplicates)
print("Rows after:", after_duplicates)
print("Duplicates removed:", before_duplicates - after_duplicates)

# Check missing values after removing duplicates
print("\n--- Missing Values After Duplicate Removal ---")
print(df.isnull().sum())

# Inspect rows with missing important values

print("\n--- Missing Phone ---")
print(df[df["Phone"].isna()][["Order_ID", "Customer_Name", "Email", "City", "Phone"]])

print("\n--- Missing City ---")
print(df[df["City"].isna()][["Order_ID", "Customer_Name", "Email", "City"]])

print("\n--- Missing Quantity / Price ---")
print(
    df[df["Quantity"].isna() | df["Unit_Price"].isna()]
    [["Order_ID", "Product", "Category", "Quantity", "Unit_Price"]]
)

# Fill missing Quantity
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

# Fill missing Unit_Price based on Product
df["Unit_Price"] = df.groupby("Product")["Unit_Price"].transform(
    lambda x: x.fillna(x.median())
)

# Check missing values
print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

# Fill missing Phone
df["Phone"] = df["Phone"].fillna("Unknown")

# Fill missing City
df["City"] = df["City"].fillna("Unknown")

# Check missing values again
print("\n--- Final Missing Values ---")
print(df.isnull().sum())

# --- Data Validation ---

print("\n--- Invalid Quantity ---")
print(df[df["Quantity"] <= 0])

print("\n--- Invalid Unit Price ---")
print(df[df["Unit_Price"] <= 0])

print("\n--- Invalid Dates ---")
print(df[df["Order_Date"].isna()])

print("\n--- Invalid Quantity Values ---")
print(df.loc[df["Quantity"] <= 0, ["Order_ID", "Product", "Category", "Quantity", "Unit_Price"]])

# Clean invalid quantities
df = df[df["Quantity"] > 0]

print("\n--- After Quantity Cleaning ---")
print("Rows after cleaning:", len(df))


# Final dataset check
print("\n--- Final Dataset Info ---")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n--- Final Missing Values ---")
print(df.isnull().sum())

# Save cleaned dataset
output_file = "Cleaned_Customer_Sales_Data.xlsx"

df.to_excel(output_file, index=False)

print("\n--- File Saved ---")
print("Saved as:", output_file)