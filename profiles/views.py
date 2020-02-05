from django.shortcuts import render,redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup as Bsoup 
import requests
import urllib3
import scholarly
import re
# Create your views here.
def searchAuthors(request):
	

	keyword = request.POST.get('keyword',False)
	Authors =[]
	Authorlink = []
	url = 'http://scholar.google.com/citations?view_op=search_authors&mauthors='+str(keyword)+'&hl=en&oi=drw'
	response = requests.get(url)
	# print(response.text[:500])

	html_soup = Bsoup(response.text,'html.parser')
	# print(type(html_soup))
	#print((html_soup))


	name_containers = html_soup.find_all('div',class_='gsc_1usr')
	# print(type(name_containers))
	# print(len(name_containers))
	interests = []

	for container in name_containers:
		interest = container.find_all('a',class_ = 'gs_ai_one_int')
		mylist = []
		for i in interest:
			mylist.append(i.text)
		interests.append(mylist)
		Authors.append(container.div.h3.a.text)
		k = str(container.div.h3.a['href'])
		Authorlink.append("https://scholar.google.com/citations?view_op=medium_photo&user="+k[k.index('='):])
	author = zip(Authors, Authorlink,interests)



	# for i in Authors:
	# 	search_query = scholarly.search_author(i)
	# 	author = next(search_query).fill()

	return render(request,'profiles/index.html',context= {'author':author})

# def Author(request):

# 	context = {
# 		'Name':Name,
# 		'affiliated':affiliated,
# 	}

#  	return render(request,'profiles/author.html',context)

def SingleAuthor(request,authorName):


	# Name = str(request.Get.get('auth',False))
	search_query = scholarly.search_author(authorName)
	author = next(search_query).fill()
	publicationlist = enumerate([pub.bib['title'] for pub in author.publications])
	context ={
		'author':author,
		'publicationlist':publicationlist,
	}

	return render(request,'profiles/author.html',context)
	
def SinglePublication(request,authorName,pubind):

	search_query = scholarly.search_author(authorName)
	author = next(search_query).fill()
	myPublication = author.publications[pubind].fill()
	pages = None 
	volume = None
	journal = None
	context = {}
	#All the Attributes
	title = myPublication.bib['title']
	abstract = re.sub('<[^>]+>', '', str(myPublication.bib['abstract']))
	author = myPublication.bib['author']
	eprint = myPublication.bib['eprint']
	if 'journal' in myPublication.bib.keys():
		journal = myPublication.bib['journal']
	if 'pages' in myPublication.bib.keys():
		pages = myPublication.bib['pages']
	
	originalUrl = myPublication.bib['url']
	if 'volume' in myPublication.bib.keys():
		volume = myPublication.bib['volume']
	
	year = myPublication.bib['year']
	citedby = myPublication.citedby
	idCitations = myPublication.id_citations
	idScholarcitedby = myPublication.id_scholarcitedby


	
	context['authorName']=authorName,
	context['author']=author,
	context['pubind']=pubind,
	context['title']=title,
	context['abstract']=abstract,
	context['pages']=pages
	context['eprint']=eprint,
	context['journal']=journal,
	context['originalUrl']=originalUrl,
	context['volume']=volume
	context['year']=year,
	context['citedby']=citedby,
	context['idCitations']=idCitations,
	context['idScholarcitedby']=idScholarcitedby
	return render(request,'profiles/publication.html',context)