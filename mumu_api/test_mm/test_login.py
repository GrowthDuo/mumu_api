import json

import pytest
import requests
from utils import readExcel as um

url = "http://111.231.103.117:8083"

@pytest.mark.parametrize(['id',
                          'titie',
                          'Class',
                          'home',
                          'mode',
                          'login',
                          'readData',
                          'dataFormat',
                          'ExpectedResults'], um.shaiXuan("登录"))
def test_l(id, titie, Class, home, mode,
           login, readData, dataFormat, ExpectedResults):
    if mode == "get":
         requests_get = requests.get(url + home, json.loads(readData))
         assert 200 == requests_get.status_code

# if __name__ == '__main__':
#     pytest.main(["-sv", "test_login.py"])
