from django.shortcuts import render, HttpResponse
from core.models import Bottle

# core/views.py
def contacts(request):
    return render(request, 'core/contacts.html')



def bottle_list(request):
    context = {}
    context["core"] = Bottle.objects.all()
    return render(request, 'botlle.html', context)

def bottle_detail(request, id):
    contex = {
        "bottle": Bottle.objects.get(id=id)
        #SELECT * FROM Bottle WHERE id+id:
    }
    return render(request, "bottle_info.html", contex)


def about(request):
    return render(request, 'about.html')

def photo(request):
    return render(request, 'static.html')


def makers_list(requests):
    context  = {}
    #SELECT * FROM Bottle
    bottles_lists = Bottle.objects.all()
    context["bottles_list"] = bottles_lists
    return render(requests, 'makers.html', context)
#render - принимает запрос,



