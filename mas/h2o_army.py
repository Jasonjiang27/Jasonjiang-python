#!usr/bin/python
#-*-coding:utf-8-*-

import csv
import sys

from pymongo import MongoClient

reload(sys)
sys.setdefaultencoding("utf-8")

host = '47.96.184.66'
port = 3717
client = MongoClient(host, port)
db = client['crawler']
db.authenticate('ugc', 'a1b2c3d4')

results = db.public_praise.find({"k_type":"bbs","user_name":{"$exists":True}})

def get_userName():
    # users = set()
    user_post = {}
    user_forum = {}
    #user_post.setdefault(key, [])
    #import pdb;pdb.set_trace()
    for r in results:
        user = r['user_name']
        # print u'该用户为{}'.format(user)
        # if user not in users:
        #     users.add(user)

        try:
            content = r['k_content']
            forum = r['k_k_c_set']

            if not user_post.has_key(user):
                user_post[user] = []
            if not user_forum.has_key(user):
                user_forum[user] = []

            user_post[user].append(content)
            user_forum[user].append(forum)
        except Exception,e:
            print str(e)

	        # user_post.setdefault(user, []).append(content)
	        # user_forum.setdefault(user, []).append(forum)
        # except:
        #     pass
    return user_post, user_forum

def judge_online_supporter():
    
    user_post, user_forum = get_userName()
    # import ipdb; ipdb.set_trace()
    online_supporter = []
    print "开始计算水军"
    with open('online_supporter_user.txt', 'a') as f:
        for user,posts in user_post.iteritems():
            for post in posts:
                if posts.count(post) >=3:
                    online_supporter.append(user)
                    f.write(user+' ')
                    break
            print u"活捉水军一只，用户名为{},当前总水军数为".format(user)
        
        # for k,v in user_forum:
        #     if len(v) >= 25:
        #         online_supporter.append(k)
        #         print u"活捉水军一只，用户名为{},当前总水军数为{}".format(k, num)
        #         f.write(k+'  ')
              
    print u"任务完成，水总总数为{}".format(len(online_supporter))
    #return online_supporter

'''#把名单写进txt文件中
def write_to_txt():
    with open('online_supporter_user.txt', 'a') as f:
        for i in online_supporter:
            f.write(i)
'''    
if __name__=='__main__':
    judge_online_supporter()
    # write_to_txt()

