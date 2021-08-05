from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profilecovid', views.profilecovid, name='profilecovid'),
    path('profilecovid19', views.profilecovid19, name='profilecovid19'),
    path('profilecovid19t', views.profilecovid19t, name='profilecovid19t'),
    path('profilecovid19to', views.profilecovid19to, name='profilecovid19to')
]