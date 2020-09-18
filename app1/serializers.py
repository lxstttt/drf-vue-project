from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions

from app1.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {
            "username": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            }
        }

    def validate_username(self, attrs):
        user = User.objects.filter(username=attrs).first()

        if user:
            raise exceptions.ValidationError("用户名已存在")

        return attrs


class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        extra_kwargs = {
            "emp_name": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            }
        }
