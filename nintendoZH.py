from bs4 import BeautifulSoup
import requests
import re

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

class game_obj:
	game_title = ""
	languages = []

if __name__ == "__main__":
	url = "https://www.perfectly-nintendo.com/nintendo-switch-list-of-games-with-english-language-option-in-japan/"
	r  = requests.get(url)
	soup = BeautifulSoup(r.text)
	
	for a in soup.find_all('a'):
		# a.replaceWithChildren()
	    del a['href']
	    del a['rel']
	    del a['target']
	    del a['title']
	    # del a['']

	uls = soup.find_all('ul')

	game_list = []
	for ul in uls:
	    for li in ul.find_all('li'):
	        str_li = str(li)
	        #print (str_li)
	        game = find_between_r(str_li, "<li>", "Yen")
	        
	        lan = find_between_r(str_li, "</a>]", "</li>")
	        lan = find_between_r(lan, "[", "]")
	        
	        if len(lan) and len(game) >0:
	        	#print (game + ":" + lan)
	        	game_item = game_obj()
	        	game_item.game_title = game
	        	game_item.languages = lan.split(",")
	        	game_list.append(game_item)

	for i in game_list:
		for j in i.languages:
			if j.strip() == 'ZH':
				print (i.game_title + '--' + j.strip())

		







