import pandas as pd


def filter_and_save_excel(input_file, output_file):
    try:
        # 读取原始Excel文件
        df = pd.read_excel(input_file, engine="openpyxl")

        # 删除包含空值的行
        df = df.dropna(subset=["运行阶段"])

        # 筛选包含“着陆”字段的数据
        filtered_df = df[df["机型"].str.contains("B737")]

        # 保存筛选后的数据到新的Excel文件
        filtered_df.to_excel(output_file, index=False, engine="openpyxl")

        print(f"包含'着陆'字段的非空白行数据已保存到 {output_file}")

    except Exception as e:
        print(f"发生错误：{str(e)}")


# # 调用函数并传入输入和输出文件路径
# input_file_path = "C:/Users/10146/Desktop/事故挖掘/测试/标准化·数据.xlsx"  # 替换为您的输入文件路径
# output_file_path = "C:/Users/10146/Desktop/事故挖掘/测试/分组/B737机型数据.xlsx"  # 替换为您的输出文件路径
# filter_and_save_excel(input_file_path, output_file_path)

import matplotlib.pyplot as plt


def bingtu(input_file, output_image):
    try:
        # 读取 Excel 文件
        df = pd.read_excel(input_file, engine="openpyxl")

        # 统计各个运行阶段的数据数量
        phase_counts = df["事件类型（主要）"].value_counts()

        # 过滤掉数据数量小于2的运行阶段
        filtered_phase_counts = phase_counts[phase_counts >= 10]

        # 计算总数据数量
        total_count = len(df)
        # 计算各个运行阶段的占比
        phase_percentages = (phase_counts / total_count) * 100

        # 打印各个运行阶段的占比数据
        print("各机型的占比数据:")
        for phase, percentage in phase_percentages.items():
            print(f"{phase}机型占比为: {percentage:.2f}%")
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 绘制饼图
        plt.figure(figsize=(8, 8))
        plt.pie(filtered_phase_counts, labels=filtered_phase_counts.index, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # 使饼图圆形
        plt.title('事件类型（主要）占比 ')

        # 保存饼图到文件
        plt.savefig(output_image)

        print(f"运行阶段数据占比饼图 (过滤小于2的数据) 已保存到 {output_image}")

    except Exception as e:
        print(f"发生错误：{str(e)}")

# 调用函数并传入输入文件和输出图像文件路径
input_file_path = "C:/Users/10146/Desktop/事故挖掘/测试/分组/统计阶段1.xlsx"  # 替换为您的输入文件路径
output_image_path = "C:/Users/10146/Desktop/事故挖掘/测试/分组/事件类型.png"   # 替换为输出图像文件路径
bingtu(input_file_path, output_image_path)

