from django.shortcuts import render, get_object_or_404
from .models import Mineral


# Create your views here.


def index(request):
    mins = Mineral.objects.order_by('name')
    minerals = {"mineral_names": mins}

    return render(request, "rocks/index.html", context=minerals)



def details(request, pk):

    mins = get_object_or_404(Mineral, pk=pk)
    minerals = {"mineral_detail": mins}

    return render(request, "rocks/details.html", context=minerals)
