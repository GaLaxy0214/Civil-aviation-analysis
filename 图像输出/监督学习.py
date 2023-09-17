import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer

# 读取Excel文件并选择需要挖掘关联规则的列（事件原因和运行阶段）
data = pd.read_excel('C:/Users/10146/Desktop/事故挖掘/测试/output.xlsx', usecols=['事件类型（主要）', '运行阶段'])

# 去除空白行
data.dropna(inplace=True)

# 将文本数据转换为词频向量
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['事件类型（主要）'])
text_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# 使用Apriori算法挖掘频繁项集
frequent_itemsets = apriori(text_df, min_support=0.1, use_colnames=True)

# 使用association_rules提取关联规则
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# 打印关联规则的基本信息
print("关联规则：")
print(rules)

# 添加支持度和置信度的分布图
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(rules['support'], bins=20, kde=True)
plt.title("支持度分布")

plt.subplot(1, 2, 2)
sns.histplot(rules['confidence'], bins=20, kde=True)
plt.title("置信度分布")
plt.show()

# 创建关联规则矩阵的热图
plt.figure(figsize=(10, 6))
sns.heatmap(pd.crosstab(index=rules['antecedents'], columns=rules['consequents']),
            annot=True, fmt='d', cmap="YlGnBu")
plt.title("关联规则矩阵")
plt.xlabel("后项 (Consequents)")
plt.ylabel("前项 (Antecedents)")
plt.show()

# 可视化关联规则的重要性和性能
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.barplot(x=rules['antecedents'], y=rules['confidence'], palette="YlGnBu")
plt.title("关联规则置信度")

plt.subplot(1, 2, 2)
sns.scatterplot(x=rules['support'], y=rules['confidence'], hue=rules['lift'], palette="YlGnBu")
plt.title("关联规则性能")
plt.xlabel("支持度")
plt.ylabel("置信度")
plt.show()
