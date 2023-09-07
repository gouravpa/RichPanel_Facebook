
from django.urls import path
from . import views

urlpatterns = [
    path('Signup/',views.Register,name="signup"),
    path('',views.Home,name="home"),
    path('contactus/',views.Contactus,name="contactus"),
    path('login/',views.Login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.logout,name="logout"),
    path('aboutus/',views.Aboutus,name="about")
    
    
]
