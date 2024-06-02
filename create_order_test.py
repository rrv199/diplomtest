import sender_stend_request
import data
def test_order_number():
    sender_stend_request.post_new_order(data.order_body)
    sender_stend_request.get_order("track_number")
response = sender_stend_request.get_order("track_number")
assert response.status_code == 200
