from django.shortcuts import render, get_object_or_404
from .models import Mineral
from random import choice

# Create your views here.




def index(request):
    mins = Mineral.objects.order_by('name')
    minerals = {"mineral_names": mins}

    return render(request, "rocks/index.html", context=minerals)



def details(request, pk):

    mins = get_object_or_404(Mineral, pk=pk)
    minerals = {"mineral_detail": mins}

    return render(request, "rocks/details.html", context=minerals)

def random(request):
    all = Mineral.objects.all()

    new_all = choice(all)
    random = {"random_mineral": new_all}

    return render(request, "rocks/random.html", context=random)

