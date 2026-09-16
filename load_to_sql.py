import pandas as pd
import sqlite3

df = pd.read_csv("shipments_clean.csv")

conn = sqlite3.connect("supply_chain.db")
df.to_sql("shipments", conn, if_exists="replace", index=False)
conn.close()

print(f"Loaded {len(df)} rows into supply_chain.db -> table 'shipments'")