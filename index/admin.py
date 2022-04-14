from sqlite3 import Cursor
from django.contrib import admin

from .models import Avatar

# Register your models here.

admin.site.register(Avatar)