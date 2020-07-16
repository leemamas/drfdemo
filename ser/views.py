from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from . import models
import json
from .utils import serializers

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