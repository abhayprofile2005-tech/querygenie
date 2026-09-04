import pytest
from app.core.validator import validate_sql, UnsafeQueryError

def test_allows_select():
    assert validate_sql("SELECT * FROM orders") == "SELECT * FROM orders"

def test_blocks_drop():
    with pytest.raises(UnsafeQueryError):
        validate_sql("DROP TABLE orders")

def test_blocks_delete():
    with pytest.raises(UnsafeQueryError):
        validate_sql("DELETE FROM orders WHERE id=1")

def test_blocks_non_select():
    with pytest.raises(UnsafeQueryError):
        validate_sql("UPDATE orders SET amount=0")

def test_blocks_multiple_statements():
    with pytest.raises(UnsafeQueryError):
        validate_sql("SELECT * FROM orders; DROP TABLE orders")