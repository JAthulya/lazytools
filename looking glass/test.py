import subprocess 
from subprocess import call
import os

r=['13641','13642','13643','13644','13645','13646','13647','13648','13649']
#os.environ['ran'] = ' '.join(r)
for i in r:
	os.environ['ran']=''.join(i)
	call("./test.sh")