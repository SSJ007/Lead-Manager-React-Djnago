from django.contrib import admin
from django.urls import path, re_path
from leads import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/leads/$', views.leads_list),
    re_path(r'^api/leads/([0-9])$', views.leads_detail),
]
