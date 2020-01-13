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