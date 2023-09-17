import pandas as pd


# 读取 Excel 文件
def ziduantongji(excel_file_path, column_name):
    # 读取 Excel 文件
    df = pd.read_excel(excel_file_path)

    # 使用 value_counts() 函数进行统计
    column_counts = df[column_name].value_counts()

    # 选择大于5次的统计结果
    result = column_counts[column_counts > 5]

    return result


# 调用函数进行统计
excel_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx'  # 替换为你的 Excel 文件路径
column_name = '运营人'  # 替换为你要统计的列的列名
result = ziduantongji(excel_file_path, column_name)

# 输出统计结果
print(result)
