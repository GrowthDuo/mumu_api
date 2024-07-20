import pandas as pd

def get_excel_case_data(interface_type):
    data = pd.read_excel('D:/Software/python/test_api/mumu_api/cases_data/第三章接口测试用例.xlsx')
    interface_type_data = data[data['请求接口类别']==interface_type]
    final_data = []
    # print(interface_type_data)
    start_index = 0
    for i in interface_type_data.index:
        inner_data = {}
        # print("--------"+str(i))
        # for d in interface_type_data.iloc[[i]]:
        for d in interface_type_data.iloc[[start_index]]:
            # print("*****"+str(d))
            inner_data[d] = interface_type_data[d][i]
        final_data.append(inner_data)
        start_index += 1
    # return interface_type_data
    return final_data










# import pandas
# # 使用pandas读取excel文件
# def get_excel_case_pandas(interface_type):
#     pandas.set_option('display.max_columns', None)
#     pandas.set_option('display.max_rows', None)
#     shu = pandas.read_excel("D:/Software/python/test_api/mumu_api/cases_data/第三章接口测试用例.xlsx", sheet_name="Sheet1")
#     interface_type_data = shu[shu['标题'] == interface_type]
#     final_data = []
#     start_index = 0
#     for i in interface_type_data.index:
#         inner_data = {}
#         for d in interface_type_data.iloc[[start_index]]:
#             inner_data[d] = interface_type_data[d][i]
#         final_data.append(inner_data)
#         start_index += 1
#     return final_data
    # # 解析数据
    # find_data = []
    # stat_index = 0
    # # 遍历 DataFrame 中每行数据，即每个 index，使用迭代器 interface_type_data.index
    # # interface_type_data.index迭代的是每一个数据值，然后使用i来接收
    # for i in interface_type_data.index:
    #     # 定义一个空字典来存储该行数据解析后的结果
    #     inner_data = {}
    #     # 遍历该行数据的每个数据，使用迭代器 interface_type_data.iloc[[i]]
    #     # for d in interface_type_data.loc[[i]]:
    #     for d in interface_type_data.iloc[[stat_index]]:
    #         # 以列名为 key，以该行该列的数据为 value，构成一个字典
    #         inner_data[d] = interface_type_data[d][i]
    #         # 将该字典添加到解析后的数据列表中
    #     find_data.append(inner_data)
    #     stat_index += 1
    # # 将读取的 DataFrame 转换成为字典存放在列表后 直接返回给调用函数
    # # print(find_data)
    # return find_data


# if __name__ == '__main__':
#
#     get_excel_case_pandas("购物车")