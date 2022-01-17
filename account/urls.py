from django.urls import path

from account.views import RegistrationView, activate, LoginView, LogoutView, ChangePasswordView, \
    ForgotPasswordView, ForgotPasswordComlete

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:uid>/<str:token>/', activate, name="activate"),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_complete/', ForgotPasswordComlete.as_view())
]