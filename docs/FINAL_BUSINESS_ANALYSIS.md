# Final Business Analysis and Recommendations

**Analysis period:** January 2022–December 2023  
**Scope:** 17,104 financially complete transactions from a restaurant sales dataset  
**Tools:** Python (pandas), Google Colab, Tableau Public  
**Unit:** Dataset currency units (the source does not specify a currency)

## Executive summary

Restaurant revenue decreased from **174,102** in 2022 to **166,515.50** in 2023, a **4.36% decline**. Units sold fell by **3.93%**, and transaction count fell **3.06%**. Revenue per unit changed only modestly (about **6.62 → 6.59**). The decline is therefore **associated primarily with lower transaction and sales volume**, rather than an obvious broad reduction in the realized revenue per unit. These figures alone do not establish *why* volume declined.

## 1. Business performance

| KPI | Full period | 2022 | 2023 |
|---|---:|---:|---:|
| Revenue | 340,617.50 | 174,102.00 | 166,515.50 |
| Units sold | 51,554 | 26,294 | 25,260 |
| Valid orders | 17,104 | 8,685 | 8,419 |
| Average order value | 19.91 | 20.05 | 19.78 |
| Distinct customer IDs | 100 | 100 | 100 |

The average order value fell by approximately **1.35%**. Transaction count fell **3.06%**. Combined, these changes are consistent with the overall revenue decrease. Revisit quantity, visits and basket size together rather than focusing on only one measure.

## 2. Product and category mix

| Category | Total revenue | Share of total | 2022→2023 revenue change |
|---|---:|---:|---:|
| Main Dishes | 160,553.00 | 47.14% | -5.76% |
| Starters | 60,044.00 | 17.63% | -4.45% |
| Desserts | 56,883.00 | 16.70% | -3.94% |
| Side Dishes | 40,549.00 | 11.90% | -0.57% |
| Drinks | 22,588.50 | 6.63% | -1.75% |

Main Dishes contribute nearly **half of all revenue**, so small shifts in this category matter disproportionately. It also accounted for **4,763** of the **7,586.50** net revenue loss between years (~**62.8%** of the net decline). These contributions are descriptive, not proof of a causal explanation.

### Top named products by revenue

| Item | Revenue |
|---|---:|
| Grilled Chicken | 37,380 |
| Pasta Alfredo | 37,128 |
| Steak | 35,320 |

Together, these three products generated **32.24% of total revenue**. This ranking **excludes blank item names**, although the associated revenue remains in the overall total.

### Largest named-item revenue declines (2022→2023)

| Item | Absolute revenue change |
|---|---:|
| Steak | -1,680 |
| Pasta Alfredo | -1,320 |
| Salmon | -936 |
| Grilled Chicken | -780 |
| Sweet Potato Fries | -660 |

These five declines sum to **-5,376**, equivalent to **70.86% of the net restaurant-wide revenue drop**. This percentage describes the magnitude relative to the *net* fall: other item gains partly offset declines, so it must not be interpreted as a causal contribution or as a percentage of gross losses.

### Notable named-item gains

Side Salad **+588**, Grilled Vegetables **+345**, Coca Cola **+275**, Vegetarian Platter **+196**, and Chicken Melt **+64**. The five increases total **1,468**. Revenue associated with **unknown item names** declined **291** between years; accounting for that group is necessary to reconcile named-product changes with the restaurant-wide total.

## 3. Customer behavior

- **100 distinct customer IDs** were observed in the analysis-ready file.
- The 10 highest-revenue customer IDs generated **40,227.50**, or **11.81%** of total revenue.
- Customer transaction count and customer revenue show a positive correlation of approximately **0.708**; this relationship is not evidence that increasing frequency *causes* a proportional revenue gain.
- Customer revenues were relatively concentrated around the mean (coefficient of variation approximately **10.14%**), rather than dominated by one or two extremely high-revenue IDs.

Because there are only 100 unique IDs across two years, avoid treating these records as evidence of the restaurant's true customer population or making demographic claims.

## 4. Payment channels and completeness

| Payment method | Transactions | Revenue | Total-revenue share |
|---|---:|---:|---:|
| Cash | 5,412 | 110,467.50 | 32.43% |
| Credit Card | 5,406 | 106,586.50 | 31.29% |
| Digital Wallet | 5,343 | 104,657.00 | 30.73% |
| Unknown / Missing | 943 | 18,906.50 | 5.55% |

None of the three **known** payment methods overwhelmingly dominates revenue. Missing payment labels must be displayed separately rather than assigned to Cash, Credit Card, or Digital Wallet without evidence.

## 5. Prioritized recommendations

| Priority | Suggested business action | Rationale | How to test it |
|---|---|---|---|
| High | Investigate Steak, Pasta Alfredo, Salmon and Grilled Chicken | Large absolute revenue declines in high-value items | Compare weekly availability, customer orders, operational changes and promotions; monitor item units, revenue and stockouts |
| High | Diagnose lower transaction volume | Orders and units sold both declined year over year | Combine transaction data with footfall, service hours and marketing campaign records; assess conversion and repeat visits |
| Medium | Experiment with non-discounted item bundles | Side dishes and selected drinks showed relative resilience | Run a time-limited pilot; measure basket size, incremental units, revenue and gross margin once cost data is available |
| Medium | Improve payment-method capture | 943 analyzed transactions have missing payment labels | Make payment type a required POS field where appropriate; monitor unknown-payment rate over time |
| Medium | Improve product-name completeness | 1,328 analyzed transactions lack item names | Enforce item catalog selection in POS; monitor blank item rate; avoid using guessed item assignments |
| Medium | Add cost and margin data | Revenue rankings can mask low-margin products | Join cost of goods, labor and discounts, then evaluate contribution margin and profitability |

These are **hypotheses and next investigations**, not guaranteed financial outcomes. Pilot test interventions and evaluate results before scaling.

## 6. Limitations and next steps

The dataset lacks costs, margins, discounts, stockouts, campaign exposure, customer demographics and external market drivers. Therefore, conclusions about causes of declining demand or expected financial benefits of recommendations would be speculative. The source's currency and licensing are also unspecified. The 430 original rows without usable financial values are excluded from these KPIs.

**Next analysis:** With operational and cost data, build a weekly performance scorecard, category gross-margin view and validated customer cohort analysis. Add a consistent missing-data monitoring process.

---

**Portfolio conclusion:** The project combines deterministic data recovery, financial validation, exploratory analysis, year-over-year decomposition and interactive Tableau dashboards to turn transaction data into an auditable business narrative while preserving uncertainty and data limitations.
