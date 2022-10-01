import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

# 条件
cond1 = '発生時（始期）'
# cond1 = '発生場所'
cond2 = '施錠関係'

# CSV取得
pref = 'tokyo'
year = 2021
way  = 'syazyounerai'
file_name = os.path.join(os.path.dirname(__file__), pref + '_' + str(year) + way + '.csv')
table = pd.read_csv(file_name, encoding="shift-jis")

# 型変換
table = table[table[cond1] != '不明']
table[cond1] = table[cond1].astype('int')

# グループ化
group_table = table.groupby(cond1)[cond2].value_counts().unstack()

# 描画
group_table.plot.bar()
plt.show()
