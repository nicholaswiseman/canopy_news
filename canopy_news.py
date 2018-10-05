import bs4 as bs
import urllib.request
from my_email_script import send_email
import time

#All the news release urls start with the same string.
#Look for that string in the url to see if its news.
def is_news(url):
	try:
		return 'www.canopygrowth.com/wp-content/uploads' in url.get('href')
	except:
		return False

#Save all the old urls in urls.txt into a string 
#Then we check if the url we are interested is in the string... if so we've seen it before.
#If not it's new and we must append it to urls.txt
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
		#grab the html and parse it
		source = urllib.request.urlopen('https://www.canopygrowth.com/investors/news-releases/').read()
		soup = bs.BeautifulSoup(source,'lxml')
		
		#for each hyperlink we check if its news and if we've seen it before
		for url in soup.find_all('a'):
			if is_news(url) and is_recent(url):
				#here we send an email if its new. For this to work you will need the pw
				msg = f"Hey Josh,\n\nA news release from Canopy Growth has been posted:\n\n{url.get('href')}\n\nYour friend,\nCanopy Updates"
				send_email('canopy.updates@gmail.com','not_the_pw','nicholas.jw.wiseman@gmail.com','Canopy Growth News Release',msg)
		time.sleep(30)		