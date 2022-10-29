"""
SSSSSSSSSSSSSSSSSSSS
"""
from random import randint

from flask import url_for


def test_get_item(client):
    """
    DDDDDDDDDDDDDDDDDDDDD
    :param client:
    :return:
    """
    # assert 1 == 1
    random_id = randint(1, 100)
    url = url_for('get_item', item_id=random_id)
    # url = f"/items/{random_id}/"
    response = client.get(url)
    assert response.status_code == 200
    # assert response.status == '200 OK'
    assert response.json['item']['id'] == random_id
