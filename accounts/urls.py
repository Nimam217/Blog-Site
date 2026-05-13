from django.urls import path
from .views import login_view,logout_view,signup_view,change_password
app_name = 'accounts'

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('signup/',signup_view,name='signup'),
    path('change-password',change_password,name='change_password')
    
    
]
