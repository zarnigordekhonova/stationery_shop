from django.urls import path
from Customers.views import RegisterView, LoginView, LogoutView, ProfileView, ProfileUpdateView


app_name = 'customers'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(), name='edit-profile')
]