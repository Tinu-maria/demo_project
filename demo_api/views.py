from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import UserSerializer, UserProfileSerializer, StudentSerializer
from django.contrib.auth.models import User
from .models import UserProfile, Student
from rest_framework import permissions
from rest_framework import status
from django.db.models import F, Q, Avg
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# API view

class StudentView(APIView):
    def get(self,request,*args,**kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)

        age1 = Student.objects.annotate(new_age = F('age')+1)
        for age in age1:
            print(age.new_age)
        age2 = Student.objects.aggregate(new_age = Avg(F('age')))
        print(age2['new_age'])
        data1 = Student.objects.filter(Q(id=27))
        print(data1)
        # data2 = Student.objects.raw("SELECT * from Student")
        # print(data2)

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


# Model view set view

class UserRegistrationView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
   
class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data, context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

# Generic view

class GenericProfileView(ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data, context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class GenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_url_kwarg = 'id'


class ProfileListView(APIView):
    def get(self,request,*args,**kwargs):
        profile = UserProfile.objects.all()
        serializer = UserProfileSerializer(profile, many=True)
        return Response(data=serializer.data)

class StudentListView(APIView):
    def get(self,request,*args,**kwargs):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(data=serializer.data)