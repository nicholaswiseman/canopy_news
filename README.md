# canopy_news

A script made as to not miss any news releases from Canopy Growth. 

BeautifulSoup is used to scrape the news release page for all links.

Each link is checked first to see if it is a news release and, if so, we check to see if it's new.

Whether or not it is 'new' is determined by whether is exists in urls.txt.

If it is new, the url is saved to urls. txt and an email is sent with a link to the release.