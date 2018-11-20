from django.urls import path
from networkShop import views


app_name = 'networkShop'
urlpatterns = [
    path('',views.networkShop,name = 'networkShop'),
]