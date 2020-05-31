from django.test import TestCase

# Create your tests here.
import requests
from qiniu import Auth
from swiper import config
qn = Auth(config.QN_ACCESS_KEY, config.QN_SECRET_KEY)
#有两种方式构造base_url的形式

#或者直接输入url的方式下载
base_url = 'http://qaezcmqwq.bkt.clouddn.com/Avatar-2.jpg'
#可以设置token过期时间
private_url = qn.private_download_url(base_url, expires=3600)
print(private_url)
r = requests.get(private_url)
print(r)
assert r.status_code == 200