 
from django.urls import path

from accounts.views import *
app_name="blow"
urlpatterns = [ 
    path('signup',SignupView.as_view(),name="signup"),
    path('dashboard',DashboardView.as_view(),name="dashboard"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
]
