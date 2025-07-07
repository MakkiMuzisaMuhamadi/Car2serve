from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.aboutus, name='aboutus'),
    path('book/<str:service_name>/', views.booking_page, name='booking_page'),
    path('cars', views.cars, name='cars'),
    path('detail/<int:car_id>/', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('fuel', views.fuel, name='fuel'),
    path('track', views.track, name='track'),
    path('status', views.trackStatus, name='trackStatus'),
    path('shipping', views.shipping, name='shipping'),
    path('success_shipping/<str:customer_name>/<str:phone_number>/<str:email>/', views.success_shipping, name='success_shipping'),
    path('success/<str:car_name>/<str:car_model>/', views.success_page, name='success_page'),
]