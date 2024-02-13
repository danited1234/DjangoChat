from django.urls import path
from .import views

urlpatterns= [
    path('',views.front_page,name='frontpage'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('logout/',views.logout_view,name='logout_view'),
]