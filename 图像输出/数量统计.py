import pandas as pd
import matplotlib.pyplot as plt

def yuchuli(input_file, output_file):
    # 读取Excel文件
    data = pd.read_excel(input_file,header=1)

    # 删除任意一列为空的行
    data = data[(data['飞机设计因素'].notnull()) | (data['人为因素'].notnull()) | (data['手册程序因素'].notnull())|(data['其他环境因素'].notnull())|(data['天气因素'].notnull())|(data['地形因素'].notnull())]

    # 保存为新的Excel文件
    data.to_excel(output_file, index=False)

    print("处理完成，已保存为新的Excel文件:", output_file)

# # 调用函数，并指定输入文件和输出文件名
# input_file = 'C:/Users/10146/Desktop/事故挖掘/测试/测试数据.xlsx'
# output_file = 'C:/Users/10146/Desktop/事故挖掘/测试/原因预处理.xlsx'
# yuchuli(input_file, output_file)

# # 计算单一列数据
# def calculate_not_empty_ratio(excel_path, selected_column):
#     # 读取Excel文件
#     data = pd.read_excel(excel_path)
#
#     # 计算不为空数据的数量
#     not_empty_count = data[selected_column].count()
#
#     # 计算总数据数量
#     total_count = len(data)
#
#     # 计算不为空数据的占比
#     not_empty_ratio = not_empty_count / total_count * 100
#
#     return not_empty_count, not_empty_ratio


def calculate_not_empty_ratio(excel_path, columns):
    data = pd.read_excel(excel_path)
    not_empty_counts = []

    for column in columns:
        not_empty_count = data[column].notnull().sum()
        not_empty_counts.append(not_empty_count)

    total_rows = len(data)
    not_empty_ratios = [count / total_rows * 100 for count in not_empty_counts]

    return not_empty_counts, not_empty_ratios

# 绘制图表
def plot_not_empty_ratios(columns, not_empty_ratios):
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(10, 6))
    plt.bar(columns, not_empty_ratios, color='skyblue', width=0.5)  # 调整width参数以控制柱状图宽度

    plt.xlabel('')
    plt.ylabel('占比 (%)')
    plt.title('各因素占比')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()




excel_path = 'C:/Users/10146/Desktop/事故挖掘/测试/原因预处理.xlsx'  # 替换为你的文件路径
columns_to_calculate = ['人为因素', '天气因素','飞机设计因素', '手册程序因素','其他环境因素','地形因素']  # 替换为你要统计的列名列表

not_empty_counts, not_empty_ratios = calculate_not_empty_ratio(excel_path, columns_to_calculate)
plot_not_empty_ratios(columns_to_calculate, not_empty_ratios)

for i, column in enumerate(columns_to_calculate):
    print(f'{column}列不为空的数量：{not_empty_counts[i]}')
    print(f'{column}列不为空数据的占比：{not_empty_ratios[i]:.2f}%')
    print()
