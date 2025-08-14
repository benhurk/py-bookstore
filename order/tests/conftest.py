import pytest
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory

@pytest.fixture
def user():
    return UserFactory()

@pytest.fixture
def product():
    return ProductFactory()

@pytest.fixture
def order(user, product):
    order = OrderFactory(user=user)
    order.product.add(product)
    return order
