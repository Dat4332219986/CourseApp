from django.contrib import admin
from courses.models import Courses, Category


class MyCourseAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Category)
admin.site.register(Courses, MyCourseAdmin)
