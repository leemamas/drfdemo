# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/21  4:40
from rest_framework import serializers
from example import models
from rest_framework.validators import ValidationError


class PublishSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        models.PublishModel.objects.create(**validated_data)
        return "xxxx"

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.address = validated_data.get('address')
        instance.save()
        return 'yyyyy'


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookModel
        # 设置所有字段
        fields = ('name', 'price', 'publish', 'authors')
        # extra_kwargs划分只序列化或只反序列化字段
        extra_kwargs = {
            'name': {
                'required': True,
                'min_length': 1,
                'error_messages': {'required': '必填项', 'min_length': '太短', },
            },
            'publish': {'write_only': True},
            'authors': {'write_only': True},
        }
