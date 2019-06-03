"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from dashboard.views import DahsboardView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('dashboard/', login_required(DahsboardView.as_view()),name='dashboard-view'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/change-password/', PasswordChangeView.as_view(success_url='/accounts/change-password/done/'), name='change-password'),
    path('accounts/change-password/done/', PasswordChangeDoneView.as_view(), name='change-password-done'),
]
