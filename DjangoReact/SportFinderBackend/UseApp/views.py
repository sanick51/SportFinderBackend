from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json 
from UseApp.models import User
from UseApp.serializers import UserSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)
        return JsonResponse(userSerializer.data, safe=False)

    elif request.method=='POST':
        users_data=JSONParser().parse(request)
        userSerializer = UserSerializer(data=users_data)
        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("El correo ya se encuentra registrado",safe=False)
    
    elif request.method=='PUT':
        users_data = JSONParser().parse(request)
        users=User.objects.get(userId=users_data['userId'])
        userSerializer=UserSerializer(users,data=users_data)
        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        users=User.objects.get(userId=id)
        users.delete()
        return JsonResponse("Deleted Succeffuly!!", safe=False)

@csrf_exempt
def loginApi(request,id=0):
   
    if request.method=='POST':
        users = User.objects.all()
        allUsers = UserSerializer(users, many=True)
        users_data=JSONParser().parse(request)
        userIn = list(users_data.values())[0]
        passIn = list(users_data.values())[1]

        for item in allUsers.data[:]:
            dic = dict(item)
            values = list(dic.values())
            userEmail = values[1]
            print("1" , userIn)
            print("2" , userEmail)
            if(userIn== userEmail):
                userPass = values[2]
                print("1" , userPass)
                print("2" , passIn)
                if(userPass== passIn):
                    return JsonResponse("Inicio de sesión exitoso",safe=False)
    return JsonResponse("Usuario o contraseña incorrectos",safe=False)
       
    
  
