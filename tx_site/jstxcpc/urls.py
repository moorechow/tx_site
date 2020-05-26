'''
 * @Author: Moore.zhou 
 * @Date: 2020-05-26 10:20:54 
 * @Last Modified by:   Moore.zhou 
 * @Last Modified time: 2020-05-26 10:20:54 
'''
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.tx_home,name="tx_home"),
]

