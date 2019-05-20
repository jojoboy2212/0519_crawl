from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    if request.method=="POST":
        
        word_query=request.POST.get('word_query')
        URL="https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
        fullURL = URL+word_query
        data = requests.get(fullURL).text


        soup=BeautifulSoup(data, 'html.parser')

        news_title = soup.find_all(class_='_sp_each_title')

        title_list=[]
        for title in news_title:
            title_list.append({'url': title.get('href'), 'title': title.get('title')})
        
        return render(request, 'result.html', {'title_list':title_list})
    else :
        return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')