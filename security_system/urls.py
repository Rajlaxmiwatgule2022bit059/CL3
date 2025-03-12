from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('visitors/', views.visitor_list, name='visitors'),
    path('incident/', views.incident_list, name='incident'),
]
