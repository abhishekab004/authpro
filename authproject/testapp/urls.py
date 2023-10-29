
from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.homepage_view),
    path('python/', views.python_view),
    path('java/', views.java_view),
    path('c/', views.c_view),
    path('ruby/', views.ruby_view),
    path('contact/', views.contact_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    
]