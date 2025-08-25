import pytest
from product.factories import ProductFactory, CategoryFactory
from product.serializers import ProductSerializer, CategorySerializer

@pytest.mark.django_db
def test_product_serializer(product):
    serializer = ProductSerializer(product)
    assert serializer.data is not None
    assert 'title' in serializer.data
    assert 'price' in serializer.data
    assert 'active' in serializer.data
    assert 'category' in serializer.data

@pytest.mark.django_db
def test_product_serializer_with_categories():
    categories = CategoryFactory.create_batch(2)
    product = ProductFactory(category=categories)
    serializer = ProductSerializer(product)
    assert len(serializer.data['category']) == 2

@pytest.mark.django_db
def test_category_serializer(category):
    serializer = CategorySerializer(category)
    assert serializer.data is not None
    assert 'title' in serializer.data
    assert 'slug' in serializer.data
    assert 'description' in serializer.data
    assert 'active' in serializer.data
