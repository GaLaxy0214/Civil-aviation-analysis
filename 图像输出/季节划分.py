import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 读取文本文件，每行是日期数据
with open('C:/Users/10146/Desktop/民航事故/数据/月份.txt', 'r',encoding='utf-8') as f:
    date_lines = f.readlines()

# 转换为日期类型
date_list = [datetime.strptime(line.strip(), "%Y/%m/%d") for line in date_lines]

# 定义季节与月份的映射关系
season_mapping = {
    '春季': [3, 4, 5],
    '夏季': [6, 7, 8],
    '秋季': [9, 10, 11],
    '冬季': [12, 1, 2]
}

# 根据日期映射到季节
season_list = []
for date in date_list:
    month = date.month
    for season, months in season_mapping.items():
        if month in months:
            season_list.append(season)
            break

# 统计每个季节的数量
season_counts = pd.Series(season_list).value_counts()
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制柱状图
plt.bar(season_counts.index, season_counts.values, color='skyblue')
plt.xlabel('季节')
plt.ylabel('数量')
plt.title('季节统计')
plt.show()
