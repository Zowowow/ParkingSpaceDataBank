
from django.urls import path
from . import views
from django.contrib import admin

#Django Admin Customize
admin.site.site_header = "Vehicular Data Bank Admin"
admin.site.site_title = "Vehicular Data Bank Admin Portal"
admin.site.index_title = "Welcome to Vehicular Data Bank Admin Portal"

urlpatterns = [
    path('login_user', views.login_user, name="login_user"),
    path('', views.logout_user, name="logout_user"),
    # path('dashboard', views.dashboard, name="dashboard"),
    path('index', views.index, name="index"),
    path('signup', views.signup_user, name="signup"),
    path('view_car', views.view_car, name="view_car"),
    path('add_car', views.add_car, name="add_car"),
    path('update_car/<car_id>', views.update_car, name="update_car"),
    path('delete_car/<car_id>', views.delete_car, name="delete_car"),



    # path for video camera
    path('video_feed', views.video_feed, name='video_feed')

    
]