import pandas as pd

def yuchuli(input_file, output_file):
    # 读取Excel文件
    data = pd.read_excel(input_file,header=1)

    # 删除任意一列为空的行
    data = data[(data['机型'].notnull()) | (data['运行阶段'].notnull()) | (data['事件类型（主要）'].notnull())]

    # 保存为新的Excel文件
    data.to_excel(output_file, index=False)

    print("处理完成，已保存为新的Excel文件:", output_file)

# 调用函数，并指定输入文件和输出文件名
input_file = 'C:/Users/10146/Desktop/事故挖掘/测试/测试数据.xlsx'
output_file = 'C:/Users/10146/Desktop/事故挖掘/测试/标准化·数据.xlsx'
yuchuli(input_file, output_file)
"""
        将事件原因输出txt
        """

# 从Excel文件读取数据
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx')

# 提取“事件原因”列的数据
event_reasons = data['事件原因']

# 将提取的数据写入txt文件
with open('C:/Users/10146/Desktop/事故挖掘/测试/事件原因.txt', 'w', encoding='utf-8') as file:
    for reason in event_reasons:
        file.write(reason + '\n')

print("数据已提取并写入文件")


import pandas as pd
import jieba
from collections import Counter

# 读取Excel文件
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx')

# 分组并统计各事件类型下事件原因的词汇出现次数
grouped = data.groupby('事件类型（主要）','运行阶段')['事件原因'].apply(list)
word_counts_by_type = {}

# for event_type, reasons in grouped.items():
#     word_counts = Counter()
#     for reason in reasons:
#         words = jieba.lcut(reason)
#         word_counts.update(words)
#     word_counts_by_type[event_type] = word_counts

for (event_type, run_stage), reasons in grouped.items():
    word_counts = Counter()
    for reason in reasons:
        words = jieba.lcut(reason)
        word_counts.update(words)
    word_counts_by_type[(event_type, run_stage)] = word_counts

# # 输出各事件类型下各词汇出现次数
# for event_type, word_counts in word_counts_by_type.items():
#     print(f"事件类型: {event_type}")
#     for word, count in word_counts.items():
#         print(f"  {word}: {count}")

# 创建一个空的DataFrame来存储统计结果
# result_df = pd.DataFrame(columns=['事件类型（主要）', '词汇', '出现次数'])

# # 将统计结果添加到DataFrame中
#
# for event_type, word_counts in word_counts_by_type.items():
#     for word, count in word_counts.items():
#         if count > 5:  # 只统计出现次数大于5次的词汇
#             result_df = result_df.append({'事件类型（主要）': event_type, '词汇': word, '出现次数': count}, ignore_index=True)

# 创建一个空的DataFrame来存储统计结果
result_df = pd.DataFrame(columns=['事件类型（主要）', '运行阶段', '词汇', '出现次数'])

# 将统计结果添加到DataFrame中
for (event_type, run_stage), word_counts in word_counts_by_type.items():
    for word, count in word_counts.items():
        if count > 5:  # 只统计出现次数大于5次的词汇
            result_df = result_df.append({'事件类型（主要）': event_type, '运行阶段': run_stage, '词汇': word, '出现次数': count}, ignore_index=True)




# 将DataFrame写入Excel文件
result_df.to_excel('C:/Users/10146/Desktop/事故挖掘/测试/统计.xlsx', index=False)
