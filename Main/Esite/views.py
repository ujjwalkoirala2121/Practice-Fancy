from django.shortcuts import render
from .models import Shoes, Accessories
# Create your views here.

def index(request):
    shoes = Shoes.objects.all()
    accessories = Accessories.objects.all()
    return render(request, 'index.html', {'shoes': shoes, 'accessories': accessories })



