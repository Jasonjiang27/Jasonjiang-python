# -*- coding: utf-8 -*-

import csv
import sys
import hashlib
import jieba
import jieba.posseg as pseg
import pandas as pd
from snownlp import SnowNLP

reload(sys)
sys.setdefaultencoding('utf-8')
jieba.load_userdict("白名单-表格_1.csv")


def stopwordslist(filepath):
    #import pdb;pdb.set_trace()
    stopwords_list = set()
    stopword_file = pd.ExcelFile(filepath)
    print stopword_file.sheet_names
    df = stopword_file.parse(u"黑名单")
    data = df[u'词']
    print data
    for word in data:
        stopwords_list.add(str(word))
    #import ipdb; ipdb.set_trace()
    return stopwords_list


def main(filename):
    line_num = 0
    csvFile2 = open('2018年8月原数据.csv',
                    'w')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile2)
    writer.writerow(["k_id", "词性", "词", "词频", "情感"])
    xls_file = pd.ExcelFile(
        '2018年8月原数据.xlsx')
    lines = xls_file.parse('Sheet')
    black_words = stopwordslist(filepath)
    for i in range(0, len(lines)):
        row = lines.iloc[i]
        content = row['k_content']
        k_id = row['k_id']
        if type(content) == float:
            continue
        words = pseg.cut(content)
        print content
        all_res = {}
        for w in words:
            if str(w.word) not in black_words:
                if w.flag == "n" or w.flag == "v" or w.flag == "a":
                   
                    if all_res.has_key(w.word):
                        all_res[w.word]["num"] += 1
                    else:
                        c = str(w.word)
                        count = SnowNLP(c).sentiments
                        if count > 0.6:
                            sentiment = '褒'
                        elif count < 0.4:
                            sentiment = '贬'
                        else:
                            sentiment = '中'

                        all_res[w.word] = {
                            "k_id": k_id,
                            "cixing": w.flag,
                            "num": 1,
                            u"情感": sentiment
                        }

        for key, value in all_res.iteritems():
            writer.writerow(
                [value['k_id'], value["cixing"], key, value["num"], value[u"情感"]])
    csvFile2.close()


filepath = '黑白名单1019.xlsx'
main("2018年8月原数据.xlsx")

