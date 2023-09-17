import pandas as pd

# 读取Excel文件
data = pd.read_excel("C:\/Users/10146/Desktop/事故挖掘/测试/分组/两机型合并数据.xlsx")

# 选择要统计的列和字段
selected_column = '事件类型（主要）'  # 替换为你要统计的列的列名
selected_field = '发动机故障'  # 替换为你要统计的字段的值

# 找出包含指定字段的行
filtered_rows = data[data[selected_column] == selected_field]

# 统计这些行中不同机型的数量
machine_counts = filtered_rows['机型'].value_counts()

# 输出统计结果
print(f"{selected_field}出现的次数：{len(filtered_rows)}")
print("不同机型的统计：")
print(machine_counts)
