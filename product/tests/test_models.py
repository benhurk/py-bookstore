import pytest
from product.models import Product, Category
from product.factories import ProductFactory, CategoryFactory

@pytest.mark.django_db
def test_product_creation(product):
    assert isinstance(product, Product)
    assert product.title is not None
    assert product.price is not None
    assert product.active is True

@pytest.mark.django_db
def test_product_with_categories():
    categories = CategoryFactory.create_batch(3)
    product = ProductFactory(category=categories)
    assert product.category.count() == 3
    assert list(product.category.all()) == categories

@pytest.mark.django_db
def test_category_creation(category):
    assert isinstance(category, Category)
    assert category.title is not None
    assert category.slug is not None
    assert category.description is not None
