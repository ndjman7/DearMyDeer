from django.conf.urls import url
from . import views

app_name = 'information'
urlpatterns = [
    url(r'keyboard$', views.test, name='test'),
    url(r'message$', views.test2, name='test2'),
]