dict_text ={}
dict_sum = {}

with open('/home/vladimir/учеба/dz file/dz-file-/1.txt', encoding='utf-8') as f:
    name  = '1.txt'
    sum_str = len(f.readlines())
    str_ = []
    for line in f:
        sum_str += 1
        str_.append(line)
        dict_text[name] =str_
    dict_sum.setdefault(name, sum_str)
    
with open('/home/vladimir/учеба/dz file/dz-file-/2.txt', encoding='utf-8') as f:
    name  = '2.txt'
    sum_str = len(f.readlines())
    str_ = []
    for line in f:
        sum_str += 1
        str_.append(line)
        dict_text[name] =str_
    dict_sum.setdefault(name, sum_str)    

with open('/home/vladimir/учеба/dz file/dz-file-/3.txt', encoding='utf-8') as f:
    name  = '3.txt'
    sum_str = 0
    str_ = []
    for line in f:
        sum_str += 1
        str_.append(line)
        dict_text[name] =str_
    dict_sum.setdefault(name, sum_str)

import operator
sorted_dict = dict(sorted(dict_sum.items(), key=operator.itemgetter(1)))

import pickle
with open('Text.txt', 'wb') as f:
    for key in sorted_dict.keys():
        for i in dict_text[key]:
            text = i.strip()
            pickle.dump(text, f)
            print(text)








