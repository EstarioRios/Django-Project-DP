"""
URL configuration for DP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from LoginSystem.views import view_login_signin_page as VLSP
from Home.views import view_home_page as VHP
from Dashboard.views import view_dashboard as VD, upgrade_to_seller as UTS

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", VHP, name="home"),
    path("login/", VLSP, name="login_signup"),
    path("dashboard/", VD, name="dashboard"),
    path("to-seller/", UTS, name="upgrade_to_seller"),
]
