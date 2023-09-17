import pandas as pd
import gensim
from gensim import corpora
from gensim.models.ldamodel import LdaModel

# 读取Excel数据
data = pd.read_excel("C:\/Users/10146/Desktop/事故挖掘/测试/分组/B737机型数据.xlsx")
# 使用众数填充分类列的空白值
data['事件类型（主要）'].fillna(data['事件类型（主要）'].mode()[0], inplace=True)
# 将每列数据合并为一个列表
documents = []
for i, row in data.iterrows():
    # document = f"{row['事件类型（主要）']} {row['运行阶段']} {row['机型']}"
    document = f"{row['事件类型（主要）']} {row['运行阶段']}"
    documents.append(document)

# 分词处理
tokenized_documents = [doc.split() for doc in documents]

# 构建词汇表
dictionary = corpora.Dictionary(tokenized_documents)

# 将文本转换为词袋表示
corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

# 训练LDA模型
num_topics = 10  # 设置主题数
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)

# 输出主题词汇分布和主题文档分布
for topic_id in range(num_topics):
    print(f"Topic {topic_id}: {lda_model.print_topic(topic_id)}")

# 对新文档进行主题推断
new_document = "新的文本数据..."
new_doc_bow = dictionary.doc2bow(new_document.split())
new_doc_topics = lda_model.get_document_topics(new_doc_bow)
print("New Document Topics:", new_doc_topics)
