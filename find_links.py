
def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ''

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		url, end_quote = None, 0
	else:
		start_quote = page.find('"',start_link)
		end_quote = page.find('"',start_quote + 1)
		url = page[start_quote+1:end_quote]

	return url, end_quote

def print_all_links(page):
	while True:
		url, end_pos = get_next_target(page)
		if url:
			print url
			page = page[end_pos:]
		else:
			break



#page = 'there is a link <a href="here.com"> here '
#page = 'there is no link here '


#url = "http://coryllus.salon24.pl"
url = "http://xkcd.com/353"
page = get_page(url)
print_all_links(page)
