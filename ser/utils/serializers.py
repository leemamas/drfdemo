# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/16  18:14

from rest_framework import serializers

class RoleSerializer(serializers.Serializer):
    '''
    简单应用序列化
    '''
    title = serializers.CharField()


class UserSerializer(serializers.Serializer):
    '''
    自定义字段
    '''
    user=serializers.CharField()
    pwd=serializers.CharField()
    # type=serializers.CharField(source='user_type') #row.user_type
    level=serializers.CharField(source='get_user_type_display')
    group=serializers.CharField(source='group.title')
    # roles=serializers.CharField(source='roles.all')
    roles=serializers.SerializerMethodField()
    def get_roles(self,row):
        roles_obj=row.roles.all()
        ret=[]
        for item in roles_obj:
            ret.append({'id':item.id,'title':item.title})
        return ret