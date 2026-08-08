import pandas as pd
from scipy.stats import ttest_ind


# Load cleaned dataset
file_path = "Dataset/Cleaned_ApexPlanet_DataAnalytics_Dataset.xlsx"

df = pd.read_excel(file_path)


# Separate sales by gender
male_sales = df.loc[df["Gender"] == "Male", "Total_Sales"]
female_sales = df.loc[df["Gender"] == "Female", "Total_Sales"]


# Descriptive statistics
print("=== DESCRIPTIVE STATISTICS ===")

print(f"Male Orders: {len(male_sales)}")
print(f"Female Orders: {len(female_sales)}")

print(f"Male Average Sales: ₹{male_sales.mean():,.2f}")
print(f"Female Average Sales: ₹{female_sales.mean():,.2f}")


# Welch's independent two-sample t-test
test_result = ttest_ind(
    male_sales,
    female_sales,
    equal_var=False
)

t_stat = test_result.statistic
p_value = test_result.pvalue


# Hypothesis test results
print("\n=== HYPOTHESIS TEST ===")

print("H0: There is no significant difference in average sales between male and female customers.")
print("H1: There is a significant difference in average sales between male and female customers.")

print(f"\nT-statistic: {t_stat:.3f}")
print(f"P-value: {p_value:.3f}")

alpha = 0.05

print(f"Significance Level: {alpha}")


# Decision
if p_value < alpha:
    print("\nDecision: Reject H0")
    print("Conclusion: The difference is statistically significant.")
else:
    print("\nDecision: Fail to Reject H0")
    print("Conclusion: The difference is not statistically significant.")
