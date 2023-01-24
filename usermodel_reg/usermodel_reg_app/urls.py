from django.urls import path
from usermodel_reg_app import views

#TEMPLATE URLS!
app_name = 'usermodel_reg_app'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register')
] 
 