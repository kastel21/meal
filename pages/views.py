from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404, redirect, render
import csv
import xlwt
import datetime
from django.http import JsonResponse
import sqlite3


def exp(request):
    context = {}
    columns=[]
    record=[]

    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursorC = sqliteConnection.cursor()
        cursorR = sqliteConnection.cursor()
        print("Database success")


        f = open("tables.txt",'r')
        tables=f.readlines()
        i=0
        for table in tables:
            # sql_select_Query = "select name from sqlite_master where type='table' and name like 'pages_%';"
            sql_select_Query = "PRAGMA table_info( "+table.strip()+" );"
            cursorC.execute(sql_select_Query)
            columns.append(cursorC.fetchall())
            #print(columns)

            sql_select_Query1 = "select * from "+table+";"
            cursorR.execute(sql_select_Query1)
            record.append(cursorR.fetchall())
            #print(record)

            i=i+1

            context={'columns': columns,
                    'record':record
            }

            # f=open('columns.txt', 'w')
            
            # for table in record:
            #     f.write(str(table) + '\n')

            # f.close()

    except sqlite3.Error as error:
        print("ndatadza sha", error)

    # finally:
    #     if sqliteConnection:
    #         sqliteConnection.close()
    #         print("ndavhara")
    #     cursor.close()


    return render(request, 'excel_home.html', context)


def index(request):
    return HttpResponse("Hello, world. You're at the pages index.")


def home(request):
    context={}

    return render(request, 'base.html', context)

def profile(request):
    # Create your views here.
    
    if request.method == 'POST':
        form = general_brti_covid_19Form(request.POST)
        if form.is_valid():
            form.save()
            ##return render(request, 'success.html')
    form = general_brti_covid_19Form()
    context = {'form': form }

    return render(request, 'brti_covid_19_weekly_statistics_tool/general.html', context)

def profilecovid19to(request):
    if request.method == 'POST':
        form = specimens_run_brti_covid_19Form(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = specimens_run_brti_covid_19Form()
    context = {'form': form}
    return render(request, 'brti_covid_19_weekly_statistics_tool/Specimens_Run.html', context)

def profilecovid(request):
    if request.method == 'POST':
        form = specimens_received_brti_covid_19Form(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = specimens_received_brti_covid_19Form()
    context = {'form': form}
    return render(request, 'brti_covid_19_weekly_statistics_tool/Specimens_Received.html', context)

def profilecovid19(request):
    if request.method == 'POST':
        form = machine_downtime_reagent_stockout_tool_brti_covid_19Form(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = machine_downtime_reagent_stockout_tool_brti_covid_19Form()
    context = {'form': form}
    return render(request, 'brti_covid_19_weekly_statistics_tool/Machine_Downtime_&_Reagent_stock_out_tool.html', context)

def profilecovid19t(request):
    if request.method == 'POST':
        form = general_brti_covid_19Form(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = general_brti_covid_19Form()
    context = {'form': form}
    return render(request, 'brti_covid_19_weekly_statistics_tool/general.html', context)

def vleid(request):
    if request.method == 'POST':
        form = Specimens_run_brti_vl_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_run_brti_vl_weeklyForm()
    context = {'form': form}
    return render(request, 'brti_vl_eid_weekly_statistics_tool/specimens_run.html', context)

def vleid2(request):
    if request.method == 'POST':
        form = specimens_received_brti_vl_eidForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = specimens_received_brti_vl_eidForm()
    context = {'form': form}
    return render(request, 'brti_vl_eid_weekly_statistics_tool/specimens_received.html', context)

def vleid3(request):
    if request.method == 'POST':
        form = reasons_for_failure_brti_vl_eidForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = reasons_for_failure_brti_vl_eidForm()
    context = {'form': form}
    return render(request, 'brti_vl_eid_weekly_statistics_tool/reasons_for_failure.html', context)

def labcovidweekly(request):
    if request.method == 'POST':
        form = Specimens_run_brti_vl_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_run_brti_vl_weeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/top.html', context)

def labcovidweekly2(request):
    if request.method == 'POST':
        form = Specimens_run_brti_vl_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_run_brti_vl_weeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/Specimensrun.html', context)

def labcovidweekly3(request):
    if request.method == 'POST':
        form = Specimens_recieved_brti_vl_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_recieved_brti_vl_weeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/specimenreceived.html', context)

def labcovidweekly4(request):
    if request.method == 'POST':
        form = Reasons_for_failure_brti_vl_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Reasons_for_failure_brti_vl_weeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/Reasonsforfailures.html', context)

def labcovidweekly5(request):
    if request.method == 'POST':
        form = Electric_outage_brti_vl_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Electric_outage_brti_vl_weeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/electricoutagestool.html', context)

def labeidweekly(request):
    if request.method == 'POST':
        form = Specimens_run_brti_vl_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_run_brti_vl_weeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/top.html', context)

def labeidweekly2(request):
    form = Specimens_run_covid_19Form()
    if request.method == 'POST':
        form = Specimens_run_covid_19Form(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_run_covid_19Form()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/Specimens_Run.html', context)

def labeidweekly3(request):
    if request.method == 'POST':
        form = Specimens_received_covid_19Form(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_received_covid_19Form()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/Specimens_Received.html', context)

def labeidweekly4(request):
    if request.method == 'POST':
        form = General_covid_19Form(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = General_covid_19Form()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/general.html', context)

def labbrtiweekly(request):
    if request.method == 'POST':
        form = Top_brti_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Top_brti_weeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/top.html', context)

def labbrtiweekly2(request):
    if request.method == 'POST':
        form = Specimens_run_brti_vl_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_run_brti_vl_weeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/Specimensrun.html', context)

def labbrtiweekly3(request):
    if request.method == 'POST':
        form = Specimens_received_brti_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Specimens_received_brti_weeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/specimenreceived.html', context)

def labbrtiweekly4(request):
    if request.method == 'POST':
        form = Reasons_for_failure_brti_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Reasons_for_failure_brti_weeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/Reasonsforfailures.html', context)

def labbrtiweekly5(request):
    if request.method == 'POST':
        form = Electric_outage_brti_weeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = Electric_outage_brti_weeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/electricoutagestool.html', context)

def export_csv(request):

    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=users' + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Day of the week','Number of hours with no electricity per day','Number of hours generator was on per day', 'number of hours generator was on per day', 'litres of fuel added to generator per day', 'number of hours machine was not being used due to power cut per day', 'total tests done per day using generator']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

     # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Electric_outage_brti_vl_weekly.objects.all().values_list('day_of_week', 'number_of_hours_with_no_electricity_per_day','number_of_hours_generator_was_on_per_day', 'litres_of_fuel_added_to_generator_per_day', 'number_of_hours_machines_was_not_being_used_due_to_power_cut_per_day', 'total_tests_done_per_day_using_generator')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    # ro = Reasons_for_failure_brti_vl_weekly.objects.all().values_list('roche_plasma_number_of_failed_tests_due_to_sample_quality_issues', 'number_of_hours_with_no_electricity_per_day','number_of_hours_generator_was_on_per_day', 'litres_of_fuel_added_to_generator_per_day', 'number_of_hours_machines_was_not_being_used_due_to_power_cut_per_day', 'total_tests_done_per_day_using_generator')
    # for row in ro:
    #     row_num += 1
    #     for col_num in range(len(row)):
    #         ws.write(row_num, col_num, row[col_num], font_style)

    # wb.save(response)

    # writer=csv.writer(response)
    # writer.writerow(['Day of the week','Number of hours with no electricity per day','Number of hours generator was on per day'])
    

    # electric=Electric_outage_brti_vl_weekly.objects.all()

    # for electric in Electric_outage_brti_vl_weekly.objects.all().values_list('day_of_week', 'number_of_hours_with_no_electricity_per_day','number_of_hours_generator_was_on_per_day'):
        
    #     writer.writerow(electric)


    # for reasons in Reasons_for_failure_brti_vl_weekly.objects.all().values_list('roche_plasma_number_of_failed_tests_due_to_sample_quality_issues', 'roche_plasma_number_of_failed_tests_due_to_reagent_quality_issues'):
        
    #         writer.writerow(reasons)

   

    return response 

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

