from django.contrib import admin

# Register your models here.
from auth_app2.models import AuthUserModel

admin.site.register(AuthUserModel)