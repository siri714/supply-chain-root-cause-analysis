import pandas as pd

df = pd.read_csv("shipments_raw.csv")

print("=== BEFORE CLEANING ===")
print(f"Rows: {len(df)}")
print(f"Duplicate order_ids: {df['order_id'].duplicated().sum()}")
print("Missing values per column:")
print(df.isna().sum())
print()

# 1. Remove duplicate order_id rows, keep the first occurrence
df = df.drop_duplicates(subset="order_id", keep="first")

# 2. Parse inconsistent date formats
def parse_messy_date(val):
    if pd.isna(val):
        return pd.NaT
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%b-%Y", "%Y/%m/%d"):
        try:
            return pd.to_datetime(val, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.to_datetime(val, errors="coerce")

df["order_date"] = df["order_date"].apply(parse_messy_date)
df["promised_date"] = pd.to_datetime(df["promised_date"], errors="coerce")
df["actual_delivery_date"] = pd.to_datetime(df["actual_delivery_date"], errors="coerce")

# 3. Fill missing region/category with "Unknown" instead of dropping rows
df["region"] = df["region"].fillna("Unknown")
df["product_category"] = df["product_category"].fillna("Unknown")

# 4. Drop rows with no delivery date (can't compute delay without it)
undelivered = df["actual_delivery_date"].isna().sum()
df = df.dropna(subset=["actual_delivery_date"])

# 5. Compute the core metric: delay in days
df["delay_days"] = (df["actual_delivery_date"] - df["promised_date"]).dt.days
df["is_late"] = (df["delay_days"] > 0).astype(int)

print("=== AFTER CLEANING ===")
print(f"Rows: {len(df)} (dropped {undelivered} with no delivery date)")
print("Remaining missing values:")
print(df.isna().sum())

df.to_csv("shipments_clean.csv", index=False)
print()
print("Saved shipments_clean.csv")
