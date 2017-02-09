from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^story/', views.the_story, name='the_story'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^database/', views.database, name='database'),
    url(r'^modify_product/(?P<pk>\d+)/$', views.modify_product, name='modify_product'),

]
