from django.urls import path
from . import views

urlpatterns = [
    path('ubah_data_user/', views.UserEditView.as_view(), name='ubah_data_user'),
    path('signup/', views.UserRegisterView.as_view(), name='register'),
    path('password/', views.PasswordChangeView.as_view(), name='ubah_password'),   
]