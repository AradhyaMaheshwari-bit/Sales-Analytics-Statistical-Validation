# 📊 Data Storytelling & Statistical Validation

<div align="center">

## 🚀 Sales Performance Analysis

**👨‍💻 Author:** **Aradhya Maheshwari**

</div>

---

# 📌 Project Overview

This project combines **sales data analysis, business storytelling, and statistical validation** to transform analytical findings into a clear business narrative.

The project focuses on identifying major sales drivers, understanding customer and revenue patterns, and statistically validating whether an observed difference in average sales between male and female customers is significant.

---

# 🎯 Objectives

- 📊 Analyze overall sales performance
- 💰 Identify major revenue contributors
- 🏷️ Analyze category and city performance
- 📅 Understand monthly revenue trends
- 👥 Analyze customer characteristics
- 🧪 Formulate and test a business hypothesis
- 📐 Interpret statistical significance and confidence intervals
- 💡 Translate analytical findings into business recommendations
- 📖 Present findings through a stakeholder-focused presentation

---

# 🛠️ Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| 🐍 Python | Statistical Analysis |
| 🐼 Pandas | Data Processing |
| 📐 SciPy | Hypothesis Testing |
| 📊 Microsoft Power BI | Business Intelligence |
| 🧮 DAX | Analytical Measures |
| 🔄 Power Query | Data Transformation |
| 📑 Microsoft Excel | Dataset & Analysis |
| 📈 Data Visualization | Business Storytelling |

---

# 📂 Project Structure

```text
Data-Storytelling-Statistical-Validation/
│
├── 📁 Dataset/
│   └── Cleaned_Sales_Dataset.xlsx
│
├── 📁 Presentation/
│   └── Sales_Analysis_Story.pptx
│
├── 📁 Statistical_Analysis/
│   ├── hypothesis_testing.py
│   └── Hypothesis_Testing_Summary.md
│
├── 📄 README.md
├── 📄 LICENSE
└── 📄 .gitignore
```

> 📌 If the presentation is exported to PDF, it can also be added to the `Presentation/` folder.

---

# 📊 Business Analysis

The analysis examined:

- 💰 Overall revenue performance
- 🏷️ Revenue by category
- 🏙️ Revenue by city
- 📅 Monthly revenue trends
- 📦 Product performance
- 👥 Customer demographics
- 📈 Average sales by gender

These findings were combined into a structured business narrative to identify key performance areas and potential business actions.

---

# 🔬 Statistical Validation

## 📌 Business Question

> **Does average sales per order differ significantly between male and female customers?**

---

## 🧪 Hypotheses

### Null Hypothesis — H₀

There is no significant difference in average sales between male and female customers.

**H₀: μₘₐₗₑ = μ𝒻ₑₘₐₗₑ**

### Alternative Hypothesis — H₁

There is a significant difference in average sales between male and female customers.

**H₁: μₘₐₗₑ ≠ μ𝒻ₑₘₐₗₑ**

### Significance Level

**α = 0.05**

---

# 📈 Descriptive Results

| Metric | Male | Female |
|---|---:|---:|
| Orders | 511 | 489 |
| Average Sales | ₹141,807.34 | ₹136,883.21 |

### Observed Difference

The male average sales value was:

**₹4,924.13 higher** than the female average.

However, this observed difference was statistically tested before drawing a business conclusion.

---

# 🧪 Hypothesis Test

A **Welch's Independent Two-Sample T-Test** was performed because the analysis compares the average sales of two independent groups without assuming equal variances.

| Statistic | Result |
|---|---:|
| T-statistic | **0.683** |
| P-value | **0.495** |
| Significance Level | **0.05** |
| Mean Difference | **₹4,924.13** |
| 95% Confidence Interval | **−₹9,231.58 to ₹19,079.85** |

---

# ✅ Statistical Conclusion

Since:

```text
P-value = 0.495
α       = 0.05
```

and:

```text
0.495 > 0.05
```

the null hypothesis is **not rejected**.

### Final Finding

> **The observed difference in average sales between male and female customers is not statistically significant.**

The 95% confidence interval also includes **₹0**, meaning that a zero difference remains plausible based on the sample.

---

# 💡 Business Insights

- 🏆 High-performing categories contribute substantially to overall revenue.
- 🏙️ Revenue performance varies across cities.
- 📅 Monthly revenue shows fluctuations throughout the year.
- 👥 Male and female customers contribute relatively similar numbers of orders.
- 📊 Male customers showed a higher observed average sales value, but the difference was not statistically significant.
- 🎯 Gender should therefore not be treated as a strong standalone factor for explaining differences in average sales.

---

# 🎯 Business Recommendations

### 🏷️ Focus on Strong Categories

Continue monitoring and strengthening high-performing categories and products.

### 🏙️ Investigate High-Performing Locations

Analyze the factors behind stronger city-level performance and identify opportunities to apply successful strategies elsewhere.

### 👥 Avoid Over-Segmentation by Gender

Since the gender-based difference was not statistically significant, business decisions should not rely on gender alone.

### 🔍 Explore Stronger Sales Drivers

Further analysis should investigate:

- Product
- Category
- City
- Quantity
- Unit Price
- Customer characteristics

to identify stronger drivers of sales performance.

---

# 📖 Data Story

The project follows a business-focused analytical narrative:

```text
Overall Sales Performance
          ↓
Identify Revenue Drivers
          ↓
Analyze Trends & Customers
          ↓
Observe Potential Difference
          ↓
Statistical Validation
          ↓
Interpret the Evidence
          ↓
Business Recommendations
```

The key takeaway is that **data-driven decisions should be based not only on observed patterns, but also on statistical evidence.**

---

# 📑 Presentation

The project includes a stakeholder-focused presentation covering:

1. 🎬 Sales Performance Analysis
2. 🎯 Business Objective
3. 💰 Overall Sales Performance
4. 📊 Revenue Drivers
5. 📅 Monthly Revenue Trend
6. 👥 Customer Insights
7. 🔬 Hypothesis & Statistical Test
8. 📐 Statistical Findings
9. 💡 Recommendations & Call to Action

---

# 🎓 Learning Outcomes

✔ Data Storytelling

✔ Business Analysis

✔ Hypothesis Testing

✔ Welch's Independent Two-Sample T-Test

✔ P-value Interpretation

✔ Confidence Interval Analysis

✔ Statistical Decision-Making

✔ Business Recommendations

✔ Stakeholder Presentation

✔ Python Statistical Analysis

---

# 🚀 Conclusion

This project demonstrates how analytical findings can be transformed into a structured business story and strengthened through statistical validation.

The analysis combines descriptive analytics with hypothesis testing to distinguish between **observed differences and statistically supported conclusions**.

The final outcome is a data-driven sales analysis that communicates not only **what happened**, but also **how confidently the findings can be used for business decision-making**.

---

## ⭐ Key Takeaway

> **Data tells us what happened. Statistical validation helps us understand whether the difference we observe is meaningful.**
