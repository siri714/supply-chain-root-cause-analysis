# Supply Chain Root Cause Analysis

End-to-end analysis identifying root causes of delivery delays and product defects across suppliers, regions, and product categories — built with SQL, Python, and Excel/VBA.

## Problem
Simulated a common ops challenge: inconsistent delivery performance across a supplier network. The goal was to identify *why* deliveries were late, confirm the findings statistically, and build a tool to catch the problem going forward without manual reporting.

## Approach
1. **Data cleaning (Python/pandas)** — fixed inconsistent date formats, handled missing values, removed duplicate order IDs (`clean_data.py`)
2. **SQL analysis (SQLite)** — calculated on-time delivery rate by supplier, average delay by region/carrier, and defect rate by product category (`load_to_sql.py`, `run_queries.py`)
3. **Root-cause testing (Python/scipy)** — used chi-square tests to confirm underperforming suppliers and categories were statistically significant, not random noise (`root_cause.py`)
4. **Automation (Excel/VBA)** — built a macro that automatically flags suppliers below an on-time threshold, removing the need for manual weekly review (`supplier_report.xlsm`, macro in Module1)

## Key Findings
- Three suppliers (SUP-001, SUP-002, SUP-003) had a 60.2% late-delivery rate vs. 28.2% for all others (p < 0.0001, statistically significant)
- Perishables had a 4.00% defect rate vs. 2.19% for other categories (p = 0.0014, statistically significant)
- 6 of 20 suppliers fell below a 55% on-time threshold

See [writeup.md](writeup.md) for the full business recommendation.

## Files
| File | Purpose |
|---|---|
| `shipments_raw.csv` | Raw synthetic shipment data (intentionally messy) |
| `clean_data.py` | Cleans raw data → `shipments_clean.csv` |
| `load_to_sql.py` | Loads clean data into SQLite |
| `run_queries.py` | Core SQL KPI queries |
| `root_cause.py` | Statistical significance testing |
| `export_to_excel.py` | Builds supplier scorecard Excel file |
| `supplier_report.xlsm` | Excel workbook with VBA automation macro |
| `writeup.md` | Business recommendation summary |

## Note on data
This project uses a synthetic dataset built to model realistic supply chain patterns (mixed date formats, missing values, duplicate records) since proprietary company data wasn't available. Statistical relationships were designed to be genuine and testable, not just illustrative.
