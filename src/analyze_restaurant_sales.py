"""Reproduce the restaurant sales KPIs and summary tables.

Usage:
    python src/analyze_restaurant_sales.py --input data/restaurant_sales_analysis_ready.csv

The analysis-ready CSV is intentionally not bundled in this public-ready
repository template until dataset reuse and privacy permissions are confirmed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "Order ID", "Customer ID", "Category", "Item", "Price",
    "Quantity", "Order Total", "Order Date", "Payment Method",
}


def load_and_validate(path: Path) -> pd.DataFrame:
    """Load analysis-ready transactions and enforce financial integrity."""
    df = pd.read_csv(path, parse_dates=["Order Date"])
    missing_columns = REQUIRED_COLUMNS.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Missing columns: {sorted(missing_columns)}")
    if df["Order Date"].isna().any():
        raise ValueError("Some order dates could not be parsed")
    for col in ("Price", "Quantity", "Order Total"):
        if df[col].isna().any():
            raise ValueError(f"Analysis-ready dataset contains missing {col}")
        if (df[col] <= 0).any():
            raise ValueError(f"Analysis-ready dataset contains non-positive {col}")
    if df["Order ID"].isna().any() or df["Order ID"].duplicated().any():
        raise ValueError("Order IDs must be present and unique")
    bad_totals = (df["Order Total"] - df["Price"] * df["Quantity"]).abs() > 0.01
    if bad_totals.any():
        raise ValueError(f"Order Total != Price × Quantity in {bad_totals.sum()} rows")
    return df


def generate_outputs(df: pd.DataFrame, output_dir: Path) -> dict:
    """Write summary tables and return headline KPIs."""
    output_dir.mkdir(parents=True, exist_ok=True)
    total_revenue = float(df["Order Total"].sum())
    transactions = int(df["Order ID"].nunique())
    kpis = {
        "transactions": transactions,
        "total_revenue": round(total_revenue, 2),
        "quantity_sold": int(df["Quantity"].sum()),
        "average_order_value": round(total_revenue / transactions, 2),
        "unique_customer_ids": int(df["Customer ID"].nunique()),
        "missing_item_rows": int(df["Item"].isna().sum()),
        "missing_item_revenue": round(float(df.loc[df["Item"].isna(), "Order Total"].sum()), 2),
        "missing_payment_rows": int(df["Payment Method"].isna().sum()),
        "missing_payment_revenue": round(float(df.loc[df["Payment Method"].isna(), "Order Total"].sum()), 2),
    }
    (output_dir / "headline_kpis.json").write_text(json.dumps(kpis, indent=2) + "\n", encoding="utf-8")

    work = df.assign(Year=df["Order Date"].dt.year,
                     Month=df["Order Date"].dt.to_period("M").astype(str),
                     Item_Label=df["Item"].fillna("Unknown Item"),
                     Payment_Label=df["Payment Method"].fillna("Unknown / Missing"))

    yearly = work.groupby("Year", as_index=False).agg(
        Transactions=("Order ID", "nunique"), Quantity_Sold=("Quantity", "sum"),
        Revenue=("Order Total", "sum"))
    yearly["Average_Order_Value"] = yearly["Revenue"] / yearly["Transactions"]
    yearly["Revenue_YoY_Percent"] = yearly["Revenue"].pct_change() * 100
    yearly.to_csv(output_dir / "yearly_summary.csv", index=False, float_format="%.2f")

    monthly = work.groupby("Month", as_index=False).agg(
        Transactions=("Order ID", "nunique"), Quantity_Sold=("Quantity", "sum"),
        Revenue=("Order Total", "sum"))
    monthly.to_csv(output_dir / "monthly_summary.csv", index=False)

    category = work.groupby("Category", as_index=False).agg(
        Transactions=("Order ID", "nunique"), Quantity_Sold=("Quantity", "sum"),
        Revenue=("Order Total", "sum"))
    category["Revenue_Share_Percent"] = category["Revenue"] / total_revenue * 100
    category.sort_values("Revenue", ascending=False).to_csv(
        output_dir / "category_summary.csv", index=False, float_format="%.2f")

    payment = work.groupby("Payment_Label", as_index=False).agg(
        Transactions=("Order ID", "nunique"), Revenue=("Order Total", "sum"))
    payment["Revenue_Share_Percent"] = payment["Revenue"] / total_revenue * 100
    payment.sort_values("Revenue", ascending=False).to_csv(
        output_dir / "payment_summary.csv", index=False, float_format="%.2f")

    item = work.groupby(["Category", "Item_Label"], as_index=False).agg(
        Transactions=("Order ID", "nunique"), Quantity_Sold=("Quantity", "sum"),
        Revenue=("Order Total", "sum"))
    item.sort_values("Revenue", ascending=False).to_csv(
        output_dir / "item_summary_including_unknown.csv", index=False)

    item_yoy = work.groupby(["Item_Label", "Year"])["Order Total"].sum().unstack(fill_value=0)
    item_yoy = item_yoy.rename(columns={2022: "Revenue_2022", 2023: "Revenue_2023"})
    if {"Revenue_2022", "Revenue_2023"}.issubset(item_yoy.columns):
        item_yoy["Revenue_Change"] = item_yoy["Revenue_2023"] - item_yoy["Revenue_2022"]
        item_yoy["Revenue_Change_Percent"] = (
            item_yoy["Revenue_Change"] / item_yoy["Revenue_2022"].replace(0, float("nan")) * 100)
    item_yoy.reset_index().sort_values("Revenue_Change").to_csv(
        output_dir / "item_yoy.csv", index=False, float_format="%.2f")

    customers = work.groupby("Customer ID", as_index=False).agg(
        Transactions=("Order ID", "nunique"), Revenue=("Order Total", "sum"))
    customers["AOV"] = customers["Revenue"] / customers["Transactions"]
    customers.sort_values("Revenue", ascending=False).to_csv(
        output_dir / "customer_summary.csv", index=False, float_format="%.2f")

    return kpis


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/restaurant_sales_analysis_ready.csv"))
    parser.add_argument("--output", type=Path, default=Path("outputs"))
    args = parser.parse_args()
    df = load_and_validate(args.input)
    kpis = generate_outputs(df, args.output)
    print(json.dumps(kpis, indent=2))


if __name__ == "__main__":
    main()
