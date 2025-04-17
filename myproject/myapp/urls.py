from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # сторінки на які можна буде перейти з головних
    path('about/', views.about, name='about'),
    path('log_in/', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('instruction/', views.instruction, name='instruction'),







    # сторінки для благодійника







    #сторінки для користувача
]
