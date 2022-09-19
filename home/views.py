from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer, UserSerializer
from .models import Task
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response(
        {
            'satus':200,
            "message":"yes!django restframework is working"
        }
    )
    
@api_view(['GET']) 
def tasklist(request):
    
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET']) 
def taskdetail(request,pk):
    tasks=Task.objects.filter(id=pk)
    serializer=TaskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return response(serializer.data)
     
@api_view(['POST'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return response("Item successfully deleted")

#class based view

class RegisterUser(APIView):
    def post(self , request):
        serializer=UserSerializer(data= request.data)
        
        if not serializer.is_valid():
            return response({"status" : 404,"errors" : serializer.errors,"message" : "something went wrong"})
        
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token_obj , _ =Token.objects.get_or_create(user=user)
        return response({"status" : 200,"payload" : serializer.data,"token" : str(token_obj),"message" : "your data is saved in db"})
    
