import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
excel_path = 'C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx'  # 替换为你的文件路径
data = pd.read_excel(excel_path)

# 选择要统计的多列
selected_columns = ['人为因素（空管、机组、维修人员等）']

# 遍历选定的列进行统计和绘图
for selected_column in selected_columns:
    selected_data = data[selected_column]

    # 统计每个数据项的数量
    value_counts = selected_data.value_counts()

    # 计算总数据数量
    total_count = selected_data.count()

    # 计算各个数据项的占比
    proportions = value_counts / total_count

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    plt.pie(proportions, labels=None, autopct='%.1f%%', startangle=140)
    plt.title(f'{selected_column}数据项占比')
    plt.axis('equal')  # 保证饼图为正圆形

    # 显示图表
    plt.show()
