#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weibo import APIClient

APP_KEY = '1220763602'  # app key
APP_SECRET = '70a950b88405e65430aafc716d165ad7'  # app secret
CALLBACK_URL = 'https://tygzx.github.io/'  # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url
import ipdb; ipdb.set_trace()

client.request_access_token('a4dceaba247b82d5402bc0e7d26d1ff5')
url = "https://api.weibo.com/2/users/show.json?access_token=2.0062jLqFW4Mc1Bddd8a5ffdfN_flFD&uid=2483201862"

