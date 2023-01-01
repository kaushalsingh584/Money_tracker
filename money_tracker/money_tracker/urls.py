"""money_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views
from transaction import views as views_trans

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegisterView.as_view(),name = "register") ,
    path('login/',views.LoginView.as_view() ,name = "login") ,
    path('trans/',views_trans.trans.as_view() ,name = "trans") ,
    path('get_users/',views.info.as_view() ,name = "get_users"),
    path('group_list/',views_trans.groups_list.as_view() ,name = "group_list"),
    path('lend/',views_trans.lended.as_view() ,name = "lend"),
    path('borrowed/',views_trans.borrowed.as_view() ,name = "borrow")
]
