from urllib.request import urlopen as uo
from urllib.request import Request as r
from bs4 import BeautifulSoup as sp
import random
# import requests as req
# import threading as tr 
class homePage():
	url1='https://indianexpress.com/section/india/'
	url2='https://timesofindia.indiatimes.com/news'
	url3='https://www.indiatoday.in/india'

	def sc(self):
		# pg=r(url1,{'User-Agent':'Magic Browser'})
		pg=r(homePage.url1, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		# pg=req.get(homePage.url1)
		pg=uo(pg)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img class="img-fluid" src="https://indianexpress.com/wp-content/themes/indianexpress/images/indian-express-logo-n.svg" title="The Indian Express" alt="The Indian Express">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgsl=soup.find('div',{'class':'nation'}).findAll('div',{'class':'snaps'})
			headsl=soup.find('div',{'class':'nation'}).findAll('h2',{'class':'title'})
			for i in imgsl:
				links.append(i.find('a').get('href'))
				logos.append(logourl)
				imgs.append(i.find('img').get('data-lazy-src'))
			for i in headsl:
				heads.append(i.find('a').text)
			news=list(zip(imgs,heads,links,logos))
			return news
		except:
			news=[]
			return news

	def sc1(self):
		pg=r(homePage.url2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		pg=uo(pg)
		# pg=req.get(homePage.url2)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img alt="Times of India" class="img-fluid" src="https://static.mediawire.in/brands/profilepic/1117/TOI%20Logo%20in%20Red%20Bakcground.jpg">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgs1=soup.find('div',{'class':'listing4 clearfix'}).find('ul').findAll('li')
			for i in imgs1:
				heads.append(i.find('span').find('a').text)
				links.append(i.find('span').find('a').get('href'))
				imgs.append(i.find('a').find('img').get('data-src'))
				logos.append(logourl)
			news=list(zip(imgs,heads,links,logos))
			return news
		except:
			news=[]
			return news

	def sc2(self):
		pg=r(homePage.url3, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		pg=uo(pg)
		# pg=req.get(homePage.url3)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img src="https://www.cs.utah.edu/~deb/assets/images/media/logo_it.png" alt="India Today" class="img-fluid">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgs1=soup.find('div',{'class':'view-content'}).findAll('div',{'class':'catagory-listing'})
			for i in imgs1:
				imgs.append(i.find('div',{'class':'pic'}).find('img').get('src'))
				heads.append(i.find('div',{'class':'detail'}).find('a').text)
				links.append(i.find('div',{'class':'detail'}).find('a').get('href'))
				logos.append(logourl)
			news=list(zip(imgs,heads,links,logos))
			return news
		except:
			news=[]
			return news

	def hNews(self):
		n=homePage.sc(self)
		n1=homePage.sc1(self)
		n2=homePage.sc2(self)
		n.extend(n1)
		n.extend(n2)
		random.shuffle(n)
		return n

class ecoPage():
	url1='https://www.financialexpress.com/economy/'

	def ec(self):
		# pg=r(url1,{'User-Agent':'Magic Browser'})
		pg=r(ecoPage.url1, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		pg=uo(pg)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img class="img-fluid" src="https://www.financialexpress.com/wp-content/themes/vip/financialexpress/assets/images/fe-logo-with-read-to-lead.svg" alt="Financial Express">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgl1=soup.find('div',{'class':'leftcol'}).findAll('figure')
			titles1=soup.find('div',{'class':'leftcol'}).findAll('h2')
			titles2=soup.find('div',{'class':'leftcol'}).findAll('h3')
			for i in imgl1:
				imgs.append(i.find('img').get('data-src'))
				links.append(i.find('a').get('href'))
				logos.append(logourl)
			for i in titles1:
				heads.append(i.find('a').text)
			for i in titles2:
				heads.append(i.find('a').text)
			news=zip(imgs,heads,links,logos)
			return news
		except:
			news=[]
			return news
class techPage():
	url1='https://indianexpress.com/section/technology/'
	url2='https://www.indiatoday.in/technology/news'
	url3='https://gadgets.ndtv.com/news'

	def tc(self):
		pg=r(techPage.url1, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		pg=uo(pg)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img class="img-fluid" src="https://indianexpress.com/wp-content/themes/indianexpress/images/indian-express-logo-n.svg" title="The Indian Express" alt="The Indian Express">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgsl=soup.find('ul',{'class':'article-list'}).findAll('li')
			for i in imgsl:
				imgs.append(i.find('img').get('src'))
				links.append(i.find('a').get('href'))
				logos.append(logourl)
				heads.append(i.find('img').get('alt'))
			news=list(zip(imgs,heads,links,logos))
			return news
		except:
			news=[]
			return news

	def tc1(self):
		pg=r(techPage.url2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		pg=uo(pg)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img src="https://akm-img-a-in.tosshub.com/indiatoday/../sites/all/themes/itg/logo.png?v=1.3" alt="India Today" class="img-fluid">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgs1=soup.find('div',{'class':'view-content'}).findAll('div',{'class':'catagory-listing'})
			for i in imgs1:
				imgs.append(i.find('div',{'class':'pic'}).find('img').get('src'))
				heads.append(i.find('div',{'class':'detail'}).find('a').text)
				links.append(i.find('div',{'class':'detail'}).find('a').get('href'))
				logos.append(logourl)
			news=list(zip(imgs,heads,links,logos))
			return news
		except:
			news=[]
			return news

	def tc2(self):
		pg=r(techPage.url3, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		pg=uo(pg)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img class="img-fluid" src="https://cdn.gadgets360.com/gadgets360_logo.png" alt="Technology News" title="NDTV Gadgets 360">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgsl=soup.find('div',{'class':'story_list row margin_b30'}).findAll('div',{'class':'thumb'})
			for i in imgsl:
				if i.find('img').get('src')=="https://gadgets.ndtv.com/static/icons/img_120n.png":
					imgs.append(i.find('img').get('data-original'))
				else:
					imgs.append(i.find('img').get('src'))
				links.append(i.find('a').get('href'))
				logos.append(logourl)
				heads.append(i.find('img').get('alt'))
			news=list(zip(imgs,heads,links,logos))
			return news
		except:
			news=[]
			return news

	def tNews(self):
		n=techPage.tc(self)
		n1=techPage.tc1(self)
		n2=techPage.tc2(self)
		n.extend(n1)
		n.extend(n2)
		random.shuffle(n)
		return n


class sportPage():
	url1='https://indianexpress.com/section/sports/'
	url2='https://timesofindia.indiatimes.com/news'
	url3='https://www.indiatoday.in/sports/cricket'

	def sp(self):
		# pg=r(url1,{'User-Agent':'Magic Browser'})
		pg=r(sportPage.url1, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		pg=uo(pg)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img class="img-fluid" src="https://indianexpress.com/wp-content/themes/indianexpress/images/indian-express-logo-n.svg" title="The Indian Express" alt="The Indian Express">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgsl=soup.find('div',{'class':'nation'}).findAll('div',{'class':'snaps'})
			headsl=soup.find('div',{'class':'nation'}).findAll('h2',{'class':'title'})
			for i in imgsl:
				links.append(i.find('a').get('href'))
				logos.append(logourl)
				imgs.append(i.find('img').get('data-lazy-src'))
			for i in headsl:
				heads.append(i.find('a').text)
			news=list(zip(imgs,heads,links,logos))
			return news
		except:
			news=[]
			return news

	# def sp1(self):
	# 	pg=r(sportPage.url2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
	# 	pg=uo(pg)
	# 	pg_ht=pg.read()
	# 	pg.close()
	# 	soup=sp(pg_ht,'html.parser')
	# 	logourl='<img alt="Times of India" class="img-fluid" src="https://static.mediawire.in/brands/profilepic/1117/TOI%20Logo%20in%20Red%20Bakcground.jpg">'
	# 	heads=[]
	# 	links=[]
	# 	imgs=[]
	# 	logos=[]
	# 	try:
	# 		imgs1=soup.find('div',{'class':'listing4 clearfix'}).find('ul').findAll('li')
	# 		for i in imgs1:
	# 			heads.append(i.find('span').find('a').text)
	# 			links.append(i.find('span').find('a').get('href'))
	# 			imgs.append(i.find('a').find('img').get('data-src'))
	# 			logos.append(logourl)
	# 		news=list(zip(imgs,heads,links,logos))
	# 		return news
	# 	except:
	# 		news=[]
	# 		return news

	def sp2(self):
		pg=r(sportPage.url3, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
		pg=uo(pg)
		pg_ht=pg.read()
		pg.close()
		soup=sp(pg_ht,'html.parser')
		logourl='<img src="https://www.cs.utah.edu/~deb/assets/images/media/logo_it.png" alt="India Today" class="img-fluid">'
		heads=[]
		links=[]
		imgs=[]
		logos=[]
		try:
			imgs1=soup.find('div',{'class':'view-content'}).findAll('div',{'class':'catagory-listing'})
			for i in imgs1:
				imgs.append(i.find('div',{'class':'pic'}).find('img').get('src'))
				heads.append(i.find('div',{'class':'detail'}).find('a').text)
				links.append(i.find('div',{'class':'detail'}).find('a').get('href'))
				logos.append(logourl)
			news=list(zip(imgs,heads,links,logos))
			return news
		except:
			news=[]
			return news

	def sNews(self):
		n=sportPage.sp(self)
		# n1=sportPage.sp1(self)
		n2=sportPage.sp2(self)
		# n.extend(n1)
		n.extend(n2)
		random.shuffle(n)
		return n	
		