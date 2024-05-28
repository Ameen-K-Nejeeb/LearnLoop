from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginpage, name= 'login'),
    path('logout/',views.logoutUser, name= 'logout'),
    path('register/',views.registerpage, name= 'register'),
    path('profile/<str:pk>/ ', views.userProfile , name="user-profile"),

    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room, name="room"),

    path('create-Room/',views.createRoom ,name="create-Room"),
    path('update-Room/<str:pk>/ ',views.updateRoom ,name="update-Room"),
    path('delete-Room/<str:pk>/ ',views.deleteRoom ,name="delete-Room"),
    path('delete-message/<str:pk>/ ',views.deleteMessages,name="delete-message"),
    path('update-user/ ',views.updateUser,name="update-user"),

]
"""
added: path of title,html page was divided into different parts,profile were updated,
"""