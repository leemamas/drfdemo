# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/14  23:35
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('login_form/', views.login_form),
    # path('login_data/', views.login_data),
    # path('login/', views.LoginView.as_view()),
    path('auth/', views.AuthView.as_view()),
    path('user/', views.UserInfoView.as_view()),
    path('vip/', views.VipView.as_view()),
    path('version/', views.VersionView.as_view()),
    re_path('(?P<ver>[v1|v2|v3]+)/version2/', views.VersionView2.as_view(),name='ver'),
    path('parse/', views.TestParserView.as_view()),
]
