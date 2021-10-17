from django.shortcuts import render
from .models import Person
# Create your views here.
def index(request):
    persons = Person.objects.all()
    return_dict = {
        'person':persons,
    }
    print(persons)
    return render(request,'index.html',context=return_dict)