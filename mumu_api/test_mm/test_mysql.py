import pymysql
import pytest
import requests
import json
from utils import readMysql
url = "http://111.231.103.117:8083"

@pytest.fixture(params=readMysql.run_sql("登录"))
def login(request):
    return request.param

def test_login(login):
    # print(login)
    id = login[0]
    title = login[1]
    Class = login[2]
    home = login[3]
    mode = login[4]
    log = login[5]
    readData = login[6]
    dateFormat = login[7]
    if mode == 'get':
        requests_get = requests.get(url + home, json.loads(readData))
        assert requests_get.status_code == 200
    elif mode == 'post':
        if dateFormat == 'json':
            requests_post = requests.post(url + home, json=json.loads(readData))
            assert requests_post.status_code == 200
        elif dateFormat == 'form':
            response = requests.post(url + home, data=json.loads(readData))
            assert response.status_code == 200




# 使用的pandans读取
@pytest.fixture(params = readMysql.pandasSql("登录"))
def login2(request):
    return request.param


def test_login2(login2):
    # print(login2)
    id = login2[0]
    title = login2[1]
    Class = login2[2]
    home = login2[3]
    mode = login2[4]
    log = login2[5]
    readData = login2[6]
    dateFormat = login2[7]

    if mode == 'get':
        requests_get = requests.get(url + home, json.loads(readData))
        assert requests_get.status_code == 200
    elif mode == 'post':
        if dateFormat == 'json':
            requests_post = requests.post(url + home, json=json.loads(readData))
            assert requests_post.status_code == 200
        elif dateFormat == 'from':
            response = requests.post(url + home, data=json.loads(readData))
            assert response.status_code == 200


if __name__ == '__main__':
    pytest.main(['-sv', 'test_mysql.py/test_login2'])