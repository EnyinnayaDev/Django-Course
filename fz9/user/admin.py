from django.contrib import admin
from .models import Profile, Author, Book, Student, Course, Article
# Register your models here.
admin.site.register(Profile)
admin.site.register(Author)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('id',)
    list_filter = ('category',)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)