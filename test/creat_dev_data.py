# import collections
#
# def getfilelines(filename, eol='\n', buffsize=4096):
#     with open(filename, 'rb') as handle:
#         linenum = 0
#         buffer = handle.read(buffsize)
#         while buffer:
#             linenum += buffer.count(eol)
#             buffer = handle.read(buffsize)
#         return linenum
#
#
# def readtline(filename, lineno, eol="\n", buffsize=4096):
#     with open(filename, 'rb') as handle:
#         readedlines = 0
#         buffer = handle.read(buffsize)
#         while buffer:
#             thisblock = buffer.count(eol)
#             if readedlines < lineno < readedlines + thisblock:
#                 # inthisblock: findthe line content, and return it
#                 return buffer.split(eol)[lineno - readedlines - 1]
#             elif lineno == readedlines + thisblock:
#                 # need continue read line rest part
#                 part0 = buffer.split(eol)[-1]
#                 buffer = handle.read(buffsize)
#                 part1 = buffer.split(eol)[0]
#                 return part0 + part1
#             readedlines += thisblock
#             buffer = handle.read(buffsize)
#         else:
#             raise IndexError
#
# def getrandomline(filename):
#     import random
#     return readtline(
#         filename,
#         random.randint(0, getfilelines(filename)),
#     )
#
# input_dir = '../data/train/20170912/train.en'
# output_dir = '../data/train/20170912/dev.en'
# # inputs = open(input_dir, 'r')
# outputs = open(output_dir, 'w')
# for i in range(1, 8000):
#     print(i)
#     line = getrandomline(input_dir)
#     print(line)
#     outputs.write(line)
#     outputs.write("\n")



    # vocab = collections.OrderedDict()
# line_count = 0
# for line in inputs.readlines():
#     line_count += 1
#     if line_count % 100000 == 0:
#         print(line_count)
#     line = line.strip("\n")
#     words = line.split(" ")
#     for word in words:
#         if word not in vocab:
#             vocab[word] = 1
#         else:
#             vocab[word] +=1
#
# print len(vocab)
# outputs = open(output_dir, 'w')
# for key in vocab.keys():
#     if vocab[key] > 4 :
#         outputs.write(key)
#         outputs.write("\n")
#
# outputs.close()

#coding=utf-8
# import xml.dom.minidom
#
#
# dom = xml.dom.minidom.parse('/home/xyx/workspace/nmt_challengerai/data/validation/20170912/valid.en-zh.en.sgm')
#
#
# root = dom.documentElement
#
# cc=dom.getElementsByTagName('seg')
# c1=cc[0]
# print c1.firstChild.data
import linecache

# count = linecache.getline(filename,linenum)
input_dir_0 = '../data/train/20170912/train.en'
input_dir_1 = '../data/train/20170912/train.zh'
# output_dir_0 = '../data/train/20170912/dev.en'
# output_dir_1 = '../data/train/20170912/dev.zh'
output_dir_0 = '../data/train/20170912/test.en'
output_dir_1 = '../data/train/20170912/test.zh'

inputs_0 = open(input_dir_0, 'r')
# lines0 = inputs_0.readlines()
inputs_1 = open(input_dir_1, 'r')
# lines1 = inputs_1.readlines()
outputs0 = open(output_dir_0, 'w')
outputs1 = open(output_dir_1, 'w')
# print len(lines0), len(lines1)
# step = len(lines0) / 8000

# count_0 = 0
count_0 = 10
numb_0 = 0
for line in inputs_0.readlines():
    count_0 += 1
    if count_0 % 1237 == 0:
        numb_0 += 1
        outputs0.write(line)
    if numb_0 ==8000:
        break

print numb_0
outputs0.close()

# count_1 = 0
count_1 = 10
numb_1 = 0
for line in inputs_1.readlines():
    count_1 += 1
    if count_1 % 1237 == 0:
        numb_1 += 1
        outputs1.write(line)
    if numb_1 ==8000:
        break

print numb_1
outputs1.close()



# for i in inputs.read
#     print(i)
#     line = getrandomline(input_dir)
#     print(line)
#     outputs.write(line)
#     outputs.write("\n")
