import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.decomposition import PCA

# 读取Excel文件并将"事发时间"列解析为日期时间对象
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx', parse_dates=['事发时间'])

# 将"事发时间"列转换为正常的日期时间格式
data['事发时间'] = pd.to_datetime(data['事发时间'], format='%Y/%m/%d %H:%M:%S')

# 输出"事发时间"列
print(data['事发时间'])

from sklearn.feature_extraction.text import TfidfVectorizer

# 读取Excel文件，假设包含"事件类型"、"运行阶段"和"事件原因"三列文本数据


# 将文本数据合并为一个列表
text_data = data['事件类型（主要）'] + ' ' + data['运行阶段'] + ' ' + data['事件原因']

# 创建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 将文本数据转换为TF-IDF向量
tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)

# 打印TF-IDF矩阵的形状（文本数量 x 词汇数量）
print("TF-IDF Matrix Shape:", tfidf_matrix.shape)

# 获取词汇表（单词列表）
vocabulary = tfidf_vectorizer.get_feature_names_out()

# 打印前几个词汇
print("Vocabulary:", vocabulary[:10])

# 打印第一个文本的TF-IDF向量
first_text_tfidf = tfidf_matrix[0]
print("TF-IDF Vector for the First Text:", first_text_tfidf)



# 创建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)

# 使用PCA降维
pca = PCA(n_components=2)
pca_result = pca.fit_transform(tfidf_matrix.toarray())



# 创建一个散点图展示降维后的结果
plt.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.5)

# 在散点图上添加标注
for i, txt in enumerate(data['事件类型（主要）']):
    plt.annotate(txt, (pca_result[i, 0], pca_result[i, 1]))

plt.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.5)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('TF-IDF PCA Visualization')
plt.show()