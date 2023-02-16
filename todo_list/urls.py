from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('cross_off/<int:id>', views.cross_off, name='cross_off'),
    path('uncross/<int:id>', views.uncross, name='uncross'),
]
