# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:36:14 2021

@author: rongyuting
"""

import pandas as pd

from pandas_datareader.data import DataReader

data = DataReader("300005.SZ", "yahoo", "2021-01-01", "2021-06-30")
print(data)