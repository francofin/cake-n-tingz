from django.contrib import admin
from .models import Lifestyle, LifestyleComment, LifestyleDashboard
# Register your models here.

class LifestyleCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','email', 'create_date', 'website')
    list_display_link = ('id', 'first_name', 'email')
    search_fields = ('first_name', 'email')
    list_per_page=25

class LifestyleAdmin(admin.ModelAdmin):
    list_display = ('lifestyle_title', 'is_travel', 'is_workout', 'is_health', 'is_new_for_blog', 'is_for_women', 'is_for_family', 'is_for_men')
    list_display_link = ('lifestyle_title')
    search_fields = ['lifestyle_title']
    list_per_page=25

admin.site.register(Lifestyle, LifestyleAdmin)
admin.site.register(LifestyleComment, LifestyleCommentAdmin)
admin.site.register(LifestyleDashboard)
