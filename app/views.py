"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *;


def artistcreate(request):
    if request.method == "GET": 
        form = ArtistForm();
        return render(request, 'app/create.html', { 'form':form ,'title':'Create Artist',
                'year':datetime.now().year,});
    elif request.method == "POST":
        form = ArtistForm(request.POST);
        if form.is_valid():
            form.save();
            return HttpResponseRedirect('/artists');
        else:
            return HttpResponse(status=406)
        

def artists(request):
    #return HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello, Django</h1></body></html>');
    artists = Artist.objects.all();
    return render_to_response('app/artists.html', { 'artists': artists,'year':datetime.now().year, });

def artistdetails(request, name):
    artist = Artist.objects.get(name = name);
    return render_to_response('app/artistdetails.html', { 'artist': artist,'year':datetime.now().year, });

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Online Music Directory.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Online Music Directory.',
            'year':datetime.now().year,
        })
    )
