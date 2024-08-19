from django.shortcuts import render
import pyshorteners
from django.contrib import messages
from .models import UrlDb
from .forms import UrlForm
# Create your views here
# url_shortener and shows_all

def url_shortner(req):
    if req.method == "POST":
        shortener = pyshorteners.Shortener()
        form = UrlForm(req.POST)
        if form.is_valid(): 
            url = form.cleaned_data["url"]
            short_url = shortener.tinyurl.short(url)
            print(short_url)
            #print(form)
            form.instance.short_url = short_url
            #UrlDb.objects.create(url=url, short_url=short_url)
            form.save()
            messages.success(req, 'Generated')
        else:
            print(form.errors)

    return render(req, "main/url_shortener.html" ,{'form': UrlForm()})

    
def show_all(req):
    all_urls = UrlDb.objects.all()
    return render(req, 'main/show.html' , {"urls":all_urls})
