from django.shortcuts import render
from django.conf import settings
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
        return Response(p.visitors_in)
    else:
        return Response('Invalid Request!')
    pass

@api_view(['GET'])
def getvisitorout(request,passphrase):
    if(passphrase == settings.PASSPHRASE):
        person = Person.objects.all()
        p = person[0]
        return Response(p.visitors_out)
        pass
    else:
        return Response('Invalid Request!')
    pass

@api_view(['GET'])
def setvisitorin(request,passphrase):
    if(passphrase == settings.PASSPHRASE):
        pass
    else:
        return Response('Invalid Request!')
    pass

@api_view(['GET'])
def setvisitorout(request,passphrase):
    if(passphrase == settings.PASSPHRASE):
        pass
    else:
        return Response('Invalid Request!')
    pass