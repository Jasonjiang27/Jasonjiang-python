#coding=utf-8
import datetime
import pandas as pd
import csv
import sys


from pymongo import MongoClient

reload(sys)
sys.setdefaultencoding('utf8')

out = open('jinritoutiao_article_all.csv', 'a')
csv_writer = csv.writer(out, dialect='excel')


client = MongoClient('192.168.1.16',3717)

db = client["crawler"]
db.authenticate("ugc","a1b2c3d4")
jinritoutiao_article = db["jinritoutiao_article"]
#import pdb;pdb.set_trace()
result  = jinritoutiao_article.find()
result = list(result)
keys = result[0].keys()
for item in result:
    crawl_date = item['crawl_date']
    values = []
    item['crawl_date'] = item['crawl_date'].strftime("%Y-%m-%d %H:%M:%S")
    for key in keys:
        if item.has_key(key):
            #if key == "k_content" or key == "k_title":
            if type(item[key]) == str:
                item[key] = item[key].replace("\n",'，')
                item[key] = item[key].replace(',','，')
                values.append(item[key])
            else:
                values.append(item[key])
        else:
            values.append("")
    
    csv_writer.writerow(values)

