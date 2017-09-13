import jieba

inputs = open('../data/train/20170912/train.zh', 'r')
outputs = open('../data/train/20170912/train_tokenized.zh', 'w')
line_count = 0
for line in inputs.readlines():
    line_count+=1
    if line_count%1000==0:
        print(line_count)
    words=jieba.cut(line, cut_all=False)
    string = " ".join(words).encode("utf-8")
    outputs.write(string)
    outputs.write("\n")

outputs.close()
# # import jieba
# import sys
# print sys.getdefaultencoding()
# # words=jieba.cut("sss ss", cut_all=False)
# print "hello1"
# print "hello"