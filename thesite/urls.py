from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^story/', views.the_story, name='the_story'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^database/', views.database, name='database'),
    url(r'^view_product/(?P<pk>\d+)/$', views.view_product, name='view_product'),
    url(r'^modify_product/(?P<pk>\d+)/$', views.modify_product, name='modify_product'),
    url(r'^view_conglomerate/(?P<pk>\d+)/$', views.view_conglomerate, name='view_conglomerate'),
    url(r'^modify_conglomerate/(?P<pk>\d+)/$', views.modify_conglomerate, name='modify_conglomerate'),
    url(r'^submit_verification/(?P<pk>\d+)/$', views.submit_verification, name='submit_verification'),
    url(r'^submit_verification_conglom/(?P<pk>\d+)/$', views.submit_verification_conglom, name='submit_verification_conglom'),

]
