from django.shortcuts import render,HttpResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.http import JsonResponse
from api.utils import auth

#django两种视图
#1.函数视图[function view]FBV
def login_form(request):

    html='''
        <form method='post' action='/api/login_data/'>
            user:<input type='text' name='user'><br>
            pwd:<input type='password' name='pwd'><br>
            <input type='submit' value='Login'>
        </form>
    '''
    return HttpResponse(html)



@csrf_exempt
def login_data(request):

    user=request.POST.get('user')
    pwd=request.POST.get('pwd')
    user_obj=models.User.objects.filter(user=user,pwd=pwd).first()
    if not user_obj:
        return HttpResponse('user or pwd error!')

    return HttpResponse('Login success!')

#2.类视图[class view] CBV
#基于反射实现根据请求不同执行不同的方法
#路由url-->as_view方法-->dispatch方法（执行get/post/delete等方法）


@method_decorator(csrf_exempt,name='dispatch')
class LoginView(View):
    def get(self,request,*args,**kwargs):
        html = '''
              <form method='post' action='/api/login/'>
                  user:<input type='text' name='user'><br>
                  pwd:<input type='password' name='pwd'><br>
                  <input type='submit' value='Login'>
              </form>
          '''
        return HttpResponse(html)

    def post(self, request, *args, **kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user_obj = models.User.objects.filter(user=user, pwd=pwd).first()
        if not user_obj:
            return HttpResponse('user or pwd error!')

        return HttpResponse('Login success!')

def md5(user):
    '''
    MD5加密user和时间戳生成token
    :param user:
    :return:
    '''
    import hashlib
    import time
    m=hashlib.md5(bytes(user,encoding='utf-8'))
    ctime=str(time.time())
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

#基于rest framwork 的ApiView
class AuthView(APIView):
    authentication_classes = []
    def post(self,request,*args,**kwargs):
        ret={
            'code':1000,
            'msg':None
        }

        try:
            user=request.data.get('user')
            pwd=request.data.get('pwd')
            user_obj = models.User.objects.filter(user=user, pwd=pwd).first()
            if not user_obj:
                ret['code']=1001
                ret['msg']='user or pwd error!'
            else:
                token=md5(user)
                models.UserToken.objects.update_or_create(user=user_obj,defaults={'token':token})
                ret['code'] = 200
                ret['msg'] = 'login success'
                ret['token'] = token
        except:
            ret['code'] = 1002
            ret['msg'] = 'except error!'

        return JsonResponse(ret)

class UserInfoView(APIView):
    # authentication_classes = [auth.MyAuthentication,]
    def get(self, request, *args, **kwargs):

        ret = {
            'code': 200,
            'user':request.user,
            'auth':request.auth
        }
        return JsonResponse(ret)