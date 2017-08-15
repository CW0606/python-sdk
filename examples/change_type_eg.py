# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth
from qiniu import BucketManager

access_key = '...'
secret_key = '...'

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

bucket_name = 'Bucket_Name'

key = '...'

ret, info = bucket.change_type(bucket_name, key ,1)#1表示低频存储，0是标准存储

print(info)
# assert info.status_code == 200
