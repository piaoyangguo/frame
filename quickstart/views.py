#coding: utf8
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from quickstart.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    查看编辑用户信息
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    查看编辑组的界面
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

