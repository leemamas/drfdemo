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
## 3.rest framework 权限
* 基于BasePermission，重写has_permission()
* 返回False没权限，反之即有
* message重写返回信息
* 全局DEFAULT_AUTHENTICATION_CLASSES

## 4.控制访问频率（节流）
* 使用DEFAULT_THROTTLE_CLASSES和DEFAULT_THROTTLE_RATES设置全局设置默认的限制策略
* DEFAULT_THROTTLE_CLASSES:创建自定义节流阀，请覆盖BaseThrottle并实施.allow_request(self, request, view),重写.wait()方法,返回建议的秒数
* DEFAULT_THROTTLE_RATES：在自定义的节流阀中，通过scope设置作用域，.get_cache_key(self, request, view)重写，对缓存定义作为key，返回通过什么代理进行节流
* DEFAULT_THROTTLE_RATES用到second，minute，hour或day作为节流段，如‘10/m' ,'500/d'等等