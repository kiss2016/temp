# coding=utf-8
import pandas as pd
import numpy as np
import re

pd.set_option('display.float_format', lambda x: '%.2f' % x)

# data = {"姓名": ["张明艳", "张琦", "霍瑶", "张颖颖", "赵珊", "刘目顺"], "性别": ["女", "女", "女", "女", "女", "男"],
#         "职位": ["后备TPL", "员工", "员工","员工", "员工", "组长"]}
# df = pd.DataFrame(data)
# df.to_excel("../demo1.xlsx", sheet_name="excel测试", index=False, header=True)
file = './demo1.xlsx'
sheetname = 'python'
data = pd.read_excel(file, sheet_name=sheetname)
# print("标题：%s" %rf.columns.values)
# print("第一行: \n{0}".format(rf.loc[0].values))
# print("第二三行: \n{0}".format(rf.loc[[1,2]].values))
df = pd.DataFrame(data, columns=['title', 'info', 'match'])
strdata = '正常'
#result = data.loc[data['title'].str.contains(strdata)]
result = data.loc[data['title'] == strdata]
print(result)
loginnormal = result.iloc[:, 2].values
login = np.array2string(loginnormal)
findstr = re.findall(r'"telnum":"18803041990"', login)
print(findstr)
matchstr = result.iloc[:, 3].values
print(matchstr)
if findstr == matchstr:
        print("The test is OK!")
else:
        print("The test is bad!")


