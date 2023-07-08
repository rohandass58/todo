from django.contrib import admin

# Register your models here.
from todoapi.models import User, Task


admin.site.register(User)
admin.site.register(Task)
