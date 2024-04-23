from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from blog.views import SignUpView, ProfileView, EmailChangeView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/email_change/', EmailChangeView.as_view(), name='email_change'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include('blog.urls')),
]