import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt

# 读取Excel数据
data = pd.read_excel("C:/Users/10146/Desktop/事故挖掘/测试/分组/A320精简数据.xlsx")

# 选择需要的文本字段作为特征
features = ['运行阶段', '事件类型（主要）', '涉及ATA章节']  # 根据数据的实际情况修改字段名

# 创建数据帧
df = data[features]

# 对分类字段进行标签编码
label_encoder = LabelEncoder()
for feature in features:
    df[feature] = label_encoder.fit_transform(df[feature])

# 对数值字段进行标准化处理（如果有的话）
scaler = StandardScaler()
if '数值字段' in df.columns:
    df['数值字段'] = scaler.fit_transform(df['数值字段'].values.reshape(-1, 1))

# 选择K值（使用肘部法则）
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(df)
    inertia.append(kmeans.inertia_)

# 绘制肘部法则图
plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), inertia, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.grid(True)
plt.show()

# 假设选择K=3
k = 5

# 训练K均值模型
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(df)

# 获取簇标签
cluster_labels = kmeans.labels_

# 将簇标签添加到原始数据
data['Cluster'] = cluster_labels

# 打印每个簇的统计信息
cluster_counts = data['Cluster'].value_counts()
print("Cluster Counts:")
print(cluster_counts)

# 分析聚类结果
for cluster_id in range(k):
    cluster_data = data[data['Cluster'] == cluster_id]
    print(f"\nCluster {cluster_id + 1}:")
    print(cluster_data[features])  # 打印每个簇的原始特征数据
