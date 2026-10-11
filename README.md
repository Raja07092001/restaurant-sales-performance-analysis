# Restaurant Sales Performance Analysis | Python & Tableau

**End-to-end data analytics portfolio project** examining transaction-level restaurant sales over 2022–2023. This project cleans and validates sales records, investigates revenue and product performance, and communicates findings through **two interactive Tableau dashboards**.

**Tech stack:** Python · pandas · Google Colab · Tableau Public · Excel · GitHub

**[View Interactive Tableau Dashboard](<https://public.tableau.com/views/Restaurant_Sales_Interactive_Final/ProductCustomerAnalysis>)** · **[Read Final Business Analysis](docs/FINAL_BUSINESS_ANALYSIS.md)**

> **Business question:** Why did revenue fall in 2023, which product categories were most affected, and what should the business investigate next?

## At a glance

| Metric | Result |
|---|---:|
| Revenue across both years | **340,617.50** |
| Financially complete transactions | **17,104** |
| Units sold | **51,554** |
| Average order value | **19.91** |
| Distinct customer IDs | **100** |
| 2023 revenue versus 2022 | **-4.36%** |

*All monetary figures are in the dataset's unspecified currency units. Order counts refer to records with complete financial fields.*

## Key findings

**1. The 2023 decline is primarily associated with lower volume.** Revenue fell from **174,102** (2022) to **166,515.50** (2023). Orders declined **3.06%** and units sold **3.93%**; average order value declined **1.35%**. The dataset does not establish the causal reason.

**2. Main Dishes drive revenue, but also accounted for the largest category decline.** Main Dishes generated **160,553 (47.14%)** of revenue. Their revenue fell **5.76%** year over year.

**3. Revenue relies on a small set of named items.** Grilled Chicken (**37,380**), Pasta Alfredo (**37,128**) and Steak (**35,320**) collectively produced **32.24%** of overall revenue. Steak (**-1,680**) and Pasta Alfredo (**-1,320**) were the two largest named-item absolute revenue declines.

**4. Data-quality caveats matter.** The original dataset had **17,534** rows. The analysis excludes **430** records without sufficient financial information. Among the remaining records, **1,328** lack an item label and **943** lack a payment-method label. Blank item revenue is kept in total revenue but excluded from named-item rankings.

## Tableau dashboards

**Restaurant Sales Overview** — headline KPIs, monthly revenue, year-over-year comparison, category mix and payment channels.

**Product & Customer Analysis** — leading items, customer revenue, order frequency and category comparison.

Interactive **Year**, **Category** and **Payment Channel** filters and chart-click actions enable drill-down. The author validated overall and 2023 KPI totals in Tableau Public Desktop.

**[Open the published Tableau Public dashboard →](<https://public.tableau.com/views/Restaurant_Sales_Interactive_Final/ProductCustomerAnalysis>)** (opens the Product & Customer Analysis view). The Tableau Public workbook contains both dashboard views. The final packaged `.twbx` is not included in this GitHub repository.

See [Dashboard guide](tableau/README.md) for workbook opening and validation instructions.

## Data methodology

- Examined null patterns, key uniqueness, categorical values and date range.
- Used `Order Total = Price × Quantity` to validate financial consistency.
- Deterministically recovered **446** missing unit prices from known quantity and order total (where possible).
- Retained original records with incomplete financial details in the cleaned dataset; excluded **430** from financial analysis without inventing revenue.
- Computed KPI, monthly, category, product, payment and customer summaries with pandas.
- Reconciled missing-item revenue when interpreting product trends.

Detailed documentation: [Data quality & limitations](docs/DATA_CLEANING_AND_LIMITATIONS.md).

## Reproduce the analysis

Install Python 3.10+ and pandas, then place an authorized copy of the analysis-ready CSV at `data/restaurant_sales_analysis_ready.csv`.

```bash
pip install -r requirements.txt
python src/analyze_restaurant_sales.py --input data/restaurant_sales_analysis_ready.csv
```

The script validates transactions and generates KPI and analytical tables locally under `outputs/`. Only three selected, non-identifying examples are committed: monthly sales, item revenue (including unknown labels), and item year-over-year changes. The repeated headline, category, yearly and payment summaries are intentionally omitted from GitHub because those key figures already appear in the README and [business report](docs/FINAL_BUSINESS_ANALYSIS.md). Customer-ID-level exports are generated locally only; the transaction-level CSV remains excluded until provenance and sharing rights are confirmed.

To run the built-in checks, install `requirements-dev.txt` and run `python -m pytest -q tests/`. GitHub Actions runs the same checks on changes.

## Repository layout

```text
restaurant-sales-performance-analysis/
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── .github/workflows/tests.yml
├── src/
│   └── analyze_restaurant_sales.py
├── tests/
│   └── test_analysis.py
├── data/
│   └── README.md
├── outputs/
│   ├── monthly_summary.csv
│   ├── item_summary_including_unknown.csv
│   └── item_yoy.csv
├── tableau/
│   └── README.md
└── docs/
    ├── DATA_CLEANING_AND_LIMITATIONS.md
    └── FINAL_BUSINESS_ANALYSIS.md
```

## Business recommendations

**Investigate high-impact main-course declines**, measure transaction and unit-volume drivers, test complementary side-dish bundles, and improve product/payment data capture. Recommendations are framed as testable hypotheses, not causal conclusions or guaranteed profit improvements. Read the [full business analysis](docs/FINAL_BUSINESS_ANALYSIS.md) for specific metrics and validation plans.

## Notes on source and scope

- Raw dataset source and redistribution licence: **to be confirmed**. Do not treat this as an officially published restaurant dataset without provenance.
- The original raw CSV and complete Colab cleaning notebook are not part of this initial bundle. Reproduction from the supplied analysis-ready dataset is supported.
- Revenue is not profit; no margin, costs, marketing, inventory or footfall data were provided.
- Only two years are available; isolated monthly peaks are not evidence of stable seasonality.

**Suggested GitHub topics:** `data-analysis`, `python`, `pandas`, `tableau`, `business-intelligence`, `data-cleaning`, `sales-analysis`, `portfolio-project`.
