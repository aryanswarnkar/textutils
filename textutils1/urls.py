"""
URL configuration for textutils1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Project: TextUtils1
Description: A simple text analysis web application
"""

from django.contrib import admin
from django.urls import path, include
from . import views

# Main URL patterns
urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Home page
    path('', views.index, name='index'),

    # Text analysis endpoint
    path('analyze/', views.analyze, name='analyze'),  # Added trailing slash for consistency

    # Optional: Add a redirect for analyze without slash
    path('analyze', views.analyze, name='analyze_redirect'),
]

# Custom 404 and 500 handlers (optional)
handler404 = 'textutils1.views.error_404'
handler500 = 'textutils1.views.error_500'

# Optional: If you plan to add more apps later
# from django.urls import include
# urlpatterns += [
#     path('api/', include('api.urls')),
# ]