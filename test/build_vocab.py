import collections

input_dir = '/home/xyx/workspace/tensorflow_nmt/tmp/nmt_data/train.en'
output_dir = '/home/xyx/workspace/tensorflow_nmt/tmp/nmt_data/build_vocab.en'
inputs = open(input_dir, 'r')  

vocab = collections.OrderedDict()

for line in inputs.readlines():
    line = line.strip("\n")
    words = line.split(" ")
    for word in words:
        if word not in vocab:
            vocab[word] = 1
        else:
            vocab[word] +=1

print len(vocab)
outputs = open(output_dir, 'w')
for key in vocab.keys():
    if vocab[key] > 4 :
        outputs.write(key)
        outputs.write("\n")

outputs.close()