from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from .forms import DrinkForm
from .models import Drinks




def home(request):
   beverages = Drinks.objects.all()

   return render(request, 'home.html', {'beverages': beverages})



def new(request):
   

   if (request.method  == 'POST'):
      form = DrinkForm(request.POST)
      if (form.is_valid()):
         form.save()
         beverage = form.cleaned_data['name']
         description = form.cleaned_data['description']
         return redirect('home')
   else:
       
       form = DrinkForm()
       return render(request, 'new.html', {'form': form})

