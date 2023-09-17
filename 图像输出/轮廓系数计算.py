import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 读取数据
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/标准化·数据.xlsx')
# 假设df是包含文本数据的DataFrame，'text_column'是文本列
data = data.dropna(subset=['运行阶段'])
# 提取文本数据所在的列，假设为 "事件原因" 列
text_data = data['运行阶段'].tolist()

# 创建 TF-IDF 模型
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)

# 尝试不同的聚类数量
for n_clusters in range(2, 20):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(tfidf_matrix)
    silhouette_avg = silhouette_score(tfidf_matrix, cluster_labels)
    print(f"当簇数为 = {n_clusters}, 轮廓系数的计算结果为 {silhouette_avg}")
