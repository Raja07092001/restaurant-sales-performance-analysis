"""Smoke tests for numerical validation and reproducible KPI generation."""
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from analyze_restaurant_sales import generate_outputs, load_and_validate


def test_known_transaction_and_revenue(tmp_path):
    x = pd.DataFrame({
        "Order ID": ["A", "B"], "Customer ID": ["C1", "C2"],
        "Category": ["Drinks", "Starters"], "Item": ["Water", None],
        "Price": [1.0, 5.0], "Quantity": [2, 3],
        "Order Total": [2.0, 15.0], "Order Date": ["2022-01-01", "2023-01-01"],
        "Payment Method": ["Cash", None]})
    p = tmp_path / "sample.csv"
    x.to_csv(p, index=False)
    k = generate_outputs(load_and_validate(p), tmp_path / "out")
    assert k["total_revenue"] == 17.0
    assert k["transactions"] == 2
    assert k["missing_item_revenue"] == 15.0
    assert k["missing_payment_revenue"] == 15.0


def test_invalid_order_total_raises(tmp_path):
    p = tmp_path / "invalid.csv"
    pd.DataFrame({
        "Order ID": ["A"], "Customer ID": ["C1"], "Category": ["Drinks"],
        "Item": ["Water"], "Price": [1.0], "Quantity": [2],
        "Order Total": [9.0], "Order Date": ["2022-01-01"],
        "Payment Method": ["Cash"]}).to_csv(p, index=False)
    with pytest.raises(ValueError, match="Order Total"):
        load_and_validate(p)
