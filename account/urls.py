from django.urls import path
from .import views


urlpatterns = [
    
    path('register/', views.register, name="register"),
    path('login/', views.customerlogin, name="customerlogin"),
    path('logout/', views.logout_view, name="logout"),
    path('lupa_password/', views.lupa_password, name="lupa_password"),
    path('change_password/<token>', views.change_password, name="change_password"),
    path('profile_saya', views.profile_saya, name="profile_saya"),

]