from django.urls import path
from . import views
from register import views as v

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.index, name="index"),
    path("create/", views.create, name="create"),
    path('register/', v.register, name="register")
]