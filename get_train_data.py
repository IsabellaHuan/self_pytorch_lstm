#coding=utf-8
import uniout

# author: Huan Shuwen
# time : 2019/4/3 下午8:38
# file : get_train_data
"""
NOTICE:

"""
training_data=[]
word_list=[]
for line in open('./train_data.txt','r'):
    if line == '\n':
        title_word_list = map(lambda x:x[0],word_list)
        title_tag_list = map(lambda x:x[1],word_list)
        training_data.append((title_word_list,title_tag_list))
        word_list=[]
    else:
        content = line.replace('\n','').split('\t')
        word_list.append(content)
