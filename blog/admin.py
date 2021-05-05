from django.contrib import admin

from .models import Blog, Author, Entry, Course, Student

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Course)
admin.site.register(Student)
