import pytest
from order.serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer(order):
    serializer = OrderSerializer(order)
    data = serializer.data

    assert 'product' in data
    assert 'total' in data
    assert isinstance(data['product'], list)
    assert len(data['product']) == order.product.count()
    assert data['total'] == sum(p.price for p in order.product.all())

@pytest.mark.django_db
def test_order_serializer_with_multiple_products(order):
    from product.factories import ProductFactory
    new_product = ProductFactory(price=20.00)
    order.product.add(new_product)

    serializer = OrderSerializer(order)
    data = serializer.data

    assert len(data['product']) == 2
    assert data['total'] == sum(p.price for p in order.product.all())
