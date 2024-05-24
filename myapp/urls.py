from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.service_list, name='services'),
    path('services/details/', views.service_detail, name='services_details'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('team/', views.team_list, name='team'),
    path('team/details/', views.team_detail, name='team_details'),
    path('blog/', views.blog_list, name='blog'),
    path('blog-details/', views.blog_detail, name='blog_details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('table/', views.pricing, name='pricing_table'),
    path('search/', views.search, name='search'),  # Add this line

]
