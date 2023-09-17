import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 读取文本文件，每行是日期数据
with open('C:/Users/10146/Desktop/民航事故/数据/月份.txt', 'r',encoding='utf-8') as f:
    date_lines = f.readlines()

# 转换为日期类型
date_list = [datetime.strptime(line.strip(), "%Y/%m/%d") for line in date_lines]

# 定义月份的映射关系
months_mapping = {
    1: '1月',
    2: '2月',
    3: '3月',
    4: '4月',
    5: '5月',
    6: '6月',
    7: '7月',
    8: '8月',
    9: '9月',
    10: '10月',
    11: '11月',
    12: '12月'
}

# 根据日期映射到月份
month_list = [months_mapping[date.month] for date in date_list]

# 统计每个月的数量
month_counts = pd.Series(month_list).value_counts()
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制柱状图
plt.bar(month_counts.index, month_counts.values, color='skyblue')
plt.xlabel('月份')
plt.ylabel('数量')
plt.title('每月数据统计')
plt.xticks(rotation=45)
plt.tight_layout()

# 显示图表
plt.show()
