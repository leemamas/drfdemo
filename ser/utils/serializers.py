# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/16  18:14

from rest_framework import serializers
from ser import models

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


def check_user(user):
    if user=='kao':
        raise serializers.ValidationError("用户名不能是禁止文字")
    return user

class UserSerializer2(serializers.Serializer):

    user=serializers.CharField(required=True, min_length=8,validators=[check_user])
    pwd=serializers.CharField(required=True, min_length=8)
    user_type=serializers.IntegerField(default=1)
    group_obj=models.UserGroup.objects.first()
    group=serializers.IntegerField(default=group_obj)



    def validate_user(self, data):
        if (data == "fuck"):
            raise serializers.ValidationError("用户名不能是禁止文字")
        # 验证完成以后务必要返回字段值
        return data

    def validate(self, data):
        user = data.get("user")
        if (user == "fuck"):
            raise serializers.ValidationError("用户名不能是禁止文字")

        pwd = data.get("pwd")
        if (len(pwd) > 64):
            raise serializers.ValidationError("密码过长")

        # 验证完成以后务必要返回data
        return data

    def create(self, validated_data):  # validated_data 参数,在序列化器调用时,会自动传递验证完成以后的数据
        user = models.User.objects.create(
            user=self.validated_data.get("user"),
            pwd=self.validated_data.get("pwd"),
            user_type=self.validated_data.get("user_type"),
            group=self.validated_data.get("group")
        )

        return user

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user")
        instance.pwd = validated_data.get("pwd")
        instance.user_type = validated_data.get("user_type")

        # 调用模型的save更新保存数据
        instance.save()
        return instance

from rest_framework.serializers import ModelSerializer
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields='__all__'
        fields = ['id', 'user', 'pwd','user_type','group','roles']
        # exclude=['user_type']
        depth=1
