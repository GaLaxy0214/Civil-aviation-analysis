import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/统计结果11.xlsx')


# 读取Excel文件
data1 = pd.read_excel('C:/Users/10146/Desktop/新数据的整理/统一数据.xlsx',header = 1)
# 选择要统计的列名
column_to_count = '运行阶段'  # 替换成实际的列名

# 使用value_counts()函数进行统计
count_result = data1[column_to_count].value_counts()

# 输出统计结果
print(count_result)


# 按出现次数降序排序，并选择前8名
top_n = 20
top_data = data.sort_values(by='出现次数', ascending=False).head(top_n)
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(top_data['运行阶段'] + ' - ' + top_data['事件类型（主要）'], top_data['出现次数'], color='skyblue')
plt.xlabel('运行阶段 - 事件类型（主要）')
plt.ylabel('出现次数')
plt.title('出现次数前{}名的数据'.format(top_n))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 显示图表
plt.show()
