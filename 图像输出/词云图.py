from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

path = 'C:/Users/10146/Desktop/事故挖掘/测试/分组/B737原因分词结果.txt'
with open(path, encoding='utf-8') as f:
    mytext = f.read()

    # 中文分词
    text = ' '.join(jieba.cut(mytext))

    # 显示词云
    wc = WordCloud(font_path='msyh.ttc').generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()