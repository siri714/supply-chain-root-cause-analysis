import pandas as pd
from scipy import stats

df = pd.read_csv("shipments_clean.csv")

# --- Find the 3 worst suppliers by late rate ---
supplier_late_pct = df.groupby("supplier")["is_late"].mean().sort_values(ascending=False)
worst_3 = supplier_late_pct.head(3).index.tolist()

group_worst = df[df["supplier"].isin(worst_3)]["is_late"]
group_rest = df[~df["supplier"].isin(worst_3)]["is_late"]

contingency = pd.crosstab(df["supplier"].isin(worst_3), df["is_late"])
chi2, p_val, dof, expected = stats.chi2_contingency(contingency)

print("=== Are the worst 3 suppliers significantly worse? ===")
print(f"Worst 3 suppliers: {worst_3}")
print(f"Late rate (worst 3): {group_worst.mean():.1%}")
print(f"Late rate (all others): {group_rest.mean():.1%}")
print(f"Chi-square p-value: {p_val:.6f}")
print("--> Statistically significant (p < 0.05)" if p_val < 0.05 else "--> NOT significant")
print()

# --- Is Perishables' defect rate significantly higher? ---
contingency2 = pd.crosstab(df["product_category"] == "Perishables", df["defect_flag"])
chi2_d, p_val_d, _, _ = stats.chi2_contingency(contingency2)

per_rate = df[df["product_category"] == "Perishables"]["defect_flag"].mean()
other_rate_d = df[df["product_category"] != "Perishables"]["defect_flag"].mean()

print("=== Is the Perishables defect rate significantly higher? ===")
print(f"Perishables defect rate: {per_rate:.2%}")
print(f"Other categories defect rate: {other_rate_d:.2%}")
print(f"Chi-square p-value: {p_val_d:.6f}")
print("--> Statistically significant (p < 0.05)" if p_val_d < 0.05 else "--> NOT significant")