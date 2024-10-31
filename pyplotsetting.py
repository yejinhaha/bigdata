# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:03:49 2024

@author: win
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:33:18 2024

@author: WD
"""

import matplotlib.pyplot as plt
import pandas as pd



#%% 1
data={
      'A':[1,2,3,4],
      'B':[4,3,2,1]}
df=pd.DataFrame(data)
df.plot()
plt.show()

#%% 2

df.plot(kind='bar',title='Example Plot',color=['blue','orange'])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
#%% 3
# 그래프 크기 설정 (가로, 세로)
plt.rcParams['figure.figsize'] = (12, 6)

# 폰트 크기 설정
plt.rcParams['font.size'] = 12

# 그리드 스타일 설정
plt.rcParams['grid.color'] = 'grey'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.5

# 선 스타일 및 색상 설정
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.color'] = 'red'

# 제목과 축 레이블 크기 설정
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
#%% 4
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

#%% 5
import matplotlib.pyplot as plt

data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [2, 3, 5, 10, 8]}

plt.plot('data_x', 'data_y', data=data_dict)
plt.show()
#%%6
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15, 
           fontdict={'family': 'serif', 'color': 'b', 'weight': 'bold', 'size': 14})
plt.ylabel('Y-Axis', labelpad=20, 
           fontdict={'family': 'fantasy', 'color': 'deeppink', 'weight': 'normal', 'size': 'xx-large'})
plt.show()
#%%7
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', loc='right')
plt.ylabel('Y-Axis', loc='top')
plt.show()
#%%8
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)

plt.scatter(x, y)
plt.show()
#%%9
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30 * np.random.rand(n))**2
colors = np.random.rand(n)

plt.scatter(x, y, s=area, c=colors)
plt.show()

#%%10
import matplotlib.pyplot as plt

plt.plot([1], [1], 'o', markersize=20, c='red')
plt.scatter([2], [1], s=20**2, c='#33FFCE')

plt.text(0.5, 1.05, 'plot(markersize=20)', fontdict={'size': 14})
plt.text(1.6, 1.05, 'scatter(s=20**2)', fontdict={'size': 14})
plt.axis([0.4, 2.6, 0.8, 1.2])
plt.show()
#%%11
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()

#%%12
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

plt.pie(ratio, labels=labels, autopct='%.1f%%',
        startangle=260,                  )
plt.show()
#%%13
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0,0,0 , 0.5]
colors = ['silver', 'gold', 'whitesmoke', 'lightgray']

plt.pie(ratio, labels=labels, autopct='%.1f%%',
        startangle=260, counterclock=False, 
                                         )
plt.show()
#%%14
ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0,0,0 , 0.5]


plt.pie(ratio, labels=labels, autopct='%.1f%%',
        startangle=260, counterclock=False, 
        explode=explode, shadow=True, colors=colors)
plt.show()