import pandas as pd
import jieba
from collections import Counter

# 读取Excel文件
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx')

# 分组并统计各事件类型下事件原因的词汇出现次数
grouped = data.groupby(['事件类型（主要）', '运行阶段'])['事件原因'].apply(list)
word_counts_by_type = {}

for (event_type, run_stage), reasons in grouped.items():
    word_counts = Counter()
    for reason in reasons:
        words = jieba.lcut(reason)
        word_counts.update(words)
    word_counts_by_type[(event_type, run_stage)] = word_counts

# 创建一个空的DataFrame来存储统计结果
result_df = pd.DataFrame(columns=['事件类型（主要）', '运行阶段', '词汇', '出现次数'])

# 将统计结果添加到DataFrame中
for (event_type, run_stage), word_counts in word_counts_by_type.items():
    for word, count in word_counts.items():
        if count > 5:  # 只统计出现次数大于5次的词汇
            result_df = result_df.append({'事件类型（主要）': event_type, '运行阶段': run_stage, '词汇': word, '出现次数': count}, ignore_index=True)

# 将DataFrame写入Excel文件
result_df.to_excel('C:/Users/10146/Desktop/事故挖掘/测试/统计.xlsx', index=False)

import pandas as pd

# 读取Excel文件
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx')

# 统计运行阶段和事件类型两列数据的出现次数
count_by_run_stage_and_event_type = data.groupby(['运行阶段', '事件类型（主要）']).size().reset_index(name='出现次数')

# 将统计结果写入Excel文件
count_by_run_stage_and_event_type.to_excel('C:/Users/10146/Desktop/事故挖掘/测试/统计结果11.xlsx', index=False)


# #  可视化展示
# 
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 读取包含统计结果的DataFrame
# result_df = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/统计结果11.xlsx')
#
# # 设置中文字体
# plt.rcParams['font.sans-serif'] = ['SimHei']
#
# # 选择出现次数最多的前N个词汇进行可视化
# top_n = 10
# top_words_df = result_df.sort_values(by='出现次数', ascending=False).head(top_n)
#
# # 绘制柱状图
# plt.figure(figsize=(10, 6))
# plt.bar(top_words_df['词汇'], top_words_df['出现次数'], color='skyblue')
# plt.xlabel('词汇')
# plt.ylabel('出现次数')
# plt.title('Top {} 出现频率最高的词汇'.format(top_n))
# plt.xticks(rotation=45)
# plt.tight_layout()
#
# # 显示图表
# plt.show()
