from django.urls import path
from companyWeb import views


app_name = 'companyWeb'
urlpatterns = [
    path('',views.companyWeb,name = 'companyWeb'),
]