#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
import os
import conf
import logging


def sentence2Vec(sentence):
    # load_dicts()
    seg_list = jieba.cut(sentence, cut_all=True)
    result = []
    for item in seg_list:
        result.append(item)
    return result


def load_dicts():
    path = "/home/firgavin/PycharmProjects/untitled/dictionary/"
    # print path
    try:
        files = os.listdir(path)
        s = []
        for file in files:
            if not os.path.isdir(file):
                dictpath = os.path.join(path, file)
                # print dictpath
                s.append(dictpath)
        for item in s:
            jieba.load_userdict(item)

    except Exception as e:
        pass


def get_keywords(sentence, topK=20, withWeight=False):
    tags = jieba.analyse.extract_tags(sentence, topK=topK, withWeight=withWeight)
    return tags


def load_self_dict():
    pass


if __name__ == '__main__':
    text = "82周年庆 | 收到八方来贺之第一波(女士专场福利) 还有2天 就是我们中央商场的场庆啦! 八方祝贺 纷至沓来 今天先剧透一波 女士专场福利 1F 悦诗风吟 满500减80 芬芳记忆套装一口价230元 单笔满300元赠三件套礼盒 1F 佰草集 满300抵50 润泽套盒原价1380元现价850元 花车低至6折 1F 薇姿 满300抵40 焕白保湿套盒原价1007元 现价596元 花车低至6折 1F 理肤泉 满300抵40 花车低至6折 1F 雅漾 满300抵40 密集舒缓套盒原价376元 现价298元 花车低至5折 1F 红地球 满300抵40 SPA礼盒原价1350元 现价856元 花车彩妆礼盒低至5折 1F 千百度集团 低至99元 200元以上再享8折 1F 星期六集团 低至129元 200元以上再享8折 1F 哈森 低至99元 部分冬款、男鞋199元 300元以上一双9折、两双8.5折 1F 瑞贝卡 低至99元 200元以上一双9折、两双8.5折 2F 菲姿 低至2.5折 任意购物加150元 即可换购指定服饰1件 2F 凯莉米洛 冬款2-6折 3折以上商品再享9折 2F 艾米瑞 充值2000得2300,充值3000得3800 充值5000得6500,充值10000得14000 满额988元即可参加抽奖 一等奖:旅行箱 二等奖:首饰盒 三等奖:围巾 四等奖:大衣刷 2F 德菲蒂奥 低至1折 5折以上商品再享9折 2F 怡惟 羽绒服低至3折 特惠品低至100元/件 2F 无色无味 冬款5折 特惠品199元/件 2F 影响时尚 冬款大衣、羽绒服低至1折 2F FION 4折以上一件折上9折二件折上8折 2F FION 4折以上一件折上9折二件折上8折 2F WHY 4折以上一件折上9.5折二件折上9折 2F adidas kids 冬款5-8折 5折以上商品两件折上8.8折 2F 七波辉 低至48元"
    fenci = sentence2Vec(text)
    print(
        " ".join(fenci)
    )
    # for item in sentence2Vec(text):
    #     print item
    # load_dicts()
    kw = get_keywords(text, 20)
    print ", ".join(kw)
