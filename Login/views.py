from django.shortcuts import render
from .scrape import homePage,ecoPage,techPage,sportPage
# Create your views here.



def home(r):
	news=homePage()
	news=news.hNews()
	return render(r,'home.html',{'data':news})

def econo(r):
	news1=ecoPage()
	news1=news1.ec()
	return render(r,'home.html',{'data':news1})

def tech(r):
	news2=techPage()
	news2=news2.tNews()
	return render(r,'home.html',{'data':news2})

def sport(r):
	news3=sportPage()
	news3=news3.sNews()
	return render(r,'home.html',{'data':news3})




