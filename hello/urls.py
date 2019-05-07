from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='indexs'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('find/', views.find, name='find'),
    path('find/<int:num>', views.find, name='find'),
    path('check', views.check, name='check'),
    
    path('message/', views.message, name='message'),
    path('message/<int:page>', views.message, name='message') ,
    path('msgedit/<int:num>', views.msgedit, name='msgedit'),
    path('msgdelete/<int:num>', views.msgdelete, name='msgdelete'),

]
