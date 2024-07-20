import pytest
import requests
import json
from config.const import URL

import utils.mysql_utils as um
import utils.excel_utils as ue
# 使用MySQL验证

# 用于登录的信息还有cooke
@pytest.fixture()
def get_token(get_cooken):
    return get_cooken

# 用于筛选类
# 使用MySQL
@pytest.fixture(params= um.get_data_case("购物车")) # 要接收的数据
def mysql_data(request):
    # request是pytest内置的fixture，必须这样写才能传进来
    # 它的作用主要就是用来帮助我们传递参数
    # 如果需要处理数据，要在return上面写处理逻辑和流程，然后再把这个值返回过来
    return request.param


def test_add_mysql_cart(get_token, mysql_data):
    jwt_token = get_token
    print(mysql_data)
    id = mysql_data[0]
    title = mysql_data[1]
    Class = mysql_data[2]
    home = mysql_data[3]
    mode = mysql_data[4]
    login = mysql_data[5]
    readData = mysql_data[6]
    dataFormat = mysql_data[7]
    ExpectedResults = mysql_data[8]
    print(home)
    headers={
        "jwt_token":jwt_token
    }
    if login == 1:
        if mode == "get":
            requests_get = requests.get(URL + home, json.loads(readData))
            print(requests_get.status_code)
            assert 200 == requests_get.status_code
            # 双重断言，断言 10000，注意转型
        elif mode == "post":
            if dataFormat == "form" and title == "添加商品到购物车":
                response = requests.post(URL + home, data=json.loads(readData),headers=headers)
                print(response.text)
                assert 200 == response.status_code
                assert  ExpectedResults == json.loads(response.text)['status']
                assert ExpectedResults == json.loads(response.text)['status']
            elif dataFormat == "json" and title == "添加商品到购物车":
                response = requests.post(URL + home, json=json.loads(readData),headers=headers)
                assert 200 == response.status_code


#
#
# def test_add_cart(get_token, get_params):
#     """
#     购物车添加商品
#     :return:
#     """
#     # 获取筛选好的数据
#     params = get_params
#     # 获取token及登录的信息
#     jwt_token = get_token
#     for requests_data in params:
#         #print("111111111111 :::  ", requests_data[0])
#         id = requests_data["id"]
#         title = requests_data["title"]
#         Class = requests_data["class"]
#         home = requests_data["home"]
#         mode = requests_data["mode"]
#         login= requests_data["login"]
#         readData= requests_data["readData"]
#         dataFormat= requests_data["dataFormat"]
#         ExpectedResults= requests_data["ExpectedResults"]
#         if login == 1:
#             headers = {
#                "jwt_token": jwt_token
#             }
#             if mode == "get":
#                 response = requests.get(URL + home, readData, headers=headers)
#                 assert 200 == response.status_code
#             elif mode == "post":
#                 if dataFormat == "from":
#                     response = requests.post(URL + home, data=readData, headers=headers)
#                     assert 200 == response.status_code
#                 elif dataFormat == "json":
#                     response = requests.post(URL + home, json=readData, headers=headers)
#                     assert 200 == response.status_code
#         elif login == 0:
#             if mode == "get":
#                 response = requests.get(URL + home, )
#                 assert 200 == response.status_code
#             elif mode == "post":
#                 if dataFormat == "from":
#                     response = requests.post(URL+home, data=readData)
#                     assert 200 == response.status_code
#                 elif dataFormat == "json":
#                     response = requests.post(URL + home, json=readData)
#                     assert 200 == response.status_code
# if __name__ == '__main__':
#     pytest.main(test_add_cart(get_token, get_params))