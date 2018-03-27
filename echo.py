
token="587488845:AAHvtE5rahjneYvL7LQ1JYQXVo_VVC7phsc"

URL="https://api.telegram.org/bot"+token+"/"

import json
import requests
import time
import urllib

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

def main():
	last_update_id=None
	while True:
		print ("sd")
		update=getupdates(last_update_id)
		if len(update['result'])>0:
			echoall(update)
			last_update_id=update['result'][len(update['result'])-1]['update_id']+1
		time.sleep(2)

if __name__ == '__main__':
	main()
