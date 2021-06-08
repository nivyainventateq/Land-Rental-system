from django.contrib import admin
from testapp.models import User,Soiltypes,Property,Roles,Watersources

admin.site.register(User,Soiltypes,Property,Roles,Watersources)
