# -*- coding: utf-8 -*-

import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class KmeansClustering():
    def __init__(self, stopwords_path=None):
        self.stopwords = self.load_stopwords(stopwords_path)
        self.vectorizer = CountVectorizer()
        self.transformer = TfidfTransformer()

    def load_stopwords(self, stopwords=None):
        """
        加载停用词
        :param stopwords:
        :return:
        """
        if stopwords:
            with open(stopwords, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f]
        else:
            return []

    def preprocess_data(self, corpus_path):
        """
        文本预处理，每行一个文本
        :param corpus_path:
        :return:
        """
        corpus = []
        with open(corpus_path, 'r', encoding='utf-8') as f:
            for line in f:
                corpus.append(' '.join([word for word in jieba.lcut(line.strip()) if word not in self.stopwords]))
        return corpus

    def get_text_tfidf_matrix(self, corpus):
        """
        获取tfidf矩阵
        :param corpus:
        :return:
        """
        tfidf = self.transformer.fit_transform(self.vectorizer.fit_transform(corpus))

        # 获取词袋中所有词语
        # words = self.vectorizer.get_feature_names()

        # 获取tfidf矩阵中权重
        weights = tfidf.toarray()
        return weights

    def kmeans(self, corpus_path, n_clusters=5):
        """
        KMeans文本聚类
        :param corpus_path: 语料路径（每行一篇）,文章id从0开始
        :param n_clusters: ：聚类类别数目
        :return: {cluster_id1:[text_id1, text_id2]}
        """
        corpus = self.preprocess_data(corpus_path)
        weights = self.get_text_tfidf_matrix(corpus)

        clf = KMeans(n_clusters=n_clusters)

        # clf.fit(weights)

        y = clf.fit_predict(weights)

        # 中心点
        # centers = clf.cluster_centers_

        # 用来评估簇的个数是否合适,距离约小说明簇分得越好,选取临界点的簇的个数
        # score = clf.inertia_

        # 每个样本所属的簇
        result = {}
        for text_idx, label_idx in enumerate(y):
            if label_idx not in result:
                result[label_idx] = [text_idx]
            else:
                result[label_idx].append(text_idx)
        return result


# if __name__ == '__main__':
#     Kmeans = KmeansClustering(stopwords_path='C:/Users/10146/Desktop/daima/第二部分/民航事故分析/文本处理/text_clustering/data/stop_words.txt')
#     result = Kmeans.kmeans('C:/Users/10146/Desktop/事故挖掘/测试/实验数据.txt', n_clusters=8)
#     print(result)
if __name__ == '__main__':
    Kmeans = KmeansClustering(
        stopwords_path='C:/Users/10146/Desktop/daima/第二部分/民航事故分析/文本处理/text_clustering/data/stop_words.txt')
    result = Kmeans.kmeans('C:/Users/10146/Desktop/事故挖掘/测试/事件原因1.txt', n_clusters=8)
    print(result)

    # 统计每个簇的文本数量
    cluster_sizes = [len(text_ids) for text_ids in result.values()]
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 绘制柱状图
    plt.bar(range(len(cluster_sizes)), cluster_sizes)
    plt.xlabel('聚类簇编号')
    plt.ylabel('文本数量')
    plt.title('每个聚类簇中的文本数量')
    plt.xticks(range(len(cluster_sizes)), result.keys())
    plt.show()