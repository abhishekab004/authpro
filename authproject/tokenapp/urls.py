from django.urls import path,include 
from tokenapp import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api',views.EmployeeCRUDCBV)

urlpatterns = [
    path('', include(router.urls)),

]   
     