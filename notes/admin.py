from django.contrib import admin
from .models import Note
# Register your models here.
admin.site.register(Note)
# This code registers the Note model with the Django admin site, allowing it to be managed through
# the admin interface. The Note model is defined in notes/models.py and includes fields for title,
# content, created_at, and updated_at. By registering it, you can create, read, update, and delete
