import pandas
import pymysql
import pandas as pd

def get_sql_conn():
    # 编辑数据库连接对象
    dn_info = {
        'host' : '127.0.0.1',
        'port': 3306,
        'user' : 'root',
        'password' : '123456',
        'db' : 'xulihao',
        'charset' : 'utf8'
    }

    # 创建连接   **dn_info 按照字典的形式解析
    conn = pymysql.connect(**dn_info)
    return conn

def run_sql(ziDuan):

    # 获取连接对象
    conn = get_sql_conn()
    # 获取游标
    cursor = conn.cursor()
    # 定义sql语句
    sql = 'select * from mumu where Class = "{}"'.format(ziDuan)
    # 执行sql语句
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    print(result)
    return result



# 使用pandas读取
def pandasSql(interface_type):
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.max_rows', None)
    # 获取数据库连接
    conns = get_sql_conn()
    # sql = 'select * from mumu where Class = "{}"'.format(Class)
    # 查询语句
    sql2 = "select * from mumu where Class = '{}'".format(interface_type)
    # 读取sql语句
    read_sql = pd.read_sql(sql2, conns)
    # 打印查询结果
    #print(read_sql)
    # print(type(read_sql))

    # 定义一个列表
    readData = []

    # 遍历查询结果
    for i in read_sql.index:
        # 定义一个字典
        zd = {}
        #  列  # 将excel的行名作为列名，打印的是列名ilo
        for j in read_sql.loc[[i]]:
            zd[j] = read_sql[j][i]
        readData.append(zd)
    print(type(readData))
    return readData


if __name__ == '__main__':
    # 调用test_pandas函数
    pandasSql('登录')