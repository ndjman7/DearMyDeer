from django.conf.urls import url
from . import views

app_name = 'information'
urlpatterns = [
    url(r'keyboard$', views.keyboard, name='test'),
    url(r'message$', views.message, name='test2'),
]