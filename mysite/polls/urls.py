from django.urls import  path
from . import views

urlpatterns = [
  path('', views.index, name='index' ), #name enables its reference from anywhere in Django, which is effective in template.
]
