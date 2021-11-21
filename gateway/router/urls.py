from django.conf.urls import url
from . import views

urlpatterns = [
    url('^internal/v1/gateway/sg/register$', views.sg_register)
]