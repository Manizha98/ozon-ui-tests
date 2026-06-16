def test_product_name():
    product = "Смартфон"
    assert len(product) > 0


def test_price_is_positive():
    price = 99999
    assert price > 0