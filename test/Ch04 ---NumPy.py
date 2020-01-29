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