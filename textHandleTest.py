#!/usr/bin/python
# -*- coding: utf-8 -*-

import jiebaUtils
import sys
import codecs
import re
import os
from itertools import izip
import jiebaUtils


reload(sys)
sys.setdefaultencoding('utf-8')


# text = open("../sample/News_info_train_example100_filter.txt", "r")
#
# # format id text
# for line in text.readlines():
#     # print line.strip()
#     vector = line.split("\t")
#     # print("{}\t{}".format(vector[0],vector[1]))
#     seg_list = jiebaUtils.sentence2Vec(vector[1])
#     print("{}\t{}".format(vector[0], vector[1]))
#     print("{}\t{}\n".format(vector[0], " ".join(seg_list)))

# 生成测试数据
def per_test_data():
    text = open("../sample/News_info_validate_filter.txt", "r")

    result = []
    id = []
    # format id text
    for line in text.readlines():
        # print line.strip()
        vector = line.split("\t")
        # print("{}\t{}".format(vector[0],vector[1]))
        result.append(vector[1])
        id.append(vector[0])
    with codecs.open("../sample/" + "test.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(result))
    return id

# 取得测试结果，合并生成提交文件
def generate_result():
    rk = "{}\t{}\tNULL\tNULL"
    id = per_test_data()

    lables = []
    text = open("../sample/predict.txt", "r")
    for line in text.readlines():
        if "1" in line:
            lables.append("1")
        elif "2" in line:
            lables.append("2")
        else:
            lables.append("0")

    print " ".join(lables)
    print " ".join(id)
    print len(id)
    last = []
    map_list = [(k, v) for k, v in izip(id, lables)]
    print len(map_list)
    for item in map_list:
        last.append("{}\t{}\tNULL\tNULL\n".format(item[0],item[1]))
    print len(last)
    #with codecs.open("../sample/" + "result.txt", "w", encoding="utf-8") as f:
    #    f.write("\n".join(last))
    f = open("../sample/result.txt", "w")
    for i in last:
        f.write(i)
    f.close()



# target: id label keywords
# info_train: id info pic_list
# label_train: id label pic_list info

# info_train: id info pic_list
def get_info_train(path):
    with open(path, "r") as f:
        result = {}
        for line in f:
            vector = line.split("\t")
            result[vector[0]] = vector[1]
        return result


# label_train: id label pic_list info
def get_label_train(path):
    with open(path, "r") as f:
        label = {}
        target = {}
        for line in f:
            vector = line.split("\t")
            label[vector[0]] = vector[1]
            target[vector[0]] = vector[3]
        return label, target


# return: id: [label, textStr]
def get_train_data(path_info_train, path_label_train):
    result = {}
    id_list = []
    raw_info = get_info_train(path_info_train)
    label_info, target_info = get_label_train(path_label_train)
    for item in label_info.items():
        id = item[0]
        id_list.append(id)
        label = item[1]
        raw_data = raw_info[id]
        if not 'NULL' in target_info[id]:
            target_data = target_info[id]
        else:
            target_data = ""
        combine = str(raw_data + target_data)
        result[id] = [id, label, combine.strip("\n\t")]
    return result, sorted(id_list)


def generate_train_data():
    path_info_train = "../sample/News_info_train_filter.txt"
    path_label_train = "../sample/News_pic_label_train.txt"
    result, id_list = get_train_data(path_info_train, path_label_train)
    train_data = []
    def not_empty(s):
        return s and s.strip()

    def is_useful(word):
        stop_words = open("../sample/stop_words.txt")
        return word not in stop_words and not re.search('([A-Za-z]+|\d+\.*\d*)', word)

    for item in id_list:
        sentence = result[item][2]
        seg_list = jiebaUtils.sentence2Vec(sentence.replace("\t"," ").replace("\n"," "))
        res = filter(not_empty, seg_list)
        res = filter(is_useful, res)
        lable = "__label__{} {}".format(result[item][1], " ".join(res))
        train_data.append(lable)
    with codecs.open("../sample/" + "train.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(train_data))


if __name__ == '__main__':
    # des_path = "../sample/categroy_{}/"
    # path_info_train = "../sample/News_info_train_example100_filter.txt"
    # path_label_train = "../sample/News_pic_label_train_example100.txt"
    # result, id_list = get_train_data(path_info_train, path_label_train)
    # data1 = []
    # data2 = []
    # data0 = []
    # split_category()

    generate_train_data()
    # for item in id_list:
    #     # print item[0]," ".join(item[1])
    #     lable = result[item][1]
    #     if lable == "1": data1.append("\t".join(result[item]))
    #     if lable == "2": data2.append("\t".join(result[item]))
    #     if lable == "0": data0.append("\t".join(result[item]))
    # list_data = [data0, data1, data2]
    # for i in (0, 1, 2):
    #     des_categroy_path = des_path.format(i)
    #     if not os.path.exists(des_categroy_path): os.mkdir(des_categroy_path)
    #     print "\n".join(list_data[i])
    #     with codecs.open(des_categroy_path + "data.txt", "w", encoding="utf-8") as f:
    #         f.write("\n".join(list_data[i]))
    # # for i in id_list:
    # #     print i
   # id = per_test_data()

   # generate_result()
