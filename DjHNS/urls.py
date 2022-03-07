"""DjHNS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from users import views as user_view
from django.contrib.auth import views as auth_views
from .views import home_page, stock_management

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home'),
    path('stock_management/', stock_management, name='stock-management'),
    path('register/', user_view.register, name='user-register'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    path('vaccine/', include(('vaccine.urls', 'vaccine'), namespace= "vaccine")),
    path('bloodbank/', include(('bloodbank.urls', 'bloodbank'), namespace = 'bloodbank')),
    path('users/', include(('users.urls', 'users'), namespace = 'users')),
<<<<<<< HEAD
    path('stocks/', include(('stocks.urls', 'stocks'), namespace = 'stocks')),
=======
    path('stocks/', include('stocks.urls', namespace='stocks')),
>>>>>>> cc211a397fdeca62c41250165c08d2b64aa99404
]
