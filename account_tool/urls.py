from django.urls import path, include

from . import views
from account_tool.views import MainView, SecureView, InputFormView, UpdateRecordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('secure/', SecureView.as_view(), name='secure'),
    path('create_new/', InputFormView.as_view(), name='input_form'),
    path('update/', UpdateRecordView.as_view(), name='update_rec'),
    path('login/', auth_views.LoginView.as_view(template_name='account_tool/login.html'), 
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main'), name='logout'),
    path('', include('django.contrib.auth.urls')),
]
