import subprocess 
from subprocess import call
import os

r = ['0','1','2','3','4','5','6','7','8','9']

#os.environ['ran'] = ' '.join(r)
for i in r:
	#num = i + '000'
	num = f"1318{i}"

	os.environ['ran']=''.join(num)
	call("./test.sh")