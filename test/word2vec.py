# # #coding:utf8
# # import gensim.models.word2vec as w2v
# # model_file_name = '/home/xyx/workspace/tensorflow_nmt/train_w2v.txt'
# # #模型训练，生成词向量
# # sentences = w2v.LineSentence('/home/xyx/workspace/tensorflow_nmt/tmp/nmt_data/train.en')
# # model = w2v.Word2Vec(sentences, size=20, window=5, min_count=5, workers=4) 
# # model.save(model_file_name)
# import gensim
# import jieba
# from gensim import corpora
# #构造字典 并 保存和加载
# # dictionary = corpora.Dictionary('/home/xyx/workspace/tensorflow_nmt/tmp/nmt_data/train.en')
# # dictionary.save('/home/xyx/workspace/tensorflow_nmt/mydict.dic')
# # print 'Tokens:Id'
# # print dictionary.token2id
# # new_dictionary = corpora.Dictionary.load('mydict.dic')
# # print(new_dictionary)

# documents = [
#     '拍照反光一直是摄影爱好者较为苦恼的问题',
#     '尤其是手机这种快速拍照设备的成像效果总是难以令人满意',
#     '特别是抓拍的珍贵照片',
#     '遇上反光照片基本作废',
#     '而索尼最近研发的集成偏振片传感器',
#     '似乎可以有效的解决拍照反光的问题'
# ]
# texts = [jieba.lcut(document) for document in documents]
# #构造字典 并 保存和加载
# dictionary = corpora.Dictionary(texts)
# dictionary.save('mydict.dic')
# print 'Tokens:Id'
# print dictionary.token2id
# new_dictionary = corpora.Dictionary.load('mydict.dic')
# print(new_dictionary)
#
from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

# print(sent_tokenize(EXAMPLE_TEXT))
print(word_tokenize('/home/xyx/workspace/tensorflow_nmt/tmp/nmt_data/train.en'))