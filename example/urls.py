# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/21  4:46


from django.urls import path,re_path,include
from . import views

from rest_framework import routers

router=routers.DefaultRouter()
router.register('authors3',views.AuthorView3)

urlpatterns=[
    path('publish/',views.PublishView.as_view()),
    re_path('^books/$', views.BookView.as_view()),
    re_path('^books/(?P<pk>.*)/$', views.BookView.as_view()),
    path('authors/',views.AuthorView.as_view()),
    path('authors2/',views.AuthorView2.as_view({'get':'list'})),
    # re_path('^authors3/$',views.AuthorView3.as_view({'get': 'list','post':'create'})),
    # re_path('^authors3/(?P<pk>\d+)/$',views.AuthorView3.as_view({'get': 'retrieve','put':'update','delete':'destroy','patch':'partial_update'})),
    path('',include(router.urls))
]