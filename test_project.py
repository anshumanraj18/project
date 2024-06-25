import pytest
import json
from io import StringIO
from unittest.mock import patch
from project import *

# Test view_customers function
'''def test_view_customers_empty(capsys):
    with patch('builtins.input', side_effect=["5"]):  # Simulate user exit
        view_customers()
        captured = capsys.readouterr()
        assert "Empty List !!!" in captured.out'''

def test_view_customers_non_empty(capsys):
    # Prepare fake data in customers.json
    data = [{"name": "John", "balance": 100, "contact": "123"}]
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

    with patch('builtins.input', side_effect=["5"]):  # Simulate user exit
        view_customers()
        captured = capsys.readouterr()
        assert "John" in captured.out

# Test add_or_remove_customer function
def test_add_or_remove_customer_add():
    # Simulate user input
    with patch('builtins.input', side_effect=["add", "Alice", "100", "123", "5"]):  # Add a customer and exit
        add_or_remove_customer()

    # Check if customer is added
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        assert any(customer['name'] == 'Alice' for customer in data)

def test_add_or_remove_customer_remove():
    # Prepare fake data in customers.json
    data = [{"name": "Alice", "balance": 100, "contact": "123"}]
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

    # Simulate user input
    with patch('builtins.input', side_effect=["remove", "Alice", "5"]):  # Remove a customer and exit
        add_or_remove_customer()

    # Check if customer is removed
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        assert not any(customer['name'] == 'Alice' for customer in data)

# Test update_customer_balance function
def test_update_customer_balance_add():
    # Prepare fake data in customers.json
    data = [{"name": "Alice", "balance": 100, "contact": "123"}]
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

    # Simulate user input
    with patch('builtins.input', side_effect=["Alice", "add", "50", "5"]):  # Add balance to a customer and exit
        update_customer_balance()

    # Check if balance is updated
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        assert data[0]['balance'] == 150

def test_update_customer_balance_reduce():
    # Prepare fake data in customers.json
    data = [{"name": "Alice", "balance": 100, "contact": "123"}]
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

    # Simulate user input
    with patch('builtins.input', side_effect=["Alice", "reduce", "50", "5"]):  # Reduce balance of a customer and exit
        update_customer_balance()

    # Check if balance is updated
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        assert data[0]['balance'] == 50

# Test search_customer function
def test_search_customer_found(capsys):
    # Prepare fake data in customers.json
    data = [{"name": "Alice", "balance": 100, "contact": "123"}]
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

    with patch('builtins.input', side_effect=["Alice", "5"]):  # Simulate user exit
        search_customer()
        captured = capsys.readouterr()
        assert "Alice" in captured.out

def test_search_customer_not_found(capsys):
    # Prepare fake data in customers.json
    data = [{"name": "Alice", "balance": 100, "contact": "123"}]
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

    with patch('builtins.input', side_effect=["Bob", "5"]):  # Simulate user exit
        search_customer()
        captured = capsys.readouterr()
        assert "No customers found" in captured.out

# Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()
    
