from django.contrib import admin
from .models import Food, Comment, Dashboard

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','email', 'create_date', 'website')
    list_display_link = ('id', 'first_name', 'email')
    search_fields = ('first_name', 'email')
    list_per_page=25

class FoodAdmin(admin.ModelAdmin):
    list_display = ('recipe_title', 'is_for_slider', 'is_for_home_page', 'is_holiday_recipe', 'is_featured_for_home_page', 'is_for_kids', 'is_dessert', 'is_dinner')
    list_display_link = ('recipe_title')
    search_fields = ['recipe_title']
    list_per_page=25

admin.site.register(Food, FoodAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Dashboard)
