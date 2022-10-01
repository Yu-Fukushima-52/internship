import numpy as np
import pandas as pd
import os

# CSV取得
table = pd.read_csv(os.path.dirname(__file__) + '/tokyo_2021syazyounerai.csv', encoding="shift-jis")
print(table.index)

# cross_table = pd.crosstab(table['市区町村（発生地）'], table['施錠関係'], margins=True, margins_name='小計')
# cross_table['施錠率'] = cross_table['施錠した'] / cross_table['小計']
# print(cross_table)



# '発生場所' == 'その他' の行を削除
# table = table.drop(table.index[table['発生場所'] == 'その他'])
table = table[table['発生場所']!='その他']



condition = [table['発生時（始期）'], table['発生場所'], table['施錠関係']]
cross_table = pd.crosstab(table['市区町村（発生地）'], condition)

print(cross_table.sum().idxmax())
print(cross_table.sum().max())

print(cross_table.max().idxmax())
print(cross_table.max().max())

print(cross_table[cross_table.max().idxmax()].idxmax())

