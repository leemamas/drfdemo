# django rest frameword的学习之路
## 1.django的2种视图
>函数视图[function view]
* crsf
* from django.views.decorators.csrf import csrf_exempt
* @crcsrf_exempt
>类视图[class view] CBV
* 基于反射实现根据请求不同执行不同的方法
* 路由url-->as_view方法-->dispatch方法（执行get/post/delete等方法）
* 验证crsf，from django.utils.decorators import method_decorator，@method_decorator(csrf_exempt,name='dispatch')

## 2.rest frameword的ApiView和认证流程
> ApiView
* 基于django的View，丰富了原生的request
> 认证
* 基于BaseAuthentication，重写authenticate()方法
* 局部,在类里面添加 authentication_classes = []
* 全局，在setting中,REST_FRAMEWORK={
    'DEFAULT_AUTHENTICATION_CLASSES':['api.utils.auth.MyAuthentication',]
}