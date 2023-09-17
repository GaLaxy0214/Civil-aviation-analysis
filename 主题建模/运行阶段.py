import pandas as pd
import gensim
from gensim import corpora
from gensim.models.ldamodel import LdaModel

# 读取Excel数据
data = pd.read_excel("C:\/Users/10146/Desktop/事故挖掘/测试/output.xlsx")

# 获取所有不同的运行阶段
run_phases = data["运行阶段"].unique()

# 循环处理每个运行阶段
for run_phase in run_phases:
    # 筛选特定运行阶段的数据
    subset_data = data[data["运行阶段"] == run_phase]

    # 合并机型和事故类型为一个文本内容
    documents = []
    for i, row in subset_data.iterrows():
        document = f"{row['机型']} {row['事件类型（主要）']}"
        documents.append(document)

    # 分词处理
    tokenized_documents = [doc.split() for doc in documents]

    # 构建词汇表
    dictionary = corpora.Dictionary(tokenized_documents)

    # 将文本转换为词袋表示
    corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    # 训练LDA模型
    num_topics = 3  # 设置主题数
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)

    print(f"Run Phase: {run_phase}")

    # 输出主题词汇分布
    for topic_id in range(num_topics):
        print(f"Topic {topic_id}: {lda_model.print_topic(topic_id)}")

    print("=" * 30)
