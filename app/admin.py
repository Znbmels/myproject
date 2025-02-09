from django.contrib import admin
from app.models import User, Teacher, Student, Lesson, Homework, ErrorLog

# Регистрация модели User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('username', 'email')

# Регистрация модели Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')

# Регистрация модели Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')

# Регистрация модели Lesson
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'start_time', 'end_time', 'teacher', 'zoom_link')
    list_filter = ('day_of_week', 'teacher')
    search_fields = ('teacher__name', 'zoom_link')

# Регистрация модели Homework
@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'day', 'topic')
    list_filter = ('lesson', 'day')
    search_fields = ('topic',)

# Регистрация модели ErrorLog
@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'description')
    list_filter = ('student', 'lesson')
    search_fields = ('description',)