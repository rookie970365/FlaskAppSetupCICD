"""
Test products vews
"""

from flask import url_for


def test_add_product(client):
    """
    DDDDDDDDDDDDDDDDDDDDD
    :param client:
    :return:
    """
    url = url_for('products_app.add')
    test_data = {
        'product-name': 'Test product name'
    }
    response = client.post(url, data=test_data)
    assert response.status_code < 400, response.text
    assert 'location' in response.headers, response.text
