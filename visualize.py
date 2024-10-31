# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:14:58 2024

@author: win
"""

import pandas as pd
import matplotlib.pyplot as plt

data={
      'A':[1,2,3,4],
      'B':[4,3,2,1]
      }

df = pd.DataFrame(data)

df.plot(kind='bar', color=['dodgerblue', 'aquamarine'])

plt.show()