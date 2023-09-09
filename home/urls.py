from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.success_page, name='success_page'),
    path('failed', views.failed_page, name='failed_page'),
    path('address', views.address_page, name='address_page'),
    path('ospf', views.ospf_page, name='ospf_page'),
    path('l3vpn', views.l3vpn_page, name='l3vpn_page'),
]