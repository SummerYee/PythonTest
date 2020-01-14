# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/1/13 18:17
# @File    : Python Test Ch3.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm

# bisect 二分搜索 已排序列表的插值
# bisect.bisect 找到元素应当被插入的位置，并保持序列排序
# bisect.insort 将元素插入到相应的位置


# 内建函数 enumerate  返回(i, value) i是元素的索引 value是元素的值
i = 0
for value in collection:
    # 使用值做点事
    i += 1
# 等价于
for i, value in enumerate(collection):
    # 使用值做点事

# sorted 返回一个根据任意序列中的元素新建的已排序列表

# zip 将列表、元素或其他序列的元素配对，新建一个元组构成的列表

# reversed 将序列的元素倒序排列

# 字典   从序列生成字典
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value

# 字典 默认值
if key in some_dict:
    value = some_dict[key]
else:
    value = default_value
#等价于
value = some_dict.get(key, default_value)


# 集和 是一种无序且元素唯一的容器  set() / {}
# 支持数学上集和的操作
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
# 联合 union() \ |
a.union(b)
Out[101]: {1, 2, 3, 4, 5, 6, 7, 8}
a | b
Out[102]: {1, 2, 3, 4, 5, 6, 7, 8}
# 交集 & \ intersection()
a.intersection(b)
Out[103]: {3, 4, 5}
a & b
Out[104]: {3, 4, 5}
# 在a不在b的元素 a-b
a.difference(b)
Out[105]: {1, 2}
# 在b不在a的元素 b-a
b.difference(a)
Out[106]: {6, 7, 8}
# 所有在a或b的元素，但不是同时在a、b中 a^b
a.symmetric_difference(b)
Out[107]: {1, 2, 6, 7, 8}
b.symmetric_difference(a)
Out[108]: {1, 2, 6, 7, 8}
# a 是否包含 b
a.issubset(b)
Out[109]: False
b.issubset(a)
Out[110]: False
# a、b没有交集返回True
a.isdisjoint(b)
Out[111]: False
# update 将a的内容设置成a、b的并集
In[112]: c = a.copy()  #将a的内容复制到c
In[113]: c |= b        #updat
In[114]: c
Out[114]: {1, 2, 3, 4, 5, 6, 7, 8
# 将a的内容设置成a、b的交集
Out[114]: {1, 2, 3, 4, 5, 6, 7, 8}
In[115]: d = a.copy()
In[116]: d &= b
In[117]: d
Out[117]: {3, 4, 5}

