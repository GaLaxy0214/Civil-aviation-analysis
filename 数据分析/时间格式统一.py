import pandas as pd

def process_and_save_data(input_file, output_file):
    # 读取 Excel 文件
    data = pd.read_excel(input_file)

    # # 将日期时间列解析为 Pandas 日期时间类型
    # data['事发时间'] = pd.to_datetime(data['事发时间'], format='%Y/%m/%d %H:%M:%S')
    #
    #
    #
    # # 提取年份信息
    # data['年份'] = data['事发时间'].dt.year
    # 将日期时间列解析为 Pandas 日期时间类型
    data['事发时间'] = pd.to_datetime(data['事发时间'], format='%Y/%m/%d %H:%M:%S')

    # 更改日期时间列的格式
    data['时间'] = data['事发时间'].dt.strftime('%Y-%m-%d %H:%M:%S')

    data.to_excel(output_file_path, index=False)

    # # 统计每年的阶段数量
    # yearly_counts = data.groupby(['年份', '事件类型（主要）']).size().unstack(fill_value=0)
    #
    # # 保存结果到 Excel 文件
    # yearly_counts.to_excel(output_file)

# 调用函数进行处理和保存
input_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/机型，类型ATA.xlsx'
output_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/时间格式统一.xlsx'
process_and_save_data(input_file_path, output_file_path)
