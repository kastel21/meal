from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    # path('brti_vl_eid_weekly_statistics_tool_may_week_4/specimens_run.html', views.prof, name='prof'),
]