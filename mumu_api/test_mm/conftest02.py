# import json
#
# import pytest
# import requests
#
# # 此文件是获取cooken的
#
# @pytest.fixture(scope="session",autouse=True)
# def test_get_cooken():
#     URL = "http://111.231.103.117:8083"
#     home = '/loginWithJwt'
#     login_data = {
#         "userName": "imooc",
#         "password": "12345678"
#     }
#     requests_get = requests.get(URL + home, login_data)
#     # print(requests_get.text)
#     # {"status":10000,"msg":"SUCCESS","data":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3JvbGUiOjIsInVzZXJfaWQiOjksInVzZXJfbmFtZSI6Imltb29jIiwiZXhwIjoxNzg3NzMxNTQzfQ.7vQ-Wl0hgRmDRGDooJr3ixWDQY5rvrrsHuoAPVH6c78"}
#     # print(type(requests_get.text)) # <class 'str'>
#     # 开始解析，拿到data
#     data = json.loads(requests_get.text)
#     jwt_token = data['data']
#     # print(jwt_token)
#     return jwt_token
#
# # if __name__ == '__main__':
# #     get_cooken()