from django.shortcuts import redirect
from django.http import HttpResponse, Http404
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
        return redirect(link)
    except Exception as e:
        raise Http404(e)
