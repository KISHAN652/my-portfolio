from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)

admin.site.register(Contact, ContactAdmin)

# This code registers the Contact model with the Django admin site.
# It allows you to manage contact messages through the admin interface.
