# Dataset

The analysis used `restaurant_sales_analysis_ready.csv`, with **17,104 transactions, 9 columns**, and order dates covering **2022-01-01 to 2023-12-31**. The script in `src/` expects this file at `data/restaurant_sales_analysis_ready.csv`.

**Public sharing note:** The transaction-level file is intentionally excluded from this template, pending confirmation that the dataset is permitted to be redistributed. It contains order and customer identifiers. The aggregate tables under `outputs/` are sufficient to inspect the reported findings.

Data dictionary:

| Column | Meaning |
|---|---|
| Order ID | One identifier per recorded order (unique in analysis-ready data) |
| Customer ID | Pseudonymous customer identifier |
| Category | Menu category |
| Item | Ordered product name; may be missing |
| Price | Unit selling price in unspecified currency units |
| Quantity | Units per transaction |
| Order Total | Price multiplied by Quantity |
| Order Date | Date of the transaction |
| Payment Method | Payment channel; may be missing |

The original source and its licence should be credited here before publishing raw data. This portfolio demonstrates analytical techniques on the supplied dataset; it does not independently establish the dataset's provenance or whether customers represent real individuals.
