import json

import pytest
import pandas
import requests

import utils.readExcel as um
# 使用数据库原生集合 fixture 进行参数化
url = "http://111.231.103.117:8083"

# 将pandas数据读取到fixture中

@pytest.mark.parametrize(['id',
                          'titie',
                          'Class',
                          'home',
                          'mode',
                          'login',
                          'readData',
                          'dataFormat',
                          'ExpectedResults'],um.shaiXuan("登录")
                         )
def test_login_excel_pandas(id,titie, Class, home, mode, login,  readData, dataFormat, ExpectedResults):
    if mode == "get":
        requests_get = requests.get(url+home, json.loads(readData))
        print(requests_get.status_code)
        assert 200 == requests_get.status_code
        # 双重断言，断言 10000，注意转型

    elif mode == "post":
        if dataFormat == "from":
           response = requests.post(url + home, data=json.loads(readData))
        elif dataFormat == "json":
           response = requests.post(url + home, json=json.loads(readData))
        assert 200 == response.status_code

# if __name__ == '__main__':
#     pytest.main(test_login_excel_pandas())




