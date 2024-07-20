# mysql 相关的工具方法
import pandas as pd
import pymysql

# 连接mysql
def connect_mysql():
  db_info = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'xulihao',
    'charset': 'utf8'
  }
  #  **dn_info 按照字典的形式解析
  conn = pymysql.connect(**db_info)
  return conn

def get_data_case(interface_type):
      conn = connect_mysql()
      sql = "select * from mumu where Class = '{}'".format(interface_type)
      # Cursor对象即游标对象，它主要负责执行SQL语句。
      cursor = conn.cursor()
      # 执行sql语句
      cursor.execute(sql)
      fetchall = cursor.fetchall()
      return fetchall



# 使用pandas读取mysql数据
'''
该段代码的作用是从数据库中读取某个表的数据，并将其转换成列表形式，以便后续使用。
'''
# 定义一个函数，接受一个参数 interface_type，表示接口类型
def get_mysql_case_pandas(interface_type):
     # 连接到 MySQL 数据库
      conn = connect_mysql()
     # 构建 SQL 查询语句，根据接口类型筛选数据
      sql = "select * from mumu where Class = '{}'".format(interface_type)
      # # 使用 pd.read_sql 方法从数据库中读取某个表的数据并存储到 DataFrame 中
      interface_type_data = pd.read_sql(sql, conn)
      # print(interface_type_data)
      # 返回结果是一个 DataFrame类型，且是一行一行的数据, 构建查询语句，根据接口类型筛选数据
      # print(interface_type_data)
      # 解析数据
      #print(interface_type_data)
      # print(type(interface_type_data)) #<class 'pandas.core.frame.DataFrame'>
      # 开始解析
     # 定义一个空列表来存储解析后的数据
      find_data = []
     # 遍历 DataFrame 中每行数据，即每个 index，使用迭代器 interface_type_data.index
     # interface_type_data.index迭代的是每一个数据值，然后使用i来接收
      for i in interface_type_data.index:
          # 定义一个空字典来存储该行数据解析后的结果
          inner_data ={}
          # 遍历该行数据的每个数据，使用迭代器 interface_type_data.iloc[[i]]
          # 方法1：
          #for d in interface_type_data.iloc[[i]]:
          # 方法2：
          for d in interface_type_data.loc[[i]]:
              # 以列名为 key，以该行该列的数据为 value，构成一个字典
              inner_data[d] = interface_type_data[d][i]
              # 将该字典添加到解析后的数据列表中
          find_data.append(inner_data)
     # 将读取的 DataFrame 转换成为字典存放在列表后 直接返回给调用函数
      return find_data

# if __name__ == '__main__':
#     get_mysql_case_pandas("登录")