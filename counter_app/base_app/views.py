from django.shortcuts import render
from .models import Person
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    persons = Person.objects.all()
    return_dict = {
        'person':persons,
    }
    print(persons)
    return render(request,'index.html',context=return_dict)

def reset(request):
    persons = Person.objects.all()
    p = persons[0]

    p.visitors_in = 0
    p.visitors_out = 0
    p.save()

    return HttpResponseRedirect(reverse('base_app:home'))