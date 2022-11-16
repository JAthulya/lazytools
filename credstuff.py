findword= 'cultiris' ####edit this

#read from usernames
#######################################################

with open('usernames.txt') as f:
	usernames = [line.rstrip() for line in f]

with open('passwords.txt') as f:
	passwords = [line.rstrip() for line in f]

#count from usernames
#########################################################

count =-1
for i in usernames:
	count = count + 1
#print(count)

##########################################################
wordposition=0
for i in range(count):
	if usernames[i] == findword:
		wordposition = i

print(wordposition)
print(passwords[wordposition])

#########################################################

rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

flag = (passwords[wordposition]).translate(rot13)
print(f"flag is {flag}")

