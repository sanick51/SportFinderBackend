from UseApp import views

from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path

urlpatterns=[
    re_path(r'^user$',views.userApi),
    re_path(r'^user/([0-9]+)$',views.userApi),

    re_path(r'^login$',views.loginApi),
    re_path(r'^login/([0-9]+)$',views.loginApi),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)