import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/分组/两机型合并数据.xlsx')

# # 使用 fillna() 将 NaN 值替换为 "Unknown"
# data['机型'].fillna('Unknown', inplace=True)
# data['运行阶段'].fillna('Unknown', inplace=True)

# 使用 groupby 进行分组和计数
grouped_data = data.groupby(['机型', '事件类型（主要）']).size().reset_index(name='次数')

# 筛选出次数大于2的数据
filtered_data = grouped_data[grouped_data['次数'] > 2]

# 绘制柱状图
plt.figure(figsize=(10, 6))
colors = {'A320': 'b', 'B737': 'g', 'Unknown': 'r'}  # 为不同机型指定颜色
for key, group in filtered_data.groupby('机型'):
    plt.bar(group['事件类型（主要）'], group['次数'], label=key, color=colors[key])
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置图表标签
plt.xlabel('事件类型（主要）')
plt.ylabel('出现次数')
plt.title('数量大于2的机型在不同运行阶段的出现次数')
plt.legend()

# 显示图表
plt.tight_layout()
plt.show()
