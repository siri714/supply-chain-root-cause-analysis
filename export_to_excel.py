import sqlite3
import pandas as pd

conn = sqlite3.connect("supply_chain.db")

query = """
SELECT
    supplier,
    COUNT(*) AS total_shipments,
    SUM(is_late) AS late_shipments,
    ROUND(100.0 * (COUNT(*) - SUM(is_late)) / COUNT(*), 1) AS on_time_pct,
    ROUND(AVG(delay_days), 2) AS avg_delay_days
FROM shipments
GROUP BY supplier
ORDER BY on_time_pct ASC;
"""

df = pd.read_sql_query(query, conn)
df.to_excel("supplier_report.xlsx", sheet_name="SupplierScorecard", index=False)
conn.close()

print("Saved supplier_report.xlsx")