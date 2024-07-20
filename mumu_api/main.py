import pytest
if __name__ == '__main__':
     # 登录
     # pytest.main(["-vs", "test_mumu/test_login_mysql_case01.py"])
     # pytest.main(["-vs", "test_mumu/test_login_excel_case02.py"])
     # pytest.main(["-vs", "test_mm/test_login.py"])
     #pytest.main(["-vs", "test_mm/test_add_car.py"])

    # 返回结果是两条元组数据
    # [mysql_data0] ('login_001', '正确的登录', '登录', ' /loginWithJwt', 'get', '0', '{"userName":"imooc","password":"12345678"}', 'params', None)

    # 购物车
     #pytest.main(["-vs", "test_mumu/test_car_add_excel_case03.py"])
     pytest.main(["-vs", "test_mumu/test_car_add_mysql_case04.py"])