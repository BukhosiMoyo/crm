from django.urls import path

from django.contrib.auth import views as auth_views

from . import views 



urlpatterns = [

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'), 
    path('user/', views.userPage, name='userpage'),
    path('account/', views.accountSettings, name='settings'),

    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),

    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    path('error/', views.errorNotAllowed, name='error1'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



    ]

    