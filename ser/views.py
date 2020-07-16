from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from . import models
import json
from .utils import serializers
from django.http import JsonResponse

class RoleView(APIView):

    def get(self, request, *args, **kwargs):
        # method1:
        # roles = models.Role.objects.all().values('id', 'title')
        # roles = list(roles)
        # ret = json.dumps(roles, ensure_ascii=False)  # ensure_ascii中文显示

        # method2:
        # 多个对象
        # roles_obj = models.Role.objects.all()
        # ser = serializers.RoleSerializer(instance=roles_obj, many=True)
        # ret = json.dumps(ser.data, ensure_ascii=False)

        # 单个对象
        role_obj = models.Role.objects.all().first()
        ser = serializers.RoleSerializer(instance=role_obj, many=False)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)

class UserView(APIView):

    def get(self, request, *args, **kwargs):

        users_obj=models.User.objects.all()
        print(users_obj)
        ser=serializers.UserSerializer(instance=users_obj,many=True)
        ret=json.dumps(ser.data, ensure_ascii=False)

        return HttpResponse(ret)

    def post(self,request,*args,**kwargs):

        data = request.data
        print(data)
        ser = serializers.UserSerializer2(data=data)

        ser.is_valid(raise_exception=True)
        # print(ser.validated_data)
        # print(ser.errors)
        ser.save()
        return HttpResponse('ok')

    def put(self,request,*args,**kwargs):
        data = request.data
        user_obj= models.User.objects.get(pk=data.get("id"))
        print(data)
        print(user_obj)
        ser = serializers.UserSerializer2(instance=user_obj,data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return HttpResponse('ok')

class UserView2(APIView):
    def get(self, request, *args, **kwargs):
        data=request.data
        users_obj = models.User.objects.all()
        ser=serializers.UserModelSerializer(instance=users_obj,many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)

        return HttpResponse(ret)

    def post(self,request,*args,**kwargs):

        data = request.data
        ser = serializers.UserModelSerializer(data=data)
        ser.is_valid(raise_exception=True)

        ser.save()
        return HttpResponse('ok')

    def put(self, request, *args, **kwargs):
        data = request.data
        user_obj = models.User.objects.get(pk=data.get("id"))
        ser = serializers.UserModelSerializer(instance=user_obj, data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return HttpResponse('ok')