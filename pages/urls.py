from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('exp', views.exp, name='exp'),
    path('home', views.home, name='home'),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.loly_login, name='loly_login'),
    # path('', TemplateView.as_view(template_name='masving_brti_vl_weekly_statistics_tool_31-6_june_2021/top.html'), name='home'),
    # path('profilecovid', views.profilecovid, name='profilecovid'),
    # path('profilecovid19', views.profilecovid19, name='profilecovid19'),
    # path('profilecovid19t', views.profilecovid19t, name='profilecovid19t'),
    # path('profilecovid19to', views.profilecovid19to, name='profilecovid19to'),
    # path('vleid',views.vleid, name='vleid'),
    # path('vleid2',views.vleid2, name='vleid2'),
    # path('vleid3',views.vleid3, name='vleid3'),

    #lab covid 19
    path('labcov19run', views.labcov19run, name='labcov19run'),
    path('labcov19recieved', views.labcov19recieved, name='labcov19recieved'),
    path('labcov19general', views.labcov19general, name='labcov19general'),
    path('labcov19machine', views.labcov19machine, name='labcov19machine'),

    #lab eid
    path('labeidelectric', views.labeidelectric, name='labeidelectric'),
    path('labeidfailure', views.labeidfailure, name='labeidfailure'),
    path('labeidrecieved', views.labeidrecieved, name='labeidrecieved'),
    path('labeidrun', views.labeidrun, name='labeidrun'),
    path('labeidtop', views.labeidtop, name='labeidtop'),

    #lab vl
    path('labvltop', views.labvltop, name='labvltop'),
    path('labvlrun', views.labvlrun, name='labvlrun'),
    path('labvlrecieved', views.labvlrecieved, name='labvlrecieved'),
    path('labvlfailure', views.labvlfailure, name='labvlfailure'),
    path('labvlelectric', views.labvlelectric, name='labvlelectric'),


    path('export_csv', views.export_csv, name='export-csv'),

]