

from django.urls import path
from .views import register,register1,details,details1,loginapi,logoutapi

urlpatterns = [
    path('reginfo/', view=register,name='register'),
    path('reginfo1/<int:id>/', view=register1,name='register1'),
    path('propinfo/',view=details,name='details'),
    path('propinfo/<int:id>/',view=details1,name='details1'),
    path('login/',view=loginapi,name='loginapi'),
    path('logout/',view=logoutapi,name='logoutapi'),
]
