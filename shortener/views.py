from django.shortcuts import redirect
from django.http import HttpResponse
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
        if 'invalid shortlink' in e.args:
            # A 404 response would be correct here, but unfortunately it did not hook in to the 404 handler in our project.  
            #return HttpResponse(status=404)
            return redirect('/')  # So instead we redirect to the start page
        else:
            return HttpResponse(e.args)
