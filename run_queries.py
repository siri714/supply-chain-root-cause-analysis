import sqlite3
import pandas as pd

conn = sqlite3.connect("supply_chain.db")

print("=== 1. On-time delivery rate by supplier ===")
q1 = """
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
print(pd.read_sql_query(q1, conn).to_string(index=False))

print("\n=== 2. Average delay by region and carrier ===")
q2 = """
SELECT
    region,
    carrier,
    COUNT(*) AS total_shipments,
    ROUND(AVG(delay_days), 2) AS avg_delay_days,
    ROUND(100.0 * SUM(is_late) / COUNT(*), 1) AS late_pct
FROM shipments
GROUP BY region, carrier
ORDER BY avg_delay_days DESC
LIMIT 10;
"""
print(pd.read_sql_query(q2, conn).to_string(index=False))

print("\n=== 3. Defect rate by product category ===")
q3 = """
SELECT
    product_category,
    COUNT(*) AS total_shipments,
    SUM(defect_flag) AS defects,
    ROUND(100.0 * SUM(defect_flag) / COUNT(*), 2) AS defect_rate_pct
FROM shipments
GROUP BY product_category
ORDER BY defect_rate_pct DESC;
"""
print(pd.read_sql_query(q3, conn).to_string(index=False))

conn.close()