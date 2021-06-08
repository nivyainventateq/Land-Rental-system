

from django.urls import path
from .views import register,register1

urlpatterns = [
    path('reginfo/', view=register,name='register'),
    path('reginfo1/<int:id>/', view=register1,name='register1'),
]
