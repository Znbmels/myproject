from rest_framework import serializers
from app.models import Lesson, Homework, ErrorLog, User, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'name']

class HomeworkSerializer(serializers.ModelSerializer):
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