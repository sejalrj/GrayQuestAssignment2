from django.urls import path
from . import views

urlpatterns = [
path('login/', views.login_page, name='login'),
path('postlogin/', views.postlogin, name='postlogin'),
path('postlogin/memepage/', views.memepage, name='memepage'),
path('set-csrf/', views.set_csrf_token, name='Set-CSRF')

]