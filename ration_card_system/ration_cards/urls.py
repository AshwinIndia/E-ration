from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply_for_card, name='apply_for_card'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('ration-card/<int:pk>/', views.ration_card_detail, name='ration_card_detail'),
    path('ration-card/<int:ration_card_pk>/add-family-member/', views.add_family_member, name='add_family_member'),
    path('check-status/', views.check_status, name='check_status'),
    path('distribution-history/', views.distribution_history, name='distribution_history'),
    path('file-complaint/', views.file_complaint, name='file_complaint'),
    path('complaints/', views.complaint_list, name='complaint_list'),
]