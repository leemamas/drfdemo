# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/16  18:14

from rest_framework import serializers

class RoleSerializer(serializers.Serializer):
    title = serializers.CharField()

