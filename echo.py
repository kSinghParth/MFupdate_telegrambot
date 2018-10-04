
import pickle

file=open('../cred','rb')

creds=pickle.load(file)

token=creds[0]

URL="https://api.telegram.org/bot"+token+"/"

chatid=creds[1]

import json
import requests
import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_url(Url):
	response=requests.get(Url)
	content=json.loads(response.content.decode("utf8"))
	return content



def getupdates(offset=None):
	url=URL+"getUpdates?timeout=10"
	if offset:
		url=url+"&offset="+str(offset)
	response=get_url(url)
	return response
	
def echoall(updateall):
	for update in updateall['result']:
		send_message(urllib.parse.quote_plus(update['message']['text']),update['message']['chat']['id'])


def send_message(text,chatid):
	js=get_url(URL+"sendMessage?chat_id={}&text={}".format(chatid,text))


def find_values():
	rel_t200=webdriver.Chrome('../chromedriver')
	hdfc_sc=webdriver.Chrome('../chromedriver')
	rel_t200.get('http://m.moneycontrol.com/mutual-funds/nav/reliance-top-200-fund-retail-plan/MRC155')
	rel_val=rel_t200.find_element(by=By.XPATH, value='/html/body/div[4]/div/p[2]/span[1]/strong').text
	hdfc_sc.get('http://m.moneycontrol.com/mutual-funds/nav/hdfc-small-cap-fund/MMS002')
	hdfc_val=hdfc_sc.find_element(by=By.XPATH, value='/html/body/div[5]/div/p[2]/span[1]/strong').text
	rel_t200.quit()
	hdfc_sc.quit()
	return float(rel_val),float(hdfc_val)

def main():

	# Basic Bot
	# last_update_id=None
	# while True:
	# 	print ("sd")
	# 	update=getupdates(last_update_id)
	# 	if len(update['result'])>0:
	# 		echoall(update)
	# 		last_update_id=update['result'][len(update['result'])-1]['update_id']+1
	rel_val,hdfc_val=find_values()
	hdfc_units=1133.376
	hdfc_amount=round(hdfc_val*hdfc_units,4)
	hdfc_profit=round(hdfc_amount-50000,4)
	rel_units=1616.940
	rel_amount=round(rel_val*rel_units,4)
	rel_profit=round(rel_amount-50000,4)
	
	messagehdfc="HDFC Small Caps\nVALUE as on date 26/03/2018 : Rs 44.116\nUnits : 1133.376\nInitial Amount : Rs 50,000.00\nCurrent Rate : {}\nAmount : {}\nProfit : {}\n\n\n".format(hdfc_val,hdfc_amount,hdfc_profit)
	messagerel="Reliance Top 200\nVALUE as on date 26/03/2018 : Rs 30.9226\nUnits : 1133.376\nInitial Amount : Rs 50,000.00\nCurrent Rate : {}\nAmount : {}\nProfit : {}\n".format(rel_val,rel_amount,rel_profit)
	send_message(messagehdfc+messagerel,chatid)

if __name__ == '__main__':
	main()
