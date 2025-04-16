from django.urls import path
from django.contrib import admin
from . import views



app_name = 'tomb'
urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game_view, name='GameView'),
    path("admin/", admin.site.urls),
]