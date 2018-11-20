from django.urls import path
from personalWeb import views


app_name = 'personalWeb'
urlpatterns = [
    path('',views.personalWeb,name = 'personalWeb'),
]