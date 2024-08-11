import data
import config
import requests

def create_new_order(body): #создание заказа
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_order_by_track_number(number): #делает поиск заказа по трек-номеру
    return requests.get(config.URL_SERVICE + config.ORDER_BY_TRACK_PATH + str(number['track']))

def get_track_status_code(): #проверка что на полученный запрос мы получаем код ответа 200
    new_order = create_new_order(data.order_body)
    print(new_order.status_code)
    trnum = new_order.json()
    ord = get_order_by_track_number(trnum)

    assert ord.status_code == 200



