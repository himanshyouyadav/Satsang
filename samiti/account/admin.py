from django.contrib import admin

# Register your models here.

from account.models import Profile
from dashboard.models import Member

admin.site.register(Profile)
admin.site.register(Member)

