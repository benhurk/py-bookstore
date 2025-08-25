import pytest
from order.models import Order
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_order_creation(order):
    assert isinstance(order, Order)
    assert isinstance(order.user, User)

@pytest.mark.django_db
def test_order_products_relationship(order, product):
    assert order.product.first() == product
    assert product.order_set.first() == order
