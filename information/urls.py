from django.conf.urls import url
from . import views

app_name = 'information'
urlpatterns = [
    url(r'keyboard$', views.keyboard, name='keyboard'),
    url(r'message$', views.message, name='message'),
]