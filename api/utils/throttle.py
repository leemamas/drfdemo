# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/15  10:28
from rest_framework.throttling import SimpleRateThrottle


class SimpleVisitThrottle(SimpleRateThrottle):
    scope = 'simple'

    def get_cache_key(self, request, view):
        return request.user

class VipVisitThrottle(SimpleRateThrottle):
    scope = 'vip'

    def get_cache_key(self, request, view):
        return request.user
