from django.urls import path, re_path
from requests.api import get
from core import views

urlpatterns = [
    re_path(r'^locations/(?P<city>\w+)/$',
            views.get_tempertaure, name='get_default_data'),
    re_path(r'^locations/(?P<city>\w+)/((?P<days>\d+)?)/$',
            views.get_tempertaure, name='get_multiple_days'),
    re_path(r'^home/', views.home)
]
