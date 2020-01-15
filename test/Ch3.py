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
# 在a不在b的元素 a-b  difference()
a.difference(b)
Out[105]: {1, 2}
# 在b不在a的元素 b-a  difference()
b.difference(a)
Out[106]: {6, 7, 8}
# 所有在a或b的元素，但不是同时在a、b中 a^b  symmetric_difference()
a.symmetric_difference(b)
Out[107]: {1, 2, 6, 7, 8}
b.symmetric_difference(a)
Out[108]: {1, 2, 6, 7, 8}
# a 是否包含 b  issubset()
a.issubset(b)
Out[109]: False
b.issubset(a)
Out[110]: False
# 如果a包含b返回True   issuperset()
In[121]: a_set = {1, 2, 3, 4, 5}
In[123]: a_set.issuperset({1, 2, 3})
Out[123]: True
# a、b没有交集返回True  isdisjoint()
a.isdisjoint(b)
Out[111]: False
#  将a的内容设置成a、b的并集  update()
In[112]: c = a.copy()  #将a的内容复制到c
In[113]: c |= b        #updat
In[114]: c
Out[114]: {1, 2, 3, 4, 5, 6, 7, 8
# 将a的内容设置成a、b的交集   &=  intersection_update()
Out[114]: {1, 2, 3, 4, 5, 6, 7, 8}
In[115]: d = a.copy()
In[116]: d &= b
In[117]: d
Out[117]: {3, 4, 5}
# 当且仅当两个集合内容完全一模一样 两个集合才相等 ==
In[125]: {1, 2, 3} == {3, 2, 1}
Out[125]: True



#列表推导式
[exper for val in collection if condition]
#等价于
result = []
for val in collection:
    if condition:
        result.append(exper)


# 字典推导式
dict_comp = { key-expr : value-expr for value in collection if collection }

# 集合推导式
sset-comp = { expr for value in collection if collection}

# 嵌套列表推导
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)
# 等价于
In[138]: result = [name for names in all_data for name in names if name.count('e') >= 2]
In[139]: result
Out[139]: ['Steven']

# 正则表达式模块re
import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result
# clean_strings 函数具有更高的复用性和通用性
# 特殊处理
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

In[148]: states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
    ...:          'south   carolina##', 'West virginia?']
In[149]: clean_strings(states)
In[150]: import re
    ...:
    ...:def clean_strings(strings):
    ...:    result = []
    ...:    for value in strings:
    ...:        value = value.strip()
    ...:        value = re.sub('[!#?]', '', value)
    ...:        value = value.title()
    ...:        result.append(value)
    ...:    return result
    ...:
In[151]: clean_strings(states)
Out[151]:
['Alabama',
 'Georgia',
 'Georgia',
 'Georgia',
 'Florida',
 'South   Carolina',
 'West Virginia']
In[152]: def remove_punctuation(value):
    ...:    return re.sub('[!#?]', '', value)
    ...:
    ...:clean_ops = [str.strip, remove_punctuation, str.title]
    ...:
    ...:def clean_strings(strings, ops):
    ...:    result = []
    ...:    for value in strings:
    ...:        for function in ops:
    ...:            value = function(value)
    ...:        result.append(value)
    ...:    return result
    ...:
In[153]: clean_strings(states, clean_ops)
Out[153]:
['Alabama',
 'Georgia',
 'Georgia',
 'Georgia',
 'Florida',
 'South   Carolina',
 'West Virginia']

# 匿名函数 Lambda  通过单个语句生成函数的方式 其结果是返回值
def short_function(x):
    return x * 2
equiv_anon = lambda x: x * 2

def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)

# 柯里化 Currying
def add_numbers(x, y):
    return x + y

add_five = lambda y : add_numbers(5, y) # 柯里化
# 可以使用functools模块可以使用pratial函数简化
from functools import partial
add_five = partial(add_numbers, 5)