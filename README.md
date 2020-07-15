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
> 流程
* 请求进来，走dispatch封装request，把所有认证对象封装到Request类中
* 执行ApiView方法中perform_authentication调用request类中的user
* 又调用authenticator类的authenticate认证方法
> 返回3种方式
* None
* 抛出异常
* 元组（request.user,request.auth）
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

## 5.版本控制
> 自定义
* ```
  class MyVersion(BaseVersioning):
    def determine_version(self, request, *args, **kwargs):
        return request.META.get('HTTP_X_API_VERSION', None)
* versioning_class = MyVersion使用
* version=request.version版本，scheme=request.versioning_scheme使用的类对象
> 内置类实现
* AcceptHeaderVersioning
* URLPathVersioning
* NamespaceVersioning
* HostNameVersioning
* QueryParameterVersioning
> 全局默认配置
*   'DEFAULT_VERSION':'v1',
*   'ALLOWED_VERSIONS':['v1','v2'],
*   'VERSION_PARAM':'ver',
> 实操
* 路径中传参，versioning_class = QueryParameterVersioning
* 如http://127.0.0.1:8888/api/version/?ver=v3，默认保是v1,可以对版本赋值,超出即异常
* url中实现versioning_class = URLPathVersioning
* http://127.0.0.1:8888/api/v1/version2/
* re_path('(?P<ver>[v1|v2|v3]+)/version2/', views.VersionView2.as_view(),name='ver')
* 反转版本api的url
* url=request.versioning_scheme.reverse(viewname='ver',request=request)
## 解析器


> 了解基础知识：request.POST/request.body 

* request.POST要取得值，必须 

1.请求头：Content-Type：application/x-www-form-urlencoded

2.数据格式: 如name=tom&age=18
1. form表单提交
```html
<from method='post' action=''>
	user:<input type='text' name='user>
	pwd:<input type='text' name='pwd>
</form>
<!--内部默认转为user=xx&pwd=xxx的数据格式-->
```
2. ajax提交
```javascript
$.ajax({
			uri:xxx,
			type:POST,
			data:{
				'name':'tom',
				'age':18
			}
		})
		##内部默认转为name=tom&age=18的数据格式
		$.ajax({
			uri:xxx,
			type:POST,
			headers:{
				'Content-Type'：'application/json'
			}
			data:{
				'name':'tom',
				'age':18
			}
		})
		$.ajax({
			uri:xxx,
			type:POST,
			headers:{
				'Content-Type'：'application/json'
			}
			data:JSON.stringfy({
				'name':'tom',
				'age':18
			})
		})
		##最后2种，body有值，POST没有
		##可以通过json.loads(request.body)取值
```
* rest framework解析器，对请求体数据进行解析
> 代码流程:
- dispatch-->initialize_request-->Request类得到get_parsers所以的parser_classes的对象
- request.data-->._load_data_and_files()-->_parse()
- 通过negotiator.select_parser(self, self.parsers)比较请求对象self.content_type和parser_classes=[]的对象得到parse
- 最后通过parse()得到请求体的数据
> 全局配置使用
* 'DEFAULT_PARSER_CLASSES':['rest_framework.parsers.JSONParser','rest_framework.parsers.FormParser']

* request.data