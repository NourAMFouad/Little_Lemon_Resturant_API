from django.shortcuts import render

from .models import Menu, Booking 
from .forms import BookingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    # to list all items that admin add it 
    menu_data = Menu.objects.all()
    context = {
        'menu' : menu_data
    }
    return render(request, 'menu.html',{"menu":context} )

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form' : form}
    return render(request, 'book.html', context)


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 