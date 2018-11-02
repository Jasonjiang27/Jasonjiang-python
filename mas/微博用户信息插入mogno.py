#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import json
from pymongo import MongoClient
import requests
import time

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

host = '47.96.184.66'
port = 3717
client = MongoClient(host, port)
db = client['crawler']
db.authenticate('ugc', 'a1b2c3d4')
#u_url = "https://api.weibo.com/2/users/show.json?access_token=2.0062jLqFW4Mc1Bddd8a5ffdfN_flFD&uid="
u_url = "https://api.weibo.com/2/users/show.json?access_token=2.00Kmlw2DMf7ETBa6c71d8386txpVPB&uid="


csv_file = open('微博数据奥迪Q2L处理后.csv', 'r')
reader = csv.reader(csv_file)
result = []
for item in reader:
    if reader.line_num == 1:
        continue
    result.append(item[1])
print len(result)
num = 0
#import pdb;pdb.set_trace()
for u_id in result:
    print u_id
    if db.weibo_user_profile_ugc.find_one({"_id":u_id}) == None:
        #import pdb;pdb.set_trace()
        try:
            r = requests.get(u_url + u_id)
            _file = r.text
            dict_file1 = json.loads(_file)
            dict_file1["_id"] = str(dict_file1["id"])
            dict_file1["city"] = eval(dict_file1["city"])
            dict_file1["province"] = eval(dict_file1["province"])
            del dict_file1["id"]
            key_list = ["_id","province","city","favourites_count","description","friends_count","url","gender","created_at","verified","allow_all_act_msg","followers_count","screen_name","location","statuses_count","verified_type","name"]
            for k,v in dict_file1.items():
                if k not in key_list:
                    del dict_file1[k]

            #map(dict_file1.pop, ["bi_followers_count","verified_trade","idstr","class","profile_image_url","cover_image_phone","profile_url","domain","weihao","pagefriends_count","video_status_count","following","geo_enabled","remark","insecurity","status","ptype","allow_all_comment","avatar_large","avatar_hd","verified_reason","verified_reason_url","verified_source","verified_source_url","follow_me","like","like_me","online_status","lang","star","mbtype","mbrank","block_word","block_app","credit_score","user_ability","urank","story_read_state","vclub_member","avatargj_id"])
        except KeyError as e:
            print e
        print dict_file1
        db.weibo_user_profile_ugc.save(dict_file1)
        num += 1
        print u"保存一条数据成功，共保存%d条数据" % num
    time.sleep(0.6)
print u"保存所有数据成功"
csv_file.close()

'''
#一条数据测试
import pdb;pdb.set_trace()
r = requests.get(u_url+"6508736190")
_file = r.text
print type(_file)
dict_file1 = json.loads(_file)
print type(dict_file1)
#dict_file2 = dict()
#for k ,v in dict_file1.items():
    #if k == "id":
dict_file1["_id"] = str(dict_file1["id"])
dict_file1["city"] = eval(dict_file1["city"])
dict_file1["province"] = eval(dict_file1["province"])
del dict_file1["id"]
    #break
    #if db.weibo_user_profile_ugc.find_one({k:{"$exists":True}}) != None:
        #dict_file2[k] = v 
map(dict_file1.pop, ["bi_followers_count","verified_trade","idstr","class","profile_image_url","cover_image_phone","profile_url","domain","weihao","pagefriends_count","video_status_count","following","geo_enabled","remark","insecurity","status","ptype","allow_all_comment","avatar_large","avatar_hd","verified_reason","verified_reason_url","verified_source","verified_source_url","follow_me","like","like_me","online_status","lang","star","mbtype","mbrank","block_word","block_app","credit_score","user_ability","avatargj_id","urank","story_read_state","vclub_member"])
print dict_file1
db.weibo_user_profile_ugc.save(dict_file1)
csv_file.close()
'''
