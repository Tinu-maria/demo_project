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
import asyncio


# API view

class StudentView(APIView):
    """
    Student view
    In GET: Obtain list of all students profile
    In POST: Creates a new student profile
    """
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)

        # age1 = Student.objects.annotate(new_age=F('age') + 1)
        # for age in age1:
        #     print(age.new_age)
        # age2 = Student.objects.aggregate(new_age=Avg(F('age')))
        # print(age2['new_age'])
        # data1 = Student.objects.filter(Q(id=27))
        # print(data1)
        # data2 = Student.objects.raw("SELECT * from Student")
        # print(data2)

        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            Student.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)


class StudentDetailView(APIView):
    """
    Student detail view
    In GET: Obtains a student profile with corresponding id
    In PUT: Updates a student profile with corresponding id
    In DELETE: Deletes a student profile with corresponding id
    """
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        queryset = Student.objects.get(id=id)
        serializer = StudentSerializer(queryset)
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

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        queryset = Student.objects.get(id=id)
        queryset.delete()
        return Response({"msg": "deleted"})


# Model view set view

class UserRegistrationView(ModelViewSet):
    """
    User registration view
    Can Create & List a user profile
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserProfileView(ModelViewSet):
    """
    User profile view
    Can Create, List, Get, Update & Delete a user profile
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Generic view

class GenericProfileView(ListCreateAPIView):
    """
    Generic profile view
    Can Create & List a user profile
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class GenericView(RetrieveUpdateDestroyAPIView):
    """
    Generic view
    Can Get, Update & Delete a user profile
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_url_kwarg = 'id'


class ProfileListView(APIView):  # created to do faker factories
    def get(self, request, *args, **kwargs):
        profile = UserProfile.objects.all()
        serializer = UserProfileSerializer(profile, many=True)
        return Response(data=serializer.data)


class StudentListView(APIView):  # created to do faker factories
    def get(self, request, *args, **kwargs):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(data=serializer.data)


async def student(i):
    print(f"student {i} entered")
    await asyncio.sleep(4)
    print(f"student {i} completed")


async def main():
    student1 = asyncio.create_task(student(1))
    await asyncio.sleep(1)
    student2 = asyncio.create_task(student(2))
    await asyncio.sleep(1)
    student3 = asyncio.create_task(student(3))
    await student1
    await student2
    await student3
# asyncio.run(main())
