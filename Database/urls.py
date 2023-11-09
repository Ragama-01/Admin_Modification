from django.urls import path

from Database import views

app_name="Database"

urlpatterns = [
    path('',views.home, name='Home'),
    path('form',views.form, name='Form'),
    path('data',views.data, name='Data'),
    path('delete/<id>',views.delete, name="delete"),
    path('insert',views.insertdata, name="insertadata"),
    path('edit/<id>',views.edit,name="edit"),
    path('sliders',views.sliders,name="sliders"),
    path('search/',views.search, name="search"),
    path('register/',views.SignUpview.as_view(), name="register"),
    path('login/',views.UserLogin.as_view(),name="login")
    
]