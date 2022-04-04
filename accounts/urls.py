from django.urls import path

from accounts.views import login_view,SignupView
app_name = 'accountsss'
urlpatterns = [ 
    path('login',login_view,name="login"),
    path('signup',SignupView.as_view(),name="signup")
]
