import pytest
import requests
import json
from config.const import URL

@pytest.fixture(scope="session",autouse=True)
def get_cooken():
    home = URL
    login_uri = "/loginWithJwt"
    login_data = {
        "userName":"imooc",
        "password":"12345678"
    }
    login_response = requests.get(home+login_uri,
                                  login_data)
    data = json.loads(login_response.text)
    jwt_token = data['data']
    return jwt_token
#     headers = {
#         "jwt_token": jwt_token
#     }
#     data_add = {
#         "count":5,
#         "productId":3
#     }
#     cart_add_uri = "/cart/add"
#     # return jwt_token
#     requests_post = requests.post(URL + cart_add_uri, data=data_add, headers=headers)
#     print(requests_post.text)
# if __name__ == '__main__':
#     test_get_login_token()