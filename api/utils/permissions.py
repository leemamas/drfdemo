# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/15  0:38

from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    message='not permission!'
    def has_permission(self, request, view):
        if not request.user.user_type>1:
            return False
        return True

