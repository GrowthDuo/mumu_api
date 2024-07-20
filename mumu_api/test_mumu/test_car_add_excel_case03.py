import pytest
import requests
import json
from config.const import URL
import utils.mysql_utils as um
import utils.excel_utils as ue

@pytest.fixture()
def get_token(get_cooken):
    return get_cooken
@pytest.fixture()
def get_params():
    return ue.get_excel_case_data("购物车")

def test_cart_add(get_token,get_params):
    params = get_params
    jwt_token = get_token
    for request_data in params:
        print(request_data)
        case_id = request_data['编号']
        title = request_data['标题']
        interface_type = request_data['请求接口类别']
        uri = request_data['请求地址']
        method = request_data['请求方式']
        if_login = request_data['是否需要登录']
        input_data = request_data['输入数据']
        data_type = request_data['数据格式']
        expect = request_data['期望结果']
        print(uri)
        print(input_data)
        headers = {
            "jwt_token": jwt_token
        }
        # requests_post = requests.post(URL + uri, data=input_data, headers=headers)
        # print(requests_post.text)
        # print(headers)
        if if_login == 1:
            if method == "get":
                response = requests.get(URL+uri,
                                        input_data,
                                        headers=headers)
                assert 200 == response.status_code

            elif method == "post":
                if data_type == "form" and title == "添加商品到购物车":
                    response = requests.post(URL+uri,
                                             data=input_data,
                                             headers=headers)
                    print(response.text)
                    assert 200 == response.status_code
                    # assert request_data['预期结果'] == json.loads(response.text)['status']
                elif data_type == "json":
                    response = requests.post(URL+uri, json=json.loads(input_data), headers=headers)
                    assert 200 == response.status_code

        elif if_login == 0:
            if method == "get":
                response = requests.get(URL+uri,
                                        input_data,
                                        headers=headers)
                assert 200 == response.status_code
                assert expect == json.loads(response.text)['status']
            elif method == "post":
                if data_type == "form":
                    response = requests.post(URL+uri,data=input_data)
                    assert 200 == response.status_code

                elif data_type == "json":
                    response = requests.post(URL + uri, json=input_data)
                    assert 200 == response.status_code


  # print(request_data['标题'])
        # if request_data['标题'] == '添加商品到购物车' and request_data['是否需要登录'] == 1 and request_data['请求方式'] == 'form':
        #     print(request_data['标题'])
        #     print(request_data['是否需要登录'])
        #     print(request_data['请求方式'])
        #
        #     headers = {
        #         "jwt_token":  jwt_token
        #     }
        #     print(headers)
        #     requests_post = requests.post(URL + request_data['请求地址'], data=request_data["输入数据"], headers=headers)
        #     assert requests_post.status_code == 200
        #     assert request_data['预期结果'] == json.loads(requests_post.text)['status']