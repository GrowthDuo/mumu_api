import pandas
'''
iloc使用顺序数字来索引数据，而不能使用字符型的标签来索引数据；注意：这里的顺序数字是指从0开始计数！

loc使用实际设置的索引来索引数据。但行列名为数字时，loc也可以索引数字，但这里的数字不一定从0开始编号，是对应具体行列名的数字！
'''
shu = pandas.read_excel("D:/Software/python/test_api/mumu_api/cases_data/mumu.xlsx", sheet_name="Sheet1")

# 构建查询语句，根据接口类型筛选数据
# 返回结果是一个 DataFrame类型，且是一行一行的数据
interface_type_data = shu[shu["class"] == '购物车']
print(interface_type_data)
# 打印索引值
print(interface_type_data.index) # [2, 3, 4, 5, 6, 7]

# 访问第0行数据
print(interface_type_data.iloc[0])
print(interface_type_data['id'][2]) # [2, 3, 4, 5, 6, 7]
#print(interface_type_data['id'][0]) # id为 [2, 3, 4, 5, 6, 7] 不可以访问0
#print(interface_type_data['id'][1]) # id为 [2, 3, 4, 5, 6, 7] 不可以访问1