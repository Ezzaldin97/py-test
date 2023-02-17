from shopping_cart import ShoppingCart
import pytest
from items_prices import ItemPrices
from unittest.mock import Mock


@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("Apple")
    assert cart.size() == 1
    
def test_when_item_added_then_its_in_cart(cart):
    cart.add("Banana")
    assert "Banana" in cart.get_items()
    
def test_when_add_more_than_max_cart_size(cart):
    for _ in range(5):
        cart.add("Apple")
    with pytest.raises(OverflowError):
        cart.add("Apple")

def test_can_get_cart_price(cart):
    cart.add("Apple")
    cart.add("Orange")
    item_db = ItemPrices()
    # use here mocking technique to enforce class method return certain value..
    #item_db.get = Mock(return_value = 1.4)
    # customize using side_effect
    def mock_get_item(item:str):
        if item == "Apple":
            return 1.0
        if item == "Orange":
            return 3.5 
    item_db.get = Mock(side_effect = mock_get_item)
    assert cart.get_total_price(item_db) == 4.5