from django.shortcuts import render
# from django.http import JsonResponse
# from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advocate
from .serializers import AdvocateSerializer

from django.db.models import Q

# Create your views here.

#GET /advocates
#POST /advocates

#GET /advocates/:id
#PUT /advocates/:id
#DELETE /advocates/:id


@api_view(['GET'])#GET here means get the data from this site
def endpoints(request):
    data=['/advocates','advcates/:username']
    return Response(data)#Only input can be dictionaries not objects

@api_view(['GET','POST'])    
def advocate_list(request):
    # data=['Mohit','Madhav','Aradhaya']
    # advocates=Advocate.objects.all()

    #Trying to put in if conditions for GET and POST request
    if request.method=='GET':
        #Giving a query for search function
        query=request.GET.get('query')#GET will accept the value from frontend
        #/advocates/?query=MANAN
        if query==None:
            query=''

        advocates=Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))    #username__icontains is an object which will help in search even the half of the word 
        #We are also going to use q lookups for the simultaneous search in both username and bio                         # i in icontains makes it non-case sensitive
        serializer =AdvocateSerializer(advocates,many=True)
        # return Response(advocates)#Response cannot serialize a class[models] so we also have to make a serializer
        return Response(serializer.data)
    if request.method=='POST':
        Advocate.objects.create(
        username=request.data['username'],
        bio=request.data['bio']
    )
    return Response('ADDED')
    


@api_view(['GET'])    
def advocate_detail(request,username):
    # data=username
    advocate=Advocate.objects.get(username=username)
    serializer=AdvocateSerializer(advocate,many=False)#many is going to be false in this case because we just want to output a single object
    return Response(serializer.data)    