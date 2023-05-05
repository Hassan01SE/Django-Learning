from django.shortcuts import render
from myapp.forms import BookingForm


def home(request):
    return render(request, "homepage.html")

def form_view(request):

     form = BookingForm()
     if request.method == 'POST':
         form = BookingForm(request.POST)
         if form.is_valid():
             form.save()
             person = form.cleaned_data['first_name']
             return render(request,"bookedsuccess.html", {"person":person})
     context = {"form" : form}
     return render(request, "booking.html", context)