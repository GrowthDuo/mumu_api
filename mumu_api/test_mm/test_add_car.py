import pytest
import requests

from utils import readExcel
from test_mm import conftest02

URL = "http://111.231.103.117:8083"
@pytest.fixture()
def get_jwt_token():
    return conftest02.test_get_cooken

@pytest.fixture()
def get_pandans_excel():
    return readExcel.shaiXuan("购物车")

def test_add_cart(get_jwt_token, get_pandans_excel):
    # 获取cooken
    jwt_token = get_jwt_token

    # 获取返回的数据
    params = get_pandans_excel
    print(params)
    print(jwt_token)
    for requests_data in params:
        # print(requests_data)
        # # print("111111111111 :::  ", requests_data[0])
        id = requests_data["id"]
        title = requests_data["title"]
        # Class = requests_data["Class"]
        home = requests_data["home"]
        mode = requests_data["mode"]
        login = requests_data["login"]
        readData = requests_data["readData"]
        dataFormat = requests_data["dataFormat"]
        ExpectedResults = requests_data["ExpectedResults"]
        if login == 1:
            headers = {
                "jwt_token": jwt_token
            }
            if mode == "get" and title == "添加商品到购物车":
                response = requests.get(URL + home, readData, headers=headers)
                assert 200 == response.status_code
            elif mode == "post" and title == "添加商品到购物车":
                 if dataFormat == "from":
                     response = requests.post(URL + home, data=readData, headers=headers)
                     assert 200 == response.status_code
                 elif dataFormat == "json":
                     response2 = requests.post(URL + home, json=readData, headers=headers)
                     assert 200 == response2.status_code

    #

if __name__ == '__main__':
    pytest.main(["-sv", "test_add_car.py"])

