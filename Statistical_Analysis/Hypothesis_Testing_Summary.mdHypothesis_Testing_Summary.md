# 📊 Hypothesis Testing & Statistical Validation

## 📌 Business Question

Does average sales per order differ significantly between male and female customers?

---

## 🎯 Objective

The objective of this analysis is to statistically validate whether the observed difference in average sales between male and female customers represents a meaningful difference or could have occurred due to random variation in the sample.

---

## 🧪 Hypotheses

### Null Hypothesis (H₀)

There is no significant difference in average sales between male and female customers.

**H₀: μₘₐₗₑ = μ𝒻ₑₘₐₗₑ**

### Alternative Hypothesis (H₁)

There is a significant difference in average sales between male and female customers.

**H₁: μₘₐₗₑ ≠ μ𝒻ₑₘₐₗₑ**

### Significance Level

**α = 0.05**

---

## 📊 Descriptive Statistics

| Metric | Male | Female |
|---|---:|---:|
| Number of Orders | 511 | 489 |
| Average Sales | ₹141,807.34 | ₹136,883.21 |

### Observed Difference

Male average sales were:

**₹4,924.13 higher** than female average sales.

However, an observed difference alone does not establish statistical significance.

---

## 🔬 Statistical Method

A **Welch's Independent Two-Sample T-Test** was performed to compare the average sales of the two independent gender groups.

Welch's t-test was selected because it does not require the assumption that both groups have equal variances.

---

## 📈 Test Results

| Statistic | Result |
|---|---:|
| T-statistic | 0.683 |
| P-value | 0.495 |
| Significance Level | 0.05 |

---

## 📐 95% Confidence Interval

The estimated difference in average sales was:

**₹4,924.13**

The 95% confidence interval for the difference was:

**−₹9,231.58 to ₹19,079.85**

The interval includes **₹0**, indicating that a zero difference remains plausible based on the sample.

---

## ✅ Statistical Decision

The decision rule is:

- If **p-value < 0.05** → Reject H₀
- If **p-value ≥ 0.05** → Fail to Reject H₀

Since:

**0.495 > 0.05**

the null hypothesis is **not rejected**.

### Decision

> **Fail to Reject H₀**

---

## 💡 Business Interpretation

Although male customers recorded a higher observed average sales value than female customers by approximately ₹4,924 per order, the statistical test produced a p-value of 0.495.

Because the p-value is greater than the 0.05 significance threshold, the observed difference is **not statistically significant**.

Therefore, the available data does not provide sufficient statistical evidence that average sales per order differs between male and female customers.

---

## 🎯 Business Recommendation

Gender should **not be treated as a strong standalone factor for differentiating average order value** based on this analysis.

Future analysis could examine other factors such as:

- Product
- Category
- City
- Quantity
- Unit Price
- Customer characteristics

Combining these variables may provide stronger explanations for differences in sales performance.

---

## 🧾 Conclusion

The descriptive analysis showed a difference in average sales between male and female customers. However, statistical validation demonstrated that this difference was not statistically significant.

This highlights the importance of combining descriptive analytics with statistical testing before making business decisions based on observed patterns.
