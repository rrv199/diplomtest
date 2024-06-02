import configuration
import requests
import data

def post_new_courier(new_courier_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER,
                         json=new_courier_body,
                         headers=data.headers)

def post_log_courier(log_courier_body):
    return requests.post(configuration.URL_SERVICE + configuration.LOG_COURIER,
                         json=log_courier_body,
                         headers=data.headers)

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body,
                         headers=data.headers)
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body,
                         headers=data.headers)

order_response = post_new_order(data.order_body)
print (order_response.json())
track_number =(order_response.json()['track'])
print (track_number)
track=str(track_number)




def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_NUMBER + track)
response = get_order(track_number)
print(response.status_code)



