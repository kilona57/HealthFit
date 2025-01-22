from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainPageView.as_view(), name ='main_page'),
    path('registration/', views.RegistrationView.as_view(), name ='registration'),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.user_logout, name ='logout'),
    path('main_page_for_logout_user/', views.main_page_for_logout_user, name ='main_page_for_logout_user'),
    path('password-change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('userinfo/', views.AddBodyParams.as_view(), name='userinfo'),

    path('profile/', views.profile_view, name='profile'),
    path('add_body_params/', views.add_body_params, name='add_body_params')
   ]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)