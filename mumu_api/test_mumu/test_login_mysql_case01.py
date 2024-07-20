import json

import pytest
import requests

from utils.mysql_utils import get_data_case,get_mysql_case_pandas
# 使用数据库原生集合 fixture 进行参数化
url = "http://111.231.103.117:8083"

# 用fixture，把测试数据和方法关联起来

@pytest.fixture(params=get_data_case("登录")) # 要接收的数据
def mysql_data(request):
    # request是pytest内置的fixture，必须这样写才能传进来
    # 它的作用主要就是用来帮助我们传递参数
    # 如果需要处理数据，要在return上面写处理逻辑和流程，然后再把这个值返回过来
    return request.param
@pytest.mark.skip
def test_login(mysql_data):
    # 把数据和测试方法关联起来
    # 把数据传给测试方法

    id= mysql_data[0]
    title= mysql_data[1]
    Class= mysql_data[2]
    home= mysql_data[3]
    mode= mysql_data[4]
    login= mysql_data[5]
    readData= mysql_data[6]
    dataFormat= mysql_data[7]
    ExpectedResults= mysql_data[8]
    print(home)
    if mode == "get":
        requests_get = requests.get(url+home, json.loads(readData))
        print(requests_get.status_code)
        assert 200 == requests_get.status_code
        # 双重断言，断言 10000，注意转型

    elif mode == "post":
        if dataFormat== "from":
           response = requests.post(url + home, data=json.loads(readData))
        elif dataFormat == "json":
           response = requests.post(url + home, json=json.loads(readData))
        assert 200 == response.status_code

print()
print()
print("-------使用pandas读取MySQL数据-------------")
print()
print()
# 将pandas数据读取到fixture中
@pytest.fixture(params=get_mysql_case_pandas("登录"))
def get_mysql_login_pandas(request):
    return request.param

# 使用pandas实现登录测试
@pytest.mark.skip
def test_login_pandas(get_mysql_login_pandas):
   # print(get_mysql_login_pandas) 返回结果是字典形式
   #{'id': 'login_001', 'title': '正确的登录', 'Class': '登录', 'home': '/loginWithJwt', 'mode': 'get', 'login': '0', 'readData': '{"userName":"imooc","password":"12345678"}', 'dataFormat': 'params', 'ExpectedResults': None}
    if get_mysql_login_pandas['mode'] == "get":
        response = requests.get(url + get_mysql_login_pandas['home'],
                                json.loads(get_mysql_login_pandas['readData']))
        assert 200 == response.status_code
    elif get_mysql_login_pandas['mode'] == "post":
        if get_mysql_login_pandas['dataFormat'] == "from":
            response = requests.get(url + get_mysql_login_pandas['home'],
                                    data = json.loads(get_mysql_login_pandas['readData']))
        elif get_mysql_login_pandas['dataFormat'] == "params":
            response = requests.get(url + get_mysql_login_pandas['home'],
                                    json = json.loads(get_mysql_login_pandas['readData']))
        assert 200 == response.status_code
