from django.urls import path

from . import views

urlpatterns = [
    path('exp', views.exp, name='exp'),
    path('', views.profile, name='profile'),
    path('profilecovid', views.profilecovid, name='profilecovid'),
    path('profilecovid19', views.profilecovid19, name='profilecovid19'),
    path('profilecovid19t', views.profilecovid19t, name='profilecovid19t'),
    path('profilecovid19to', views.profilecovid19to, name='profilecovid19to'),
    path('vleid',views.vleid, name='vleid'),
    path('vleid2',views.vleid2, name='vleid2'),
    path('vleid3',views.vleid3, name='vleid3'),
    path('labcovidweekly', views.labcovidweekly, name='labcovidweekly'),
    path('labcovidweekly2', views.labcovidweekly2, name='labcovidweekly2'),
    path('labcovidweekly3', views.labcovidweekly3, name='labcovidweekly3'),
    path('labcovidweekly4', views.labcovidweekly4, name='labcovidweekly4'),
    path('labcovidweekly5', views.labcovidweekly5, name='labcovidweekly5'),
    path('labeidweekly', views.labeidweekly, name='labeidweekly'),
    path('labeidweekly2', views.labeidweekly2, name='labeidweekly2'),
    path('labeidweekly3', views.labeidweekly3, name='labeidweekly3'),
    path('labeidweekly4', views.labeidweekly4, name='labeidweekly4'),
    path('labbrtiweekly', views.labbrtiweekly, name='labbrtiweekly'),
    path('labbrtiweekly2', views.labbrtiweekly2, name='labbrtiweekly2'),
    path('labbrtiweekly3', views.labbrtiweekly3, name='labbrtiweekly3'),
    path('labbrtiweekly4', views.labbrtiweekly4, name='labbrtiweekly4'),
    path('labbrtiweekly5', views.labbrtiweekly5, name='labbrtiweekly5'),
    path('labcov19weekly5', views.labcov19weekly5, name='labcov19weekly5'),
    path('export_csv', views.export_csv, name='export-csv'),

]