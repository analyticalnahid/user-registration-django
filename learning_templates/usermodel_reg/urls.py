
from django.contrib import admin
from django.urls import path, include
from usermodel_reg_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('usermodel_reg_app/', include('usermodel_reg_app.urls'), name='usermodel_reg_app')
]
