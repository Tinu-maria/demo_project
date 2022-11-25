from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from .serializers import UserSerializer, UserProfileSerializer, StudentSerializer
from django.contrib.auth.models import User
from .models import UserProfile, Student
from rest_framework import permissions
from rest_framework import status

# Create your views here.

class UserRegistrationView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    
class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data, context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
class StudentView(APIView):
    def get(self,request,*args,**kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            Student.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)
 
        
class StudentDetailView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        queryset = Student.objects.get(id=id)
        serializer=StudentSerializer(queryset)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        queryset = Student.objects.get(id=id)
        serializer = StudentSerializer(data=request.data, instance=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        queryset = Student.objects.get(id=id)
        queryset.delete()
        return Response({"msg":"deleted"})

        
        

