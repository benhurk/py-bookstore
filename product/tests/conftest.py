import pytest
from product.factories import ProductFactory, CategoryFactory

@pytest.fixture
def product():
    return ProductFactory()

@pytest.fixture
def category():
    return CategoryFactory()
