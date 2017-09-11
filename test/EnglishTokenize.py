
import nltk
inputs = open('/home/xyx/workspace/ai_challenger_translation/train.en', 'r')  
outputs = open('/home/xyx/workspace/ai_challenger_translation/Tokens.en', 'w')  
for line in inputs.readlines():
	tokens = nltk.word_tokenize("A new cartoon. “l wish l was taller.”")
	string = " ".join(tokens)
		# .encode("utf-8")
	# for token in tokens:
	# 	outputs.write(token)
	outputs.write(string)
	outputs.write("\n")

outputs.close()
