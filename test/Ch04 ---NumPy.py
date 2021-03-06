# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/1/26 17:05
# @File    : Python Test Ch04 ---NumPy.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm

# NumPy 基础：数组和向量化计算
# 在数据处理、清洗、构造子集、过滤、变换以及其他计算中进行快速的向量滑计算
# 常见的数组算法：比sort、unique以及set操作等
# 高效的描述性统计和聚合/概述数据
# 数据排列和相关数据操作，例如对异构数据进行merge和join
  # 使用数组表达式来表明条件逻辑，代替if-elif-else条件分支的循环
# 分组数据的操作（聚合、变换以及函数式操作）

# numpy 比 python 快10 - 100 倍 并且使用内存小
In[7]: import numpy as np
In[8]: my_arr = np.arange(1000000)
In[9]: my_list = list(range(1000000))
In[10]: %time for _ in range(10): my_arr2 = my_arr * 2
Wall time: 148 ms
In[11]: %time for _ in range(10): my_list2 = [x * 2 for x in my_list]
Wall time: 1.34 s
Compiler : 121 ms
Parser   : 256 ms

# 4.1 NumPy ndarray: 多维数组对象（快速灵活的大型数据集容器）
In[12]: import numpy as np
In[13]: data = np.random.randn(2,3)
In[14]: data
Out[14]:
array([[ 0.61080692, -0.18762617, -1.66599111],
       [-0.14889702, -0.57375967, -0.24480561]])
In[15]: data * 10
Out[15]:
array([[  6.10806917,  -1.87626174, -16.65991106],
       [ -1.48897022,  -5.73759674,  -2.44805613]])
In[16]: data + data
Out[16]:
array([[ 1.22161383, -0.37525235, -3.33198221],
       [-0.29779404, -1.14751935, -0.48961123]])

# ndarray的数据类型
# dtype（数据类型）是⼀个特殊的对象，它含有ndarray将⼀块内存解释为特定数据类型所需的信息：
# dtype是NumPy灵活交互其它系统的源泉之⼀。多数情况下，它们直接映射到相应的机器表示，这使得“读写磁盘上的⼆进制数据流”以及“集成低级语⾔代码（如C、Fortran）”等⼯作变得更加
# 简单。数值型dtype的命名⽅式相同：⼀个类型名（如float或int），后⾯跟⼀个⽤于表示各元素位⻓的数字。标准的双精度浮点值（即Python中的float对象）需要占⽤8字节（即64位）。因
# 此，该类型在NumPy中就记作float64#astype。
# astype 方法明确地将一个数组从一个dtype转换成另一个dtype
# int32->int63  /  数字-> 数值
# 调⽤astype总会创建⼀个新的数组（⼀个数据的备份），即使新的dtype与旧的dtype相同。
# NumPy数组的运算
# 数组很重要，因为它使你不⽤编写循环即可对数据执⾏批量运算。
# NumPy⽤户称其为⽮量化（vectorization）。⼤⼩相等的数组之间的任何算术运算都会将运算应⽤到元素级：
In[58]: arr =np.array([[1., 2., 3.],[4., 5., 5.]])
In[59]: arr
Out[59]:
array([[1., 2., 3.],
       [4., 5., 5.]])
In[60]: arr - arr
Out[60]:
array([[0., 0., 0.],
       [0., 0., 0.]])
In[61]: arr * arr
Out[61]:
array([[ 1.,  4.,  9.],
       [16., 25., 25.]])
In[62]: arr / arr
Out[62]:
array([[1., 1., 1.],
       [1., 1., 1.]])
In[63]: arr + arr
Out[63]:
array([[ 2.,  4.,  6.],
       [ 8., 10., 10.]])

# 数组与标量的算术运算会将标量值传播到各个元素：
In[64]: 1 / arr
Out[64]:
array([[1.        , 0.5       , 0.33333333],
       [0.25      , 0.2       , 0.2       ]])
In[65]: arr ** 0.5
Out[65]:
array([[1.        , 1.41421356, 1.73205081],
       [2.        , 2.23606798, 2.23606798]])
In[66]: arr ** 2
Out[66]:
array([[ 1.,  4.,  9.],
       [16., 25., 25.]])

# ⼤⼩相同的数组之间的⽐较会⽣成布尔值数组：(不同⼤⼩的数组之间的运算叫做⼴播)
Out[68]:
array([[ 0.,  4.,  1.],
       [ 7.,  2., 12.]])
In[69]: arr2 > arr
Out[69]:
array([[False,  True, False],
       [ True, False,  True]])
In[70]: arr
Out[70]:
array([[1., 2., 3.],
       [4., 5., 5.]])

# 索引 / 切片

n[114]: x = arr3d[1]
In[115]: x
Out[115]:
array([[ 7,  8,  9],
       [10, 11, 12]])
In[116]: x[0]
Out[116]: array([7, 8, 9])
In[117]: arr
Out[117]: array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
In[118]: arr[1:6]
Out[118]: array([ 1,  2,  3,  4, 64])
In[119]: arr2d
Out[119]:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
In[120]: arr2d[:2]
Out[120]:
array([[1, 2, 3],
       [4, 5, 6]])
In[121]: arr2d[1:2]
Out[121]: array([[4, 5, 6]])
In[122]: arr2d[:1]
Out[122]: array([[1, 2, 3]])
In[123]: arr2d[:2,1:]
Out[123]:
array([[2, 3],
       [5, 6]])
In[124]: arr2d[1,:2]
Out[124]: array([4, 5])
In[125]: arr2d[:2,2]
Out[125]: array([3, 6])
In[126]: arr2d[:,:1]
Out[126]:
array([[1],
       [4],
       [7]])
