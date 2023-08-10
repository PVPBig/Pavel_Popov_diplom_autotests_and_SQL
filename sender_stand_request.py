import configuration
import requests
import data


def post_new_order():  # Функция создания нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.KITS_CREATE_ORDER,
                          json=data.body)

def get_new_order_track(): # Функция получения номера заказа
    response = post_new_order()
    order_track = response.json().get('track')
    return order_track

def get_order_by_track():  # Функция получения заказа по его номеру
    return requests.get(configuration.URL_SERVICE+configuration.KITS_GET_ORDER_BY_TRACK+'get_new_order_track()')






