from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.conf.urls import url
from .import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'), 
    path('customer/', views.CustomerList.as_view(), name='customer-list'),
    path('customer/<int:pk>/',  views.CustomerDetail.as_view(), name='customer-detail'),
    path('customer/<int:pk>/highlight/', views.CustomerHighlight.as_view(), name='customer-highlight'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#app_name = 'accounts_api'

#urlpatterns = [
#    path('users/', views.UserList.as_view(), name='user-list'),
#    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'), 
#    path('customer/', views.CustomerList.as_view(), name='customer-list'),
#    path('customer/<int:pk>/',  views.CustomerDetail.as_view(), name='customer-detail'),
 #   path('customer/<int:pk>/highlight/', views.CustomerHighlight.as_view(), name='customer-highlight'),
#    path('', views.api_root),
#]
#urlpatterns = format_suffix_patterns(urlpatterns)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)