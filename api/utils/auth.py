# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/15  0:16

from rest_framework.authentication import BaseAuthentication
from api import models
from rest_framework import exceptions

class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token=request.query_params.get('token')
        token_obj=models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('auth failure!')

        return (token_obj.user,None)