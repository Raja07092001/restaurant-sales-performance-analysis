# Data preparation, validation and limitations

## Original cleaning work
The original restaurant dataset contained **17,534 transaction records and 9 fields**. These points document the cleaning process performed in Google Colab:

- Checked missingness, row duplicates, order-ID uniqueness, date ranges and category spelling.
- Converted `Order Date` to a datetime type and `Quantity` to an integer-compatible type.
- Validated the financial identity `Order Total = Price × Quantity` on records where all terms were available.
- Recovered **446 missing prices** only when `Quantity` and `Order Total` permitted deterministic calculation (`Price = Order Total / Quantity`). These prices were checked against observed valid unit prices.
- Did **not** guess missing item names where multiple products shared the same category and price.
- Retained **430 transaction records** with no usable price, quantity or total in the cleaned raw dataset, but excluded them from financial analysis. Thus, the analysis-ready dataset has **17,104 records**.

**Reproducibility boundary:** The original raw CSV and step-by-step Colab notebook are not included in this bundle. The `src/` script reproduces analysis and validates the analysis-ready CSV; it does not claim to fully reproduce every earlier cleaning operation without the raw file.

## Remaining missing information in the analysis-ready file

| Field | Missing records | Impact |
|---|---:|---|
| Item | 1,328 | Unknown-item transactions are included in total/category revenue, but excluded from named-product rankings. They represent **25,936** revenue units. |
| Payment Method | 943 | Represent an explicit **Unknown / Missing** group: **18,906.50** revenue units (**5.55%** of total). |
| Price, Quantity, Order Total, Order Date | 0 | Complete for financial and time series computations. |

The analysis-ready dataset has **0 duplicated Order IDs** and **0 financial mismatches** (checked within 0.01). The restaurant's currency is unspecified, so figures are stated in *currency units* rather than dollars or rupees.

## Analytical limitations

- **Revenue, not profit:** No food cost, staffing, discount, refunds, or operating expenses are provided. The project cannot conclude which products are most profitable.
- **No causal variables:** Promotions, footfall, stock availability, service quality, opening hours and competition are missing. Observed declines cannot be causally attributed to any of those factors.
- **Two-year history:** Provides year-over-year comparisons, but is insufficient to establish recurring seasonality confidently.
- **Customer IDs:** 100 distinct identifiers, but the dataset has no demographics, acquisition dates or complete customer histories. Interpret frequency and loyalty conclusions cautiously.
- **Incomplete records:** The 430 financially unusable original rows are omitted from financial KPIs. `Valid Transactions` is therefore not necessarily the total number of operational transactions.
- **Unknown item names:** Attributions of total revenue change to named items are incomplete unless unknown-item changes are reconciled separately.
- **Dataset provenance:** Verify the original data provider and sharing licence before making the transaction-level file public.
