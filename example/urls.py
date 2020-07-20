# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/21  4:46


from django.urls import path,re_path
from . import views

urlpatterns=[
    path('publish/',views.PublishView.as_view()),
    re_path('^books/$', views.BookView.as_view()),
    re_path('^books/(?P<pk>.*)/$', views.BookView.as_view()),
]