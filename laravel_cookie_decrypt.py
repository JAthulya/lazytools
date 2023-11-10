import os
import json
import hashlib
import sys
import hmac
import base64
import string
import requests
from Crypto.Cipher import AES
from phpserialize import loads, dumps

#https://gist.github.com/bluetechy/5580fab27510906711a2775f3c4f5ce3

def mcrypt_decrypt(value, iv):
    global key
    AES.key_size = [len(key)]
    print(AES.key_size)
    crypt_object = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    return crypt_object.decrypt(value)
#cbc

#app_key ='C2ib6FP70OsLP0rRrUDh38r5RwoGCYCuix5GZP3fxhM='
app_key = 'enter the laravel key'
key = base64.b64decode(app_key)

bstring=input('enter the encrypt: ')
dic = json.loads(base64.b64decode(bstring).decode())
mac = dic['mac']
value = bytes(dic['value'], 'utf-8')
iv = bytes(dic['iv'], 'utf-8')
testmac = hmac.new(key, iv+value, hashlib.sha256).hexdigest()
print(f'value={value}')
print(f'iv={iv}')
print(f'testmac={testmac}')
print(f'key={key}')
if mac == hmac.new(key, iv+value, hashlib.sha256).hexdigest():
    dec = mcrypt_decrypt(base64.b64decode(value), base64.b64decode(iv))
        #return loads(mcrypt_decrypt(base64.b64decode(value), base64.b64decode(iv))).decode()
print(dec)




#decrypt('eyJpdiI6IktoZTZKdzdwUlRRVHlwT1V3TThLenc9PSIsInZhbHVlIjoiRWZ4d2VvdFd4U0FTdTdxbkhmblg3UXRGM0NrU0E1aTQ5My84YkcxSnlvTUZEeWUvRkNGY0x5dTBWQmViczlvNUF4WWFWU09sMEZzWVB2UkI2UTltRlRQaFljeHNwZCtPR0Q3MmFNVzc0M2hVSi95VE8wRmtQVmZxdUNLYTlZakQiLCJtYWMiOiJlMWJmMGE0YWRiNWQwMDkyYzJiZGQ5NDg0YzdhZWQyOTViMDU1MjA3NzI0ZmIyMTZhNjIyZjM3MWJkNzllYjZkIn0K')
#b'{"data":"a:6:{s:6:\\"_token\\";s:40:\\"vYzY0IdalD2ZC7v9yopWlnnYnCB2NkCXPbzfQ3MV\\";s:8:\\"username\\";s:8:\\"guestc32\\";s:5:\\"order\\";s:2:\\"id\\";s:9:\\"direction\\";s:4:\\"desc\\";s:6:\\"_flash\\";a:2:{s:3:\\"old\\";a:0:{}s:3:\\"new\\";a:0:{}}s:9:\\"_previous\\";a:1:{s:3:\\"url\\";s:38:\\"http:\\/\\/206.189.25.23:31031\\/api\\/configs\\";}}","expires":1605140631}\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
