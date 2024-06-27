from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.applogin, name='login'),
    path('logout/', views.indexlogout, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),


    path('', views.index, name='index'),
    path('package/', views.package, name='package'),
    path('package-details/<int:pk>', views.packagedetails, name='packagedetails'),
    path('blog-details/<int:pk>/', views.blogdetails, name='blogdetails'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
]