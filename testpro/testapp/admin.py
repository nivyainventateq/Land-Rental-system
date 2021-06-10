from django.contrib import admin
from testapp.models import User,Soiltypes,Property,Roles,Watersources

admin.site.register(User)
admin.site.register(Soiltypes)
admin.site.register(Roles)
admin.site.register(Watersources)
admin.site.register(Property)
