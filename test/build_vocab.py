import collections
input_dir = '../data/train/20170912/train.en'
output_dir = '../data/train/20170912/dev.en'
inputs = open(input_dir, 'r')
outputs = open(output_dir, 'w')
vocab = collections.OrderedDict()
line_count = 0
for line in inputs.readlines():
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count)
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