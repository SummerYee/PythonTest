# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/1/13 16:30
# @File    : Python Test ipython_script_test.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm

def f(x , y , z ):
    return (x + y) / z
a = 5
b = 6
c = 7.5
result = f(a, b, c)


# None 作为默认参数
def add_abd_amybe_multiply(a, b, c=None):
    result = a + b

    if c is not None:
        result = result * c

    return result

# 控制流 if elif else


# for 循环
for value in collection:
    # 用值做些什么
for a, b, c in iterator:
    # 做些什么

# while 循环

# pass “什么都不做”

# range 返回生成一个等差整数序列
# range 产生的整数包含起始但不包含结尾  常用于根据序列的检索遍历

# 三元表达式  value = true-expr if cindition else false-expr
# 等价于    if cindition:
#               value =  true-expr
#           else:
#               value = false-expr

