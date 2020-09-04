from django.contrib import admin
from .models import Food, Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','email', 'create_date', 'website')
    list_display_link = ('id', 'first_name', 'email')
    search_fields = ('first_name', 'email')
    list_per_page=25


admin.site.register(Food)
admin.site.register(Comment, CommentAdmin)
