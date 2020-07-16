# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/16  17:54
from . import views


from django.urls import path

urlpatterns = [
    path('roles/',views.RoleView.as_view()),
]