from django.shortcuts import redirect
from django.http import HttpResponse #, HttpResponseRedirect
from shortener import shortener


# Create your views here.
def test(request, link):
    if request.user.is_authenticated:
        data = shortener.create(request.user, link)
        return HttpResponse(data)
    else:
        return HttpResponse('unauthorized')


def expand(request, link):
    try:
        link = shortener.expand(link)
        return redirect(link)  # TODO: permanent=True
    except Exception as e:
        if 'invalid shortlink' in e.args:
            return HttpResponse(status=404)
            #return HttpResponseRedirect('/404')
        else:
            return HttpResponse(e.args)
