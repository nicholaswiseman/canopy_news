import bs4 as bs
import urllib.request
from my_email_script import send_email
import time

def is_news(url):
	try:
		return 'www.canopygrowth.com/wp-content/uploads' in url.get('href')
	except:
		return False

def is_recent(url):
	try:
		file = open('urls.txt','r')
		old_urls = file.read()
		file.close()
	except:
		print("Failed the open urls.txt! Please make sure urls.txt is present")
	
	if (url.get('href') in old_urls):
		return False
	elif not (url.get('href') in old_urls):
		file = open('urls.txt','a')
		file.write(f"\n{url.get('href')}")
		file.close()
		return True

if __name__ == '__main__':
	while 1:
		source = urllib.request.urlopen('https://www.canopygrowth.com/investors/news-releases/').read()
		soup = bs.BeautifulSoup(source,'lxml')

		for url in soup.find_all('a'):
			if is_news(url) and is_recent(url):
				msg = f"Hey Josh,\n\nA news release from Canopy Growth has been posted:\n\n{url.get('href')}\n\nYour friend,\nCanopy Updates"
				send_email('canopy.updates@gmail.com','nickandjosh','nicholas.jw.wiseman@gmail.com','Canopy Growth News Release',msg)
		time.sleep(30)		