from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','email', 'subject', 'create_date')
    list_display_link = ('id', 'first_name', 'email', 'subject')
    search_fields = ('first_name', 'email')
    list_per_page=25


admin.site.register(Contact, ContactAdmin)
