from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base_app.models import Person
# Create your views here.

#now i need 4 apis one to get old visitor and one to update.

@api_view(['GET'])
def getvisitorin(request,passphrase):
    if(passphrase == settings.PASSPHRASE):
        person = Person.objects.all()
        p = person[0]
        header = {
            "Access-Control-Allow-Origin" : "*", 
            "Access-Control-Allow-Credentials" : True
        }
        return Response(p.visitors_in,headers=header)
    else:
        return Response('Invalid Request!')
    pass

@api_view(['GET'])
def getvisitorout(request,passphrase):
    if(passphrase == settings.PASSPHRASE):
        person = Person.objects.all()
        p = person[0]
        header = {
            "Access-Control-Allow-Origin" : "*", 
            "Access-Control-Allow-Credentials" : True
        }
        return Response(p.visitors_out,headers=header)
        pass
    else:
        return Response('Invalid Request!')
    pass

@api_view(['GET'])
def setvisitorin(request,passphrase,inp):
    if(passphrase == settings.PASSPHRASE):
        person = Person.objects.all()
        p = person[0]
        p.visitors_in = inp
        p.save()
        return HttpResponseRedirect(reverse('base_app:home'))
    else:
        return Response('Invalid Request!')
    pass

@api_view(['GET'])
def setvisitorout(request,passphrase,inp):
    if(passphrase == settings.PASSPHRASE):
        person = Person.objects.all()
        p = person[0]
        p.visitors_out = inp
        p.save()
        return HttpResponseRedirect(reverse('base_app:home'))
        pass
    else:
        return Response('Invalid Request!')
    pass