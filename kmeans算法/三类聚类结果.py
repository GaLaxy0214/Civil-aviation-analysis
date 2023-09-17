from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# 生成模拟数据
X, y = make_blobs(n_samples=1000, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)

# 增加数据点到第一个簇
cluster1_x = np.random.normal(2, 0.2, 300)
cluster1_y = np.random.normal(3, 0.2, 300)

# 增加数据点到第二个簇（更加集中）
cluster2_x = np.random.normal(0, 0.1, 500)
cluster2_y = np.random.normal(0, 0.3, 500)

# 增加数据点到第三个簇
cluster3_x = np.random.normal(1, 0.3, 50)
cluster3_y = np.random.normal(1, 0.4, 50)

X = np.concatenate((X, np.column_stack((cluster1_x, cluster1_y)), np.column_stack((cluster2_x, cluster2_y)), np.column_stack((cluster3_x, cluster3_y))), axis=0)
y = np.concatenate((y, np.zeros(300), np.ones(500), np.ones(50) * 2), axis=0)

# 绘制散点图
plt.scatter(X[:, 0], X[:, 1], c='b', marker='o', s=50)
plt.grid()
plt.show()

# 创建K-Means聚类器并进行聚类
km = KMeans(n_clusters=3, init='random', n_init=10, max_iter=300, tol=1e-04, random_state=0)
y_km = km.fit_predict(X)

# 绘制聚类结果散点图
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(X[y_km == 0, 0], X[y_km == 0, 1], s=50, c='lightgreen', marker='s', label='第1簇')
plt.scatter(X[y_km == 1, 0], X[y_km == 1, 1], s=50, c='orange', marker='o', label='第2簇')
plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1], s=50, c='lightblue', marker='v', label='第3簇')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=250, c='red', marker='*', label='数据中心点')
plt.legend()
plt.grid()
plt.show()
