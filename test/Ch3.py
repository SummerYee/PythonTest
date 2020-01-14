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
