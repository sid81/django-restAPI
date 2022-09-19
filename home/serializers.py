

from rest_framework import serializers
from .models import Task
from .models import *
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        
    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['paasword'])
        return user