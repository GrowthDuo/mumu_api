import pandas

def shaiXuan(Class):
    # 显示最大列
    pandas.set_option('display.max_columns', None)
    # 显示最大行
    pandas.set_option('display.max_rows', None)
    excel = pandas.read_excel("D:/Software/python/test_api/mumu_api/cases_data/mumu.xlsx", sheet_name="Sheet1")
    # print(excel)
    ok = excel[excel["class"] == Class]

    # 遍历
    list1 = []
    # 打印的是行数
    for i in ok.index:
        # 每循环一次创建一个字典
        dict1 = {}
        # 将行数作为列名，打印的是列名
        for j in ok.loc[[i]]:
            dict1[j] = ok[j][i]
        list1.append(dict1)
    #print(list1)
    # print(type(list1))
    return list1

# if __name__ == '__main__':
#    shaiXuan("添加商品到购物车")