import pandas as pd
import jieba
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文支持的字体

# 读取Excel文件
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx',header=0)

# 选择需要统计的文本列
text_column = '机型'

# 遍历列数据并处理非字符串值
for column in data.columns:
    if data[column].dtype != 'object':
        data[column] = data[column].astype(str)

# 分词并统计词汇出现次数
word_counts = Counter()
for text in data[text_column]:
    words = jieba.lcut(text)  # 使用jieba分词
    word_counts.update(words)

# 提取词汇和出现次数
words = list(word_counts.keys())
counts = list(word_counts.values())

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(words, counts)
plt.xlabel('机型')
plt.ylabel('出现次数')
plt.xticks(rotation=45)
plt.title(f'词汇出现次数统计 - {text_column}')
plt.tight_layout()
plt.show()
