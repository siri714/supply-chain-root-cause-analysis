Supply Chain Performance Review: Root Cause Analysis & Recommendations

Summary
Analysis of 5,940 shipment records identified specific, statistically significant drivers of late deliveries and product defects. Three suppliers account for a disproportionate share of delays, and one product category carries elevated defect risk. An automated monitoring tool was built to flag future issues without manual review.

Key Findings

Three suppliers are driving the majority of late deliveries. SUP-001, SUP-002, and SUP-003 have a combined 60.2% late-delivery rate, compared to 28.2% across all other suppliers — more than double. This gap is statistically significant (p < 0.0001), meaning it reflects a real performance issue, not normal variation.
Perishables carry a disproportionate defect rate. 4.00% of Perishable shipments are defective, nearly double the 2.19% rate across all other categories (p = 0.0014, statistically significant).
Six suppliers currently fall below a 55% on-time threshold and are candidates for performance review: SUP-001, SUP-002, SUP-003, SUP-012, SUP-015, SUP-017.

Recommendation

Prioritize a performance review with SUP-001, SUP-002, and SUP-003 — their late-delivery rates are a statistically confirmed, ongoing pattern, not a temporary dip.
Evaluate cold-chain or packaging procedures for Perishables specifically, given the elevated defect rate relative to other categories.
Adopt the automated exception-reporting tool (built in Excel/VBA) for ongoing weekly monitoring, removing the need for manual review of supplier performance data.

What was built

SQL queries calculating on-time delivery rate, average delay, and defect rate across suppliers, regions, and product categories
Python-based statistical testing (chi-square) to confirm findings were significant, not random noise
An Excel/VBA macro that automatically flags underperforming suppliers against a configurable threshold