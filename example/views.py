from django.shortcuts import render, HttpResponse

from rest_framework.views import APIView
from . import models
from .utils import serializer
import json
from rest_framework.response import Response


class PublishView(APIView):

    def get(self, request, *args, **kwargs):
        publishs = models.PublishModel.objects.all()
        ser = serializer.PublishSerializer(publishs, many=True)
        data = ser.data
        return HttpResponse(json.dumps(data, ensure_ascii=False))

    def post(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, dict):
            many = False
        elif isinstance(data, list):
            many = True
        else:
            return HttpResponse('error!')
        ser = serializer.PublishSerializer(data=data, many=many)
        ser.is_valid(raise_exception=True)
        # print(ser.validated_data)
        ser.save()
        # publish=serializer.PublishSerializer(obj,many=many)
        # return HttpResponse(json.dumps(publish))
        return HttpResponse('xxxx')

    def put(self, request, *args, **kwargs):
        data = request.data
        obj = models.PublishModel.objects.filter(pk=data.get('id')).first()
        ser = serializer.PublishSerializer(obj, data=data)
        ser.is_valid()
        ser.save()
        return HttpResponse('1111')

from example.utils import paginator as pg
class BookView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                book_query = models.BookModel.objects.get(pk=pk)
                many=False

            except:
                return Response({
                    'status': 1,
                    'msg': '书籍不存在'
                })
        else:
            book_query = models.BookModel.objects.all()
            many=True

        # 分页
        # paginator=pg.MyPagination1()   #page=2&size=3

        # paginator=pg.MyPagination2()    #?limit=3&offset=1

        paginator = pg.MyPagination3()
        book_page_obj = paginator.paginate_queryset(book_query, request=request, view=self)

        book_data = serializer.BookModelSerializer(book_page_obj, many=True).data
        # return Response({
        #     'status': 0,
        #     'msg': 'ok',
        #     'results': book_data
        # })

        return paginator.get_paginated_response(book_data)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        if isinstance(request_data, dict):
            many = False
        elif isinstance(request_data, list):
            many = True
        else:
            return Response({
                'status': 1,
                'msg': '数据有误',
            })
        book_ser = serializer.BookModelSerializer(data=request_data, many=many)
        book_ser.is_valid(raise_exception=True)
        book_obj_list = book_ser.save()
        print(book_obj_list, type(book_obj_list))
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': serializer.BookModelSerializer(book_obj_list, many=many).data
        })
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            pks = [pk]
        else:
            pks = request.data.get('pks')
        num = models.BookModel.objects.filter(pk__in=pks).delete()
        if num:
            return Response({
                'status': 0,
                'msg': '删除成功',
            })
        return Response({
            'status': 1,
            'msg': '删除失败',
        })

from rest_framework.generics import GenericAPIView
class AuthorView(GenericAPIView):
    queryset =models.AuthorModel.objects.all()
    serializer_class = serializer.AuthorModelSerializer
    pagination_class = pg.MyPagination3

    def get(self, request, *args, **kwargs):
        authors=self.get_queryset()
        authors_page=self.paginate_queryset(authors)
        ser=self.get_serializer(authors_page,many=True)
        return Response(ser.data)

from rest_framework.viewsets import GenericViewSet
class AuthorView2(GenericViewSet):
    queryset = models.AuthorModel.objects.all()
    serializer_class = serializer.AuthorModelSerializer
    pagination_class = pg.MyPagination3

    def list(self, request, *args, **kwargs):
        authors = self.get_queryset()
        authors_page = self.paginate_queryset(authors)
        ser = self.get_serializer(authors_page, many=True)
        return Response(ser.data)

from rest_framework.viewsets import ModelViewSet
class AuthorView3(ModelViewSet):
    queryset = models.AuthorModel.objects.all()
    serializer_class = serializer.AuthorModelSerializer
    pagination_class = pg.MyPagination3

from rest_framework.renderers import JSONRenderer,HTMLFormRenderer
class TestView(APIView):
    renderer_classes = [JSONRenderer,HTMLFormRenderer]
    def get(self,request):
        return HttpResponse('xxxxx')