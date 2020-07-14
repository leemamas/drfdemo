#django rest frameword的学习之路
##1.django的2种视图
>函数视图[function view]
* crsf
* from django.views.decorators.csrf import csrf_exempt
* @crcsrf_exempt
>类视图[class view] CBV
* 基于反射实现根据请求不同执行不同的方法
* 路由url-->as_view方法-->dispatch方法（执行get/post/delete等方法）
* 验证crsf，from django.utils.decorators import method_decorator，@method_decorator(csrf_exempt,name='dispatch')