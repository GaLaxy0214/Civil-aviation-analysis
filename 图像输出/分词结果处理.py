# -*- coding: utf-8 -*-

import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


class DbscanClustering():
    def __init__(self, stopwords_path=None):
        self.stopwords = self.load_stopwords(stopwords_path)
        self.vectorizer = CountVectorizer()
        self.transformer = TfidfTransformer()

# 加载停用词

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

    def pca(self, weights, n_components=2):
        """
        PCA对数据进行降维
        :param weights:
        :param n_components:
        :return:
        """
        pca = PCA(n_components=n_components)
        return pca.fit_transform(weights)

    def dbscan(self, corpus_path, eps=0.1, min_samples=3, fig=True):
        """
        DBSCAN：基于密度的文本聚类算法
        :param corpus_path: 语料路径，每行一个文本
        :param eps: DBSCA中半径参数
        :param min_samples: DBSCAN中半径eps内最小样本数目
        :param fig: 是否对降维后的样本进行画图显示
        :return:
        """
        corpus = self.preprocess_data(corpus_path)
        weights = self.get_text_tfidf_matrix(corpus)

        pca_weights = self.pca(weights)

        clf = DBSCAN(eps=eps, min_samples=min_samples)

        y = clf.fit_predict(pca_weights)

        if fig:
            plt.scatter(pca_weights[:, 0], pca_weights[:, 1], c=y)
            plt.show()

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

    def preprocess_data(self, corpus_path, output_path):
        """
        文本预处理，每行一个文本，并将分词结果写入文件
        :param corpus_path: 原始文本数据文件路径
        :param output_path: 分词结果输出文件路径
        :return: 无需返回值
        """
        with open(corpus_path, 'r', encoding='utf-8') as f:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                for line in f:
                    words = [word for word in jieba.lcut(line.strip()) if word not in self.stopwords]
                    output_file.write(' '.join(words) + '\n')

    def save_tfidf_matrix(self, weights, output_path):
        """
        将TF-IDF权重矩阵写入文件
        :param weights: TF-IDF权重矩阵
        :param output_path: 输出文件路径
        :return: 无需返回值
        """
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for row in weights:
                row_str = ' '.join([str(value) for value in row])
                output_file.write(row_str + '\n')
# if __name__ == '__main__':
#     dbscan = DbscanClustering(
#         stopwords_path='C:/Users/10146/Desktop/daima/第二部分/民航事故分析/文本处理/text_clustering/data/stop_words.txt')
#     result = dbscan.dbscan('C:/Users/10146/Desktop/事故挖掘/测试/实验数据.txt', eps=0.05,
#                            min_samples=3)
#     print(result)

if __name__ == '__main__':
    stopwords_path = 'C:/Users/10146/Desktop/daima/第二部分/民航事故分析/文本处理/text_clustering/data/stop_words.txt'
    input_path = 'C:/Users/10146/Desktop/事故挖掘/测试/分组/B737原因.txt'
    output_path = 'C:/Users/10146/Desktop/事故挖掘/测试/分组/B737原因分词结果.txt'

    dbscan = DbscanClustering(stopwords_path=stopwords_path)

    # 对原始文本数据进行分词，并将分词结果写入文件
    dbscan.preprocess_data(input_path, output_path)