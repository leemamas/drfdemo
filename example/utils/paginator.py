# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/21  6:27
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyPagination1(PageNumberPagination):
    '''
    根据页码进行分页
    '''
    #每页显示条数
    page_size = 2
    #url传入每页显示条数的key
    page_query_param = 'page'
    #url传入页码的key
    page_size_query_param = 'size'
    #每页最大显示条数
    max_page_size = 50

class MyPagination2(LimitOffsetPagination):
    '''
    位置和个数进行分页
    '''
    # 默认每页显示的数据条数
    default_limit = 1
    # URL中传入的显示数据条数的参数
    limit_query_param = 'limit'
    # URL中传入的数据位置的参数
    offset_query_param = 'offset'
    # 最大每页显得条数
    max_limit = 50

class MyPagination3(CursorPagination):
    '''
    游标分页
    '''
    # URL传入的游标参数
    cursor_query_param = 'cursor'
    # 默认每页显示的数据条数
    page_size = 1
    # URL传入的每页显示条数的参数
    page_size_query_param = 'size'
    # 每页显示数据最大条数
    max_page_size = 50

    # 根据ID从大到小排列
    ordering = "id"