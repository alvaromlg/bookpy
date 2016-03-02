import urllib2

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.conf import settings


def finder_index(request):
    template = loader.get_template('finder/index.html')
    return HttpResponse(template.render())

def finder_results(request):
    search_box = request.GET["search_box"]
    template = loader.get_template('finder/results.html')
    api = settings.GOOGLE_API_URL + "?q=%s" % search_box
    read = urllib2.urlopen(api)
    read = read.read()

    context = {
        "looking" : search_box,
        "result" : read
    }


    return HttpResponse(template.render(context))
