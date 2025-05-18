from django.urls import path
from employeapp import views

urlpatterns = [
    path('',views.registrationview,name='register'),
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logoutview'),
    path('employelist/',views.employelist,name='employeelist'),
    path('companylist/',views.companylist,name='companylist'),
    path('companyadd/',views.companyadd,name='company-add'),
    path('employeadd/',views.employeadd,name='employe-add'),
    path('empyoeupdate/<int:pk>/',views.employeupdate,name='employeupdate'),
    path('companyupdate/<int:pk>/',views.companyupdate,name='companyupdate'),
]
