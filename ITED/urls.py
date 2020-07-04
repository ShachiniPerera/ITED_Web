from django.urls import path
from.import views
urlpatterns = [
    path('', views.home,name = 'ITED_home'),
    # path('index/', views.index, name='ITED_index'),
    path('index/', views.index_page, name='index_page'),
    path('about/', views.about_page, name='about_page'),
    path('gallery/', views.gallery_page, name='gallery_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('services1/', views.services1_page, name='services1_page'),
    path('services2/', views.services2_page, name='services2_page'),
    path('services3/', views.services3_page, name='services3_page'),
    path('services/', views.services_page, name='services_page'),
    path('services4/', views.services4_page, name='services4_page'),
    path('services5/', views.services5_page, name='services5_page'),
    path('services6/', views.services6_page, name='services6_page'),
    path('services7/', views.services7_page, name='services7_page'),
    path('services8/', views.services8_page, name='services8_page'),
    path('services9/', views.services9_page, name='services9_page'),
    path('products1/', views.products1_page, name='products1_page'),
    path('products2/', views.products2_page, name='products2_page'),
    path('products3/', views.products3_page, name='products3_page'),
    path('disclaimer/', views.disclaimer_page, name='disclaimer_page'),
    path('careers/', views.careers_page, name='careers_page'),
    path('test/', views.test_page, name='test_page'),
    path('test1/', views.test1_page, name='test1_page'),
    path('index2/', views.index2_page, name='index2_page'),
    path('index3/', views.index3_page, name='index3_page'),
    path('pop/', views.pop_page, name='pop_page'),
    path('newpop/', views.newpop_page, name='newpop_page'),

    # path('base1/', views.index, name='ITED_base1'),
    # path('about/', views.about,name = 'ITED_about'),
    # path('contact/', views.contact_page, name='contact_page'),  # render index.html
    # path('about/', views.about_page, name='about_page'),
    # path('contact/', views.contact_page, name='contact_page'),
]

