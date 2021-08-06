from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404, redirect, render



def index(request):
    return HttpResponse("Hello, world. You're at the pages index.")


def home(request):
    context={}

    return render(request, 'base.html', context)

def profile(request):
    context={}
    return render(request, 'brti_covid_19_weekly_statistics_tool/general.html', context)

def profilecovid19to(request):
    context={}
    return render(request, 'brti_covid_19_weekly_statistics_tool/Specimens_Run.html', context)

def profilecovid(request):
    context={}
    return render(request, 'brti_covid_19_weekly_statistics_tool/Specimens_Received.html', context)

def profilecovid19(request):
    context={}
    return render(request, 'brti_covid_19_weekly_statistics_tool/Machine_Downtime_&_Reagent_stock_out_tool.html', context)

def profilecovid19t(request):
    context={}
    return render(request, 'brti_covid_19_weekly_statistics_tool/general.html', context)

def vleid(request):
    context={}
    return render(request, 'brti_vl_eid_weekly_statistics_tool/specimens_run.html', context)

def vleid2(request):
    context={}
    return render(request, 'brti_vl_eid_weekly_statistics_tool/specimens_received.html', context)

def vleid3(request):
    context={}
    return render(request, 'brti_vl_eid_weekly_statistics_tool/reasons_for_failure.html', context)

def labcovidweekly(request):
    context={}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/top.html', context)

def labcovidweekly2(request):
    context={}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/Specimensrun.html', context)

def labcovidweekly3(request):
    context={}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/specimenreceived.html', context)

def labcovidweekly4(request):
    context={}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/Reasonsforfailures.html', context)

def labcovidweekly5(request):
    context={}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/electricoutagestool.html', context)

def labeidweekly(request):
    context={}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/top.html', context)

def labeidweekly2(request):
    context={}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/Specimens_Run.html', context)

def labeidweekly3(request):
    context={}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/Specimens_Received.html', context)

def labeidweekly4(request):
    context={}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/general.html', context)

def labbrtiweekly(request):
    context={}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/top.html', context)

def labbrtiweekly2(request):
    context={}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/Specimensrun.html', context)

def labbrtiweekly3(request):
    context={}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/specimenreceived.html', context)

def labbrtiweekly4(request):
    context={}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/Reasonsforfailures.html', context)

def labbrtiweekly5(request):
    context={}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/electricoutagestool.html', context)




# @method_decorator([login_required], name='dispatch')
# class RecordAddView(CreateView):

#     model = Record
#     form_class = RecordAddForm
#     template_name = 'templates/add_record.html'


#     def form_valid(self, form):
#         print("===============try try=====================================",self.request.user)

#         #form.owner = str(self.request.user)
#         obj = form.save(commit=False)
#         obj.owner = str(self.request.user)
#         obj.save()
#         #form.save()
#         return redirect('127.0.0.1:8000')

