from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin
# Create your views here.
from rest_framework.views import APIView

from app1.models import User, Employee
from app1.serializers import UserModelSerializer, EmployeeModelSerializer
from utils.response import APIResponse


class UserAPIView(APIView):

    # 处理用户注册
    def post(self,request,*args,**kwargs):

        data = request.data
        serializer = UserModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        save = serializer.save()
        return APIResponse(200, True, results=UserModelSerializer(save).data)

    # 处理用户登录
    def get(self,request,*args,**kwargs):

        username = request.query_params.get('username')
        pwd = request.query_params.get('pwd')
        print(username,pwd)

        user_obj = User.objects.filter(username=username, password=pwd).first()
        if user_obj:
            data = UserModelSerializer(user_obj).data
            return APIResponse(200, True, results=data)

        return APIResponse(400, False)

class EmployeeGenericAPIView(ListModelMixin, CreateModelMixin, GenericAPIView,DestroyModelMixin,UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

    lookup_field = id

    # 处理获取所有员工请求
    def get(self,request,*args,**kwargs):
        response = self.list(request,*args,**kwargs)
        return APIResponse(200, True, results=response.data)

    # 处理员工添加请求
    def post(self,request,*args,**kwargs):
        print(request.data)
        response = self.create(request,*args,**kwargs)
        return APIResponse(200, True, results=response.data)

    # 处理删除员工请求
    def delete(self,request,*args,**kwargs):
        id = request.data.get('id')
        print(id)
        # lookup_field = id
        response = self.destroy(request, *args, **kwargs)
        return APIResponse(200, True, results=response.data)


    def patch(self,request,*args,**kwargs):
        response = self.update(request, *args, **kwargs)
        return APIResponse(results=response.data)