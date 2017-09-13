
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
inputs = open('../data/train/20170912/train.en', 'r')
outputs = open('../data/train/20170912/train_tokenized.en', 'w')
line_count = 0
lines=[line.decode('utf-8') for line in inputs.readlines()]
for line in lines:
	line_count += 1
	if line_count % 1000 == 0:
		print(line_count)
	# line.decode('utf-8')
	tokens = nltk.word_tokenize(line)
	string = " ".join(tokens)
		# .encode("utf-8")
	# for token in tokens:
	# 	outputs.write(token)
	outputs.write(string)
	outputs.write("\n")

outputs.close()
