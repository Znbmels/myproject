from rest_framework import serializers
from django.contrib.auth import get_user_model
from app.models import Lesson, Homework, ErrorLog, Student  # User импортируем через get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data.get('role', 'student')
        )
        return user

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'name']

class HomeworkSerializer(serializers.ModelSerializer):
    tasks = serializers.ListField(
        child=serializers.CharField(max_length=255),  # Каждый элемент массива — строка
        allow_empty=False  # Не разрешать пустые массивы
    )

    class Meta:
        model = Homework
        fields = ['id', 'lesson', 'day', 'topic', 'tasks']

class ErrorLogSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role="student")  # Только пользователи с ролью "student"
    )

    class Meta:
        model = ErrorLog
        fields = ['id', 'student', 'lesson', 'description']


class LessonSerializer(serializers.ModelSerializer):
    homeworks = serializers.SerializerMethodField()
    errors = ErrorLogSerializer(many=True, read_only=True, source='errorlog_set')

    class Meta:
        model = Lesson
        fields = [
            'id', 'day_of_week', 'start_time', 'end_time', 'zoom_link',
            'students', 'homeworks', 'errors'
        ]

    def get_homeworks(self, obj):
        return HomeworkSerializer(obj.homework_set.all(), many=True).data