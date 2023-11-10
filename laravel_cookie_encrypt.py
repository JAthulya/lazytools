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

def mcrypt_encrypt(value, iv):
    #global key
    AES.key_size = [len(key)]
    crypt_object = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
    return crypt_object.encrypt(value)

app_key = 'enter the laravel key'
key = base64.b64decode(app_key)

#string = input('enter to encrypt:')
#string = b'{"data":"hello"}'
string = b'dc32ebad0070055281d131828f97137883c929e6|sqtuRcmYkgYK96HmwOcWP6MAq9CuBmgjH5fRyX7N'

iv = os.urandom(16)
#string = dumps(string)
padding = 16 - len(string) % 16
string += bytes(chr(padding) * padding, 'utf-8')
value = base64.b64encode(mcrypt_encrypt(string, iv))
iv = base64.b64encode(iv)
mac = hmac.new(key, iv+value, hashlib.sha256).hexdigest()
dic = {'iv': iv.decode(), 'value': value.decode(), 'mac': mac}
enc= base64.b64encode(bytes(json.dumps(dic), 'utf-8'))
print(enc)