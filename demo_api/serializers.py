from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        return UserProfile.objects.create(user=user,**validated_data)
    

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    class Meta:
        model = Student
        fields = "__all__"
