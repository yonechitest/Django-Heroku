from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='indexs'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('createpurpose', views.createpurpose, name='createpurpose'),
    path('editpurpose/<int:num>', views.editpurpose, name='editpurpose'),
    path('deletepurpose/<int:num>', views.deletepurpose, name='deletepurpose'),



    path('check', views.check, name='check'),

    path('top', views.top, name='top'),
    path('top2', views.top2, name='top2'),
    path('devtest', views.devtest, name='devtest'),
    



#######################未使用#############################
    path('find/', views.find, name='find'),
    path('find/<int:num>', views.find, name='find'),
    path('message/', views.message, name='message'),
    path('message/<int:page>', views.message, name='message') ,
    path('msgedit/<int:num>', views.msgedit, name='msgedit'),
    path('msgdelete/<int:num>', views.msgdelete, name='msgdelete'),

]
