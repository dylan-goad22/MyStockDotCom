
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('portfolio/', views.portfoliopage, name='portfolio'),
    path('stocks/', views.stockpage, name='stocks'),
    path('invest/', views.investment, name='invest-page'),
    
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
]
