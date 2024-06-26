from django.contrib import admin
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls")),
    path('register/', v.register, name="register")
]
