import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 读取 Excel 文件
def ziduantongji_by_year(excel_file_path, column_names):
    # 读取 Excel 文件并解析日期列
    df = pd.read_excel(excel_file_path, parse_dates=['事发时间'])

    # 提取年份
    df['年份'] = df['事发时间'].dt.year

    # 创建一个子图布局，以适应多个柱状图
    fig, axs = plt.subplots(len(column_names), 1, figsize=(12, 6 * len(column_names)))

    # 定义一组颜色，用于区分不同数据集
    colors = ['skyblue', 'lightcoral', 'lightgreen', 'lightblue', 'pink']

    for i, column_name in enumerate(column_names):
        # 分组统计数据
        grouped = df.groupby(['年份', column_name]).size().unstack().fillna(0)

        # 绘制柱状图
        ax = axs[i]
        grouped.plot(kind='bar', stacked=True, colormap='tab20', ax=ax)
        ax.set_xlabel('年份')
        ax.set_ylabel('数量')
        ax.set_title(f'{column_name}随年份的变化')
        ax.legend(title=column_name)
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 设置中文字体
    font = FontProperties(fname=r'C:\Windows\Fonts\SimHei.ttf', size=12)  # 替换为你的中文字体路径
    plt.xticks(fontproperties=font)
    plt.yticks(fontproperties=font)

    plt.tight_layout()

    # 显示图表
    plt.show()

# # 调用函数进行统计
# excel_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/机型，类型ATA.xlsx'  # 替换为你的 Excel 文件路径
# column_names = ['机型', '事件类型（主要）', '涉及ATA章节']  # 替换为你要统计的列的列名列表
# ziduantongji_by_year(excel_file_path, column_names)

#
# # 单字段统计
# def count_machine_by_year(excel_file_path, output_file_path):
#     # 读取 Excel 文件
#     data = pd.read_excel(excel_file_path)
#
#     # 解析时间列为 Pandas 日期时间类型
#     data['时间'] = pd.to_datetime(data['事发时间'], format='%Y/%m/%d %H:%M:%S')
#
#     # 提取年份信息
#     data['年份'] = data['时间'].dt.year
#
#     # 按年份和机型进行分组，并计数
#     result = data.groupby(['年份', '机型']).size().reset_index(name='数量')
#
#     # 输出结果到新的 Excel 文件
#     result.to_excel(output_file_path, index=False)
#
#     # 调用函数并传入文件路径


# excel_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/机型，类型ATA.xlsx'  # 替换为你的 Excel 文件路径
# output_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/output_file.xlsx'  # 替换为输出文件的路径
# count_machine_by_year(excel_file_path, output_file_path)


def count_machine_by_year(excel_file_path, min_count=5):
    # 读取 Excel 文件
    data = pd.read_excel(excel_file_path)

    # 解析时间列为 Pandas 日期时间类型
    data['时间'] = pd.to_datetime(data['事发时间'], format='%Y/%m/%d %H:%M:%S')

    # 提取年份信息
    data['年份'] = data['时间'].dt.year

    # 按年份和运行阶段进行分组，并计数
    result = data.groupby(['年份', '运行阶段']).size().reset_index(name='数量')

    # 筛选数量大于等于 min_count 的数据
    result = result[result['数量'] >= min_count]

    # 获取所有不同的运行阶段
    machine_types = result['运行阶段'].unique()

    # 定义颜色列表，按顺序分别为黑、白、透明（空白色）
    colors = ['black', 'white', 'none']
    # 创建柱状图
    plt.figure(figsize=(12, 6))

    # 排序运行阶段，按数量降序排列
    sorted_machine_types = sorted(machine_types, key=lambda x: -result[result['运行阶段'] == x]['数量'].sum())

    for machine_type in sorted_machine_types:
        subset = result[result['运行阶段'] == machine_type]
        plt.bar(subset['年份'], subset['数量'], label=machine_type)

    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel('年份')
    plt.ylabel('数量')
    plt.title('每年不同运行阶段的数据数量 '.format(min_count))
    plt.legend(loc='upper right')
    # plt.legend(labels=[], loc='upper left')

    plt.grid(True)
    # # 隐藏图例
    # plt.legend(loc=None)

    # 显示图表
    plt.show()


# # 调用函数并传入文件路径
# excel_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/标准化·数据.xlsx'  # 替换为你的 Excel 文件路径
# count_machine_by_year(excel_file_path)



def count_jieduan_by_year(excel_file_path, min_count=2, top_n=3):
    # 读取 Excel 文件
    data = pd.read_excel(excel_file_path)

    # 解析时间列为 Pandas 日期时间类型
    data['时间'] = pd.to_datetime(data['事发时间'], format='%Y/%m/%d %H:%M:%S')

    # 提取年份信息
    data['年份'] = data['时间'].dt.year

    # 按年份和运行阶段进行分组，并计数
    result = data.groupby(['年份', '运行阶段']).size().reset_index(name='数量')

    # 筛选数量大于等于 min_count 的数据
    result = result[result['数量'] >= min_count]

    # 获取每年前 top_n 名的运行阶段数据
    top_n_data = result.groupby('年份', group_keys=False).apply(lambda x: x.nlargest(top_n, '数量'))

    # 创建柱状图
    plt.figure(figsize=(12, 6))

    for year, subset in top_n_data.groupby('年份'):
        plt.bar(subset['运行阶段'], subset['数量'], label=str(year))

    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel('运行阶段')
    plt.ylabel('数量')
    plt.title('每年前{}名的运行阶段数据数量 (数量大于等于{})'.format(top_n, min_count))
    plt.legend(loc='upper right')
    plt.grid(True)

    # 显示图表
    plt.show()

# 调用函数
excel_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/标准化·数据.xlsx'
count_jieduan_by_year(excel_file_path, min_count=2, top_n=3)