# Tableau dashboard

The portfolio contains two interactive Tableau views:

1. **Restaurant Sales Overview:** Total Revenue, Quantity Sold, Average Order Value, Unique Customers, monthly sales trend, yearly comparisons, category and payment-channel performance.
2. **Product & Customer Analysis:** Leading menu items, category trends, customer revenue and transaction frequency.

## Interactive controls
- **Year** (2022, 2023, or both)
- **Category** (five menu categories)
- **Payment channel**, including missing values
- **Chart selections** that filter related views, with a reset by clearing the selection

When opening the workbook in Tableau Public Desktop, verify that each filter card is configured as **Apply to Worksheets → All Using This Data Source**. If chart-click actions are used, clear a selection before interpreting a newly filtered KPI.

## Validation checks
- All years, no chart selection: revenue **340,617.50**, quantity **51,554**, AOV **19.91**, unique customer IDs **100**.
- Year 2023: revenue **166,515.50**, quantity **25,260**, AOV **19.78**, unique customer IDs **100**.
- Category Main Dishes, all years: revenue **160,553**, quantity **10,549**, AOV **46.39**, unique customer IDs **100**.

These checks were matched by the project author in Tableau Public Desktop. Currency symbols are omitted because the dataset does not identify a currency.

**Workbook upload:** The final saved packaged workbook (`.twbx`) is not included in the initial GitHub-ready bundle because the latest version with the six saved filter-scope fixes is still on the author's Windows PC. Add it under `tableau/Restaurant_Sales_Interactive_Final.twbx` once supplied. Do not substitute earlier drafts with incomplete filter configuration.
