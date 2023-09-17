import re

# 读取文本文件
input_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/分词结果.txt'
output_file_path = 'C:/Users/10146/Desktop/事故挖掘/测试/cleaned_text.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 去除空格、数字和标点
cleaned_text = re.sub(r'\s+', ' ', text)  # 去除多余的空格
cleaned_text = re.sub(r'\d+', '', cleaned_text)  # 去除数字
cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # 去除标点

# 保存处理后的文本
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_text)
