from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# 生成模拟数据
X, y = make_blobs(n_samples=600, n_features=2, centers=1, cluster_std=0.4, shuffle=True, random_state=0)

# 添加第二个簇（150个数据点）
cluster2_x = np.random.normal(1, 0.4, 150)
cluster2_y = np.random.normal(2, 0.3, 150)
X = np.concatenate((X, np.column_stack((cluster2_x, cluster2_y))), axis=0)
y = np.concatenate((y, np.ones(150)))

# 添加第三个簇（100个数据点）
cluster3_x = np.random.normal(-0.5, 0.4, 100)
cluster3_y = np.random.normal(-1, 0.4, 100)
X = np.concatenate((X, np.column_stack((cluster3_x, cluster3_y))), axis=0)
y = np.concatenate((y, np.ones(100) * 2))

# 添加第四个簇（100个数据点）
cluster4_x = np.random.normal(2, 0.4, 100)
cluster4_y = np.random.normal(-1, 0.3, 100)
X = np.concatenate((X, np.column_stack((cluster4_x, cluster4_y))), axis=0)
y = np.concatenate((y, np.ones(100) * 3))

# 添加第五个簇（80个数据点）
cluster5_x = np.random.normal(-1.5, 0.4, 80)
cluster5_y = np.random.normal(1.8, 0.5, 80)
X = np.concatenate((X, np.column_stack((cluster5_x, cluster5_y))), axis=0)
y = np.concatenate((y, np.ones(80) * 4))

# 绘制散点图
plt.scatter(X[:, 0], X[:, 1], c='b', marker='o', s=50)
plt.grid()
plt.show()

# 创建K-Means聚类器并进行聚类
km = KMeans(n_clusters=5, init='random', n_init=10, max_iter=300, tol=1e-04, random_state=0)
y_km = km.fit_predict(X)

# 绘制聚类结果散点图
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(X[y_km == 0, 0], X[y_km == 0, 1], s=50, c='lightgreen', marker='s', label='第1簇')
plt.scatter(X[y_km == 1, 0], X[y_km == 1, 1], s=50, c='orange', marker='o', label='第2簇')
plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1], s=50, c='lightblue', marker='v', label='第3簇')
plt.scatter(X[y_km == 3, 0], X[y_km == 3, 1], s=50, c='pink', marker='P', label='第4簇')
plt.scatter(X[y_km == 4, 0], X[y_km == 4, 1], s=50, c='purple', marker='D', label='第5簇')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=250, c='red', marker='*', label='数据中心点')
plt.legend()
plt.grid()
plt.show()
print('Distortion: %.2f' % km.inertia_)# 在完成KMeans模型的拟合后，簇内误差平方和可以通过inertia属性访问
distortions = []
for i in range(1,11) :
    km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300, random_state=0)
    km.fit(X)
    distortions.append(km.inertia_)
plt.plot(range(1,11), distortions, marker='o',)
plt.xlabel('簇的数量')
plt.ylabel('不同簇数量时的畸变值')
plt.show()

