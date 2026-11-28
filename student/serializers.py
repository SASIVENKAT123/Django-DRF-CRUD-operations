from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student,Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','subject']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']
class StudentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only =True)
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        required=False,
        allow_null = True,
        write_only = True
    )
    teacher_details = TeacherSerializer(
        source ='teacher',
        read_only = True
    )
    class Meta:
        model=Student
        fields='__all__'
        read_only_fields =['id']

    def  validate_age(self,value):
        if value<18:
            raise serializers.ValidationError(
                "Student age must be above 18"
            )
        return value

    def validate(self, data):
        name = data.get('name')
        course = data.get('course')

        if name is not None and course is not None:
            if name ==course:
                raise serializers.ValidationError(
                    "Studnet and course cannot be same"
                )
        return data
