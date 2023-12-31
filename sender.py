import requests
import data
import configuration

# СОЗДАЮ КУРЬЕРА
#def post_new_courier(body):
    #return requests.post(configuration.URL + configuration.URL_POST_COURIER,
                         #json=body)

# СОЗДАЮ ЗАКАЗ
def create_new_order(order_body):
    return requests.post(configuration.URL + configuration.URL_POST_ORDER,
                         json=order_body)

# вытаскиваю трек
def track_new_order(track):
    return requests.get(configuration.URL + configuration.URL_GET_ORDER_BY_TRACK, params=track)
