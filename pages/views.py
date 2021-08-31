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




#function to get current reporting week

def getReportingWeek():
    #do calcs

    #for every new reporting week we nned to create new empty total records for that week to be used that week
    #ie for every lab total create an total for that lab to be updated by incomming records

    #     labchoices=[
    #     ('NMRL','NMRL'),
    #     ('Mpilo','Mpilo'),
    #     ('BRIDH','BRIDH'),
    #     ('NTBRL','NTBRL'),
    #     ('Gweru','Gweru'),
    #     ('Chinhoyi','Chinhoyi'),
    #     ('Masvingo','Masvingo'),
    #     ('eid','eid'),
    #     ('Victoria Falls', 'Victoria Falls'),
    #     ('Bindura','Bindura'),
    #     ('Kadoma','Kadoma'),
    #     ('Marondera','Marondera'),
    #     ('St Lukes', 'St Lukes'),
    #     ('Gwanda','Gwanda'),
        
    # ]

    return "1"


















#------------------------------lab vl--------------------------------------------------------------------------------------------------------













def labvltop(request):
    if request.method == 'POST':
        form = SpecimensrunbrtivlweeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = SpecimensrunbrtivlweeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/top.html', context)





def labvlrun(request):
    if request.method == 'POST':
        form = SpecimensrunbrtivlweeklyForm(request.POST)
        if form.is_valid():
            
            updateTotal = specimensrunbrtivleid.objects.get(key="vl", lab=request.user.lab,reportingweek=getReportingWeek() )

            updateTotal.testsdonerochenumberofsamplesreceivedthisweekplasma = updateTotal.testsdonerochenumberofsamplesreceivedthisweekplasma + form.cleaned_data.get('testsdonerochenumberofsamplesreceivedthisweekplasma')
            updateTotal.testsdonerochenumberofsamplescarriedoverpreviousweeksplasma = updateTotal.testsdonerochenumberofsamplescarriedoverpreviousweeksplasma + form.cleaned_data.get('testsdonerochenumberofsamplescarriedoverpreviousweeksplasma')
            
            updateTotal.testsdonerochefailedbuteligibaleforrepeatplasma += form.cleaned_data.get('testsdonerochefailedbuteligibaleforrepeatplasma')
            updateTotal.testsdonerochefailedbutnoteligibaleforrepeatplasma += form.cleaned_data.get('testsdonerochefailedbutnoteligibaleforrepeatplasma')
            updateTotal.testsdonerocherepeatplasma += form.cleaned_data.get('testsdonerocherepeatplasma')
            updateTotal.testsdonerochefailedafterrepeattestingplasma += form.cleaned_data.get('testsdonerochefailedafterrepeattestingplasma')
            updateTotal.testsdonerochenumberofsamplesreceivedthisweekdbs += form.cleaned_data.get('testsdonerochenumberofsamplesreceivedthisweekdbs')

            updateTotal.testsdonerochenumberofsamplescarriedoverpreviousweeksdbs += form.cleaned_data.get('testsdonerochenumberofsamplescarriedoverpreviousweeksdbs')
            updateTotal.testsdonerochefailedbuteligibaleforrepeatdbs += form.cleaned_data.get('testsdonerochefailedbuteligibaleforrepeatdbs')
            updateTotal.testsdonerochefailedbutnoteligibaleforrepeatdbs += form.cleaned_data.get('testsdonerochefailedbutnoteligibaleforrepeatdbs')
            updateTotal.testsdonerocherepeatdbs += form.cleaned_data.get('testsdonerocherepeatdbs')
            updateTotal.testsdonerochefailedafterrepeattestingdbs += form.cleaned_data.get('testsdonerochefailedafterrepeattestingdbs')
            updateTotal.testsdonebmxnumberofsamplesreceivedthisweekplasma += form.cleaned_data.get('testsdonebmxnumberofsamplesreceivedthisweekplasma')

            updateTotal.testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma += form.cleaned_data.get('testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma')
            updateTotal.testsdonebmxfailedbuteligibaleforrepeatplasma += form.cleaned_data.get('testsdonebmxfailedbuteligibaleforrepeatplasma')
            updateTotal.testsdonebmxfailedbutnoteligibaleforrepeatplasma += form.cleaned_data.get('testsdonebmxfailedbutnoteligibaleforrepeatplasma')
            updateTotal.testsdonebmxrepeatplasma += form.cleaned_data.get('testsdonebmxrepeatplasma')
            updateTotal.testsdonebmxfailedafterrepeattestingplasma += form.cleaned_data.get('testsdonebmxfailedafterrepeattestingplasma')
            updateTotal.testsdonebmxnumberofsamplesreceivedthisweekdbs += form.cleaned_data.get('testsdonebmxnumberofsamplesreceivedthisweekdbs')

            updateTotal.testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs += form.cleaned_data.get('testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs')
            updateTotal.testsdonebmxfailedbuteligibaleforrepeatdbs += form.cleaned_data.get('testsdonebmxfailedbuteligibaleforrepeatdbs')
            updateTotal.testsdonebmxfailedbutnoteligibaleforrepeatdbs += form.cleaned_data.get('testsdonebmxfailedbutnoteligibaleforrepeatdbs')
            updateTotal.testsdonebmxrepeatdbs += form.cleaned_data.get('testsdonebmxrepeatdbs')
            updateTotal.testsdonebmxfailedafterrepeattestingdbs += form.cleaned_data.get('testsdonebmxfailedafterrepeattestingdbs')
            updateTotal.testsdoneabbottnumberofsamplesreceivedthisweekplasma += form.cleaned_data.get('testsdoneabbottnumberofsamplesreceivedthisweekplasma')

            updateTotal.testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma += form.cleaned_data.get('testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma')
            updateTotal.testsdoneabbottfailedbuteligibaleforrepeatplasma += form.cleaned_data.get('testsdoneabbottfailedbuteligibaleforrepeatplasma')
            updateTotal.testsdoneabbottfailedbutnoteligibaleforrepeatplasma += form.cleaned_data.get('testsdoneabbottfailedbutnoteligibaleforrepeatplasma')
            updateTotal.testsdoneabbottrepeatplasma += form.cleaned_data.get('testsdoneabbottrepeatplasma')
            updateTotal.testsdoneabbottfailedafterrepeattestingplasma += form.cleaned_data.get('testsdoneabbottfailedafterrepeattestingplasma')
            updateTotal.testsdoneabbottnumberofsamplesreceivedthisweekdbs += form.cleaned_data.get('testsdoneabbottnumberofsamplesreceivedthisweekdbs')

            updateTotal.testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs += form.cleaned_data.get('testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs')
            updateTotal.testsdoneabbottfailedbuteligibaleforrepeatdbs += form.cleaned_data.get('testsdoneabbottfailedbuteligibaleforrepeatdbs')
            updateTotal.testsdoneabbottfailedbutnoteligibaleforrepeatdbs += form.cleaned_data.get('testsdoneabbottfailedbutnoteligibaleforrepeatdbs')
            updateTotal.testsdoneabbottrepeatdbs += form.cleaned_data.get('testsdoneabbottrepeatdbs')
            updateTotal.testsdoneabbottfailedafterrepeattestingdbs += form.cleaned_data.get('testsdoneabbottfailedafterrepeattestingdbs')
            updateTotal.testsdonehologicpanthernumberofsamplesreceivedthisweekplasma += form.cleaned_data.get('testsdonehologicpanthernumberofsamplesreceivedthisweekplasma')

            updateTotal.tests2 += form.cleaned_data.get('tests2')
            updateTotal.testsdonehologicpantherfailedbuteligibaleforrepeatplasma += form.cleaned_data.get('testsdonehologicpantherfailedbuteligibaleforrepeatplasma')
            updateTotal.testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma += form.cleaned_data.get('testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma')
            updateTotal.testsdonehologicpantherrepeatplasma += form.cleaned_data.get('testsdonehologicpantherrepeatplasma')
            updateTotal.testsdonehologicpantherfailedafterrepeattestingplasma += form.cleaned_data.get('testsdonehologicpantherfailedafterrepeattestingplasma')
            updateTotal.testsdonehologicpanthernumberofsamplesreceivedthisweekdbs += form.cleaned_data.get('testsdonehologicpanthernumberofsamplesreceivedthisweekdbs')

            updateTotal.tests1 += form.cleaned_data.get('tests1')
            updateTotal.testsdonehologicpantherfailedbuteligibaleforrepeatdbs += form.cleaned_data.get('testsdonehologicpantherfailedbuteligibaleforrepeatdbs')
            updateTotal.testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs += form.cleaned_data.get('testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs')
            updateTotal.testsdonehologicpantherrepeatdbs += form.cleaned_data.get('testsdonehologicpantherrepeatdbs')
            updateTotal.testsdonehologicpantherfailedafterrepeattestingdbs += form.cleaned_data.get('testsdonehologicpantherfailedafterrepeattestingdbs')
            updateTotal.totaltestsdone += form.cleaned_data.get('totaltestsdone')

            updateTotal.totalrepeats += form.cleaned_data.get('totalrepeats')
            updateTotal.totalpatientsrun += form.cleaned_data.get('totalpatientsrun')
            updateTotal.targetsweekly += form.cleaned_data.get('targetsweekly')
            updateTotal.percentagetargetsachievements += form.cleaned_data.get('percentagetargetsachievements')
            updateTotal.percentageerrorraterocheplasma += form.cleaned_data.get('percentageerrorraterocheplasma')
            updateTotal.percentageerrorraterochedbs += form.cleaned_data.get('percentageerrorraterochedbs')

            updateTotal.percentageerrorratebmxplasma += form.cleaned_data.get('percentageerrorratebmxplasma')
            updateTotal.percentageerrorratebmxdbs += form.cleaned_data.get('percentageerrorratebmxdbs')
            updateTotal.percentageerrorrateabbottplasma += form.cleaned_data.get('percentageerrorrateabbottplasma')
            updateTotal.percentageerrorrateabbottdbs += form.cleaned_data.get('percentageerrorrateabbottdbs')
            updateTotal.percentageerrorratehologicpantherplasma += form.cleaned_data.get('percentageerrorratehologicpantherplasma')
            updateTotal.percentageerrorratehologicpantherdbs += form.cleaned_data.get('percentageerrorratehologicpantherdbs')

            updateTotal.totalncsfromaudit += form.cleaned_data.get('totalncsfromaudit')
            updateTotal.ncsnotyetclosed += form.cleaned_data.get('ncsnotyetclosed')
            updateTotal.lab = request.user.lab
            updateTotal.key = "vl"
            updateTotal.testsdoneabbottrun += form.cleaned_data.get('testsdoneabbottrun')
            updateTotal.testsdoneabbottrun += form.cleaned_data.get('testsdoneabbottrun')



            updateTotal.save()
            form.save()
            #return render(request, 'success.html')
    form = SpecimensrunbrtivlweeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/Specimensrun.html', context)

def labvlrecieved(request):
    if request.method == 'POST':
        form = SpecimensrecievedbrtivlweeklyForm(request.POST)
        if form.is_valid():
            updateTotal = specimensreceivedbrtivleid.objects.get(key="vl", lab=request.user.lab,reportingweek=getReportingWeek() )

            updateTotal.totalncsfromaudit += form.cleaned_data.get('totalncsfromaudit')


            form.save()
            #return render(request, 'success.html')
    form = SpecimensrecievedbrtivlweeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/specimenreceived.html', context)

def labvlfailure(request):
    if request.method == 'POST':
        form = ReasonsforfailurebrtivlweeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = ReasonsforfailurebrtivlweeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/Reasonsforfailures.html', context)

def labvlelectric(request):
    if request.method == 'POST':
        form = ElectricoutagebrtivlweeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = ElectricoutagebrtivlweeklyForm()
    context = {'form': form}
    return render(request, 'masving_brti_vl_weekly_statistics_tool_31-6_june_2021/electricoutagestool.html', context)



#-------------------------lab cov 19-------------------------------------------------------------------------------------------------------------------




def labcov19top(request):

    #before save create or update the unique row called total to be sent over as an entry to brti cov 19 table
    if request.method == 'POST':
        form = SpecimensrunbrtivlweeklyForm(request.POST)
        if form.is_valid():
            brticov19SpecimenRunrecord = covRecordsSpecimenRun(

            )
            form.save()
            #return render(request, 'success.html')
    form = SpecimensrunbrtivlweeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/top.html', context)


def labcov19run(request):
        #before save create or update the unique row called total to be sent over as an entry to brti cov 19 table
    # updateTotal = Specimensruncovid19.objects.get(dayofweek="Total")
    # for row in updateTotal.__dict__:
    #     print(row)

    form = Specimensruncovid19Form()
    if request.method == 'POST':
        form = Specimensruncovid19Form(request.POST)
        if form.is_valid():
            print('hello there mate')
            #get the object for brti cov19 and disect the form object and assign or update the total entry and save
            updateTotal = specimensrunbrticovid19.objects.get(dayofweek="Total", lab='brti',reportingweek=getReportingWeek() )
            

            
            updateTotal.testsdoneabbottrun +=   form.cleaned_data.get('testsdoneabbottrun')





            updateTotal.testsdoneabbottfailedbuteligibaleforrepeat = updateTotal.testsdoneabbottfailedbuteligibaleforrepeat + form.cleaned_data.get('testsdoneabbottfailedbuteligibaleforrepeat')
            updateTotal.testsdoneabbottfailedbutnoteligibaleforrepeat = updateTotal.testsdoneabbottfailedbutnoteligibaleforrepeat + form.cleaned_data.get('testsdoneabbottfailedbutnoteligibaleforrepeat')
            updateTotal.testsdoneabbottrepeat = updateTotal.testsdoneabbottrepeat + form.cleaned_data.get('testsdoneabbottrepeat')


            updateTotal.testsdonebmxrun = updateTotal.testsdonebmxrun + form.cleaned_data.get('testsdonebmxrun')
            updateTotal.testsdonebmxfailedbuteligibaleforrepeat = updateTotal.testsdonebmxfailedbuteligibaleforrepeat + form.cleaned_data.get('testsdonebmxfailedbuteligibaleforrepeat')
            updateTotal.testsdonebmxfailedbutnoteligibaleforrepeat = updateTotal.testsdonebmxfailedbutnoteligibaleforrepeat + form.cleaned_data.get('testsdonebmxfailedbutnoteligibaleforrepeat')
            updateTotal.testsdonebmxrepeat = updateTotal.testsdonebmxrepeat + form.cleaned_data.get('testsdonebmxrepeat')
            updateTotal.testsdonegenexpertrun = updateTotal.testsdonegenexpertrun + form.cleaned_data.get('testsdonegenexpertrun')
            updateTotal.testsdonegenexpertfailedbuteligibaleforrepeat = updateTotal.testsdonegenexpertfailedbuteligibaleforrepeat + form.cleaned_data.get('testsdonegenexpertfailedbuteligibaleforrepeat')
            updateTotal.testsdonegenexpertfailedbutnoteligibaleforrepeat = updateTotal.testsdonegenexpertfailedbutnoteligibaleforrepeat + form.cleaned_data.get('testsdonegenexpertfailedbutnoteligibaleforrepeat')
            updateTotal.testsdonegenexpertrepeat = updateTotal.testsdonegenexpertrepeat + form.cleaned_data.get('testsdonegenexpertrepeat')


            updateTotal.testsdonequantstudio3run = updateTotal.testsdonequantstudio3run + form.cleaned_data.get('testsdonequantstudio3run')
            updateTotal.testsdonequantstudio3failedbuteligibaleforrepeat = updateTotal.testsdonequantstudio3failedbuteligibaleforrepeat + form.cleaned_data.get('testsdonequantstudio3failedbuteligibaleforrepeat')
            updateTotal.testsdonequantstudio3failedbutnoteligibaleforrepeat = updateTotal.testsdonequantstudio3failedbutnoteligibaleforrepeat + form.cleaned_data.get('testsdonequantstudio3failedbutnoteligibaleforrepeat')
            updateTotal.testsdonequantstudio3repeat = updateTotal.testsdonequantstudio3repeat + form.cleaned_data.get('testsdonequantstudio3repeat')


            updateTotal.testsdonehologicpantherrun = updateTotal.testsdonehologicpantherrun + form.cleaned_data.get('testsdonehologicpantherrun')
            updateTotal.testsdonehologicpantherfailedbuteligibaleforrepeat = updateTotal.testsdonehologicpantherfailedbuteligibaleforrepeat + form.cleaned_data.get('testsdonehologicpantherfailedbuteligibaleforrepeat')
            updateTotal.testsdonehologicpantherfailedbutnoteligibaleforrepeat = updateTotal.testsdonehologicpantherfailedbutnoteligibaleforrepeat + form.cleaned_data.get('testsdonehologicpantherfailedbutnoteligibaleforrepeat')
            updateTotal.testsdonehologicpantherrepeat = updateTotal.testsdonehologicpantherrepeat + form.cleaned_data.get('testsdonehologicpantherrepeat')
            updateTotal.testsdonerdtabrun = updateTotal.testsdonerdtabrun + form.cleaned_data.get('testsdonerdtabrun')


            updateTotal.testsdonerdtabfailedbuteligibaleforrepeat = updateTotal.testsdonerdtabfailedbuteligibaleforrepeat + form.cleaned_data.get('testsdonerdtabfailedbuteligibaleforrepeat')
            updateTotal.testsdonerdtabfailedbutnoteligibaleforrepeat = updateTotal.testsdonerdtabfailedbutnoteligibaleforrepeat + form.cleaned_data.get('testsdonerdtabfailedbutnoteligibaleforrepeat')
            updateTotal.testsdonerdtabrepeat = updateTotal.testsdonerdtabrepeat + form.cleaned_data.get('testsdonerdtabrepeat')


            updateTotal.testsdonerdtagrun = updateTotal.testsdonerdtagrun + form.cleaned_data.get('testsdonerdtagrun')
            updateTotal.testsdonerdtagfailedbuteligibaleforrepeat = updateTotal.testsdonerdtagfailedbuteligibaleforrepeat + form.cleaned_data.get('testsdonerdtagfailedbuteligibaleforrepeat')
            updateTotal.testsdonerdtagfailedbutnoteligibaleforrepeat = updateTotal.testsdonerdtagfailedbutnoteligibaleforrepeat + form.cleaned_data.get('testsdonerdtagfailedbutnoteligibaleforrepeat')
            
            updateTotal.testsdonerdtagrepeat = updateTotal.testsdonerdtagrepeat + form.cleaned_data.get('testsdonerdtagrepeat')
            updateTotal.totaltestsdone = updateTotal.totaltestsdone + form.cleaned_data.get('totaltestsdone')
            updateTotal.totalrepeats = updateTotal.totalrepeats + form.cleaned_data.get('totalrepeats')
            updateTotal.totalpatientsrun = updateTotal.totalpatientsrun + form.cleaned_data.get('totalpatientsrun')

            updateTotal.errorratesabbott = updateTotal.errorratesabbott + form.cleaned_data.get('errorratesabbott')
            updateTotal.errorratesbmx = updateTotal.errorratesbmx + form.cleaned_data.get('errorratesbmx')
            updateTotal.errorratesgenexpert = updateTotal.errorratesgenexpert + form.cleaned_data.get('errorratesgenexpert')
            updateTotal.errorratesquantstudio3 = updateTotal.errorratesquantstudio3 + form.cleaned_data.get('errorratesquantstudio3')
            updateTotal.errorrateshologicpanther = updateTotal.errorrateshologicpanther + form.cleaned_data.get('errorrateshologicpanther')
            updateTotal.errorratesrdtab = updateTotal.errorratesrdtab + form.cleaned_data.get('errorratesrdtab')
            updateTotal.errorratesrdtag = updateTotal.errorratesrdtag + form.cleaned_data.get('errorratesrdtag')

           
            # updateTotal.save()

            #updateTotal.save()

            form.save()
            #return render(request, 'success.html')
    form = Specimensruncovid19Form()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/Specimens_Run.html', context)

def labcov19recieved(request):
    # updateTotal = Specimensreceivedcovid19.objects.get(dayofweek="Total")
    # for row in updateTotal.__dict__:
    #         print(updateTotal.__dict__[row].)

    if request.method == 'POST':
        form = Specimensreceivedcovid19Form(request.POST)
        if form.is_valid():
            print('e=nter tge rhtiung')
            updateTotal = specimensreceivedbrticovid19.objects.get(dayofweek="Total",lab='brti',reportingweek='1')

            updateTotal = specimensreceivedbrticovid19.objects.get(dayofweek="Total",lab='brti',reportingweek='1')
            updateTotal.samplescarriedoverpreviousweeks = updateTotal.samplescarriedoverpreviousweeks + form.cleaned_data.get('samplescarriedoverpreviousweeks')
            updateTotal.samplesreceivedcurrentweeknasopharyngealswab = updateTotal.samplesreceivedcurrentweeknasopharyngealswab + form.cleaned_data.get('samplesreceivedcurrentweeknasopharyngealswab')
            updateTotal.samplesreceivedcurrentweeknasalswab = updateTotal.samplesreceivedcurrentweeknasalswab + form.cleaned_data.get('samplesreceivedcurrentweeknasalswab')
            updateTotal.samplesreceivedcurrentweekoropharyngealswab = updateTotal.samplesreceivedcurrentweekoropharyngealswab + form.cleaned_data.get('samplesreceivedcurrentweekoropharyngealswab')

            updateTotal.samplesreceivedcurrentweekmidturbinateswab = updateTotal.samplesreceivedcurrentweekmidturbinateswab + form.cleaned_data.get('samplesreceivedcurrentweekmidturbinateswab')
            updateTotal.samplesreceivedcurrentweeksputum = updateTotal.samplesreceivedcurrentweeksputum + form.cleaned_data.get('samplesreceivedcurrentweeksputum')
            updateTotal.samplesreceivedcurrentweekwholebloodorplasmaorserum = updateTotal.samplesreceivedcurrentweekwholebloodorplasmaorserum + form.cleaned_data.get('samplesreceivedcurrentweekwholebloodorplasmaorserum')
            updateTotal.samplesreceivedcurrentweekother = updateTotal.samplesreceivedcurrentweekother + form.cleaned_data.get('samplesreceivedcurrentweekother')

            updateTotal.samplesrejectedcurrentweek = updateTotal.samplesrejectedcurrentweek + form.cleaned_data.get('samplesrejectedcurrentweek')
            updateTotal.totalsamplesreceivedcurrentweek = updateTotal.totalsamplesreceivedcurrentweek + form.cleaned_data.get('totalsamplesreceivedcurrentweek')
            updateTotal.numberofsamplesenteredintolims = updateTotal.numberofsamplesenteredintolims + form.cleaned_data.get('numberofsamplesenteredintolims')
            updateTotal.totalsamplescurrentpluscarryover = updateTotal.totalsamplescurrentpluscarryover + form.cleaned_data.get('totalsamplescurrentpluscarryover')

            updateTotal.samplesreferred = updateTotal.samplesreferred + form.cleaned_data.get('samplesreferred')
            updateTotal.rejectionratecurrentweek = updateTotal.rejectionratecurrentweek + form.cleaned_data.get('rejectionratecurrentweek')
            updateTotal.numberofresultsprintedlims = updateTotal.numberofresultsprintedlims + form.cleaned_data.get('numberofresultsprintedlims')
            updateTotal.totalresultsdispatchedbylab = updateTotal.totalresultsdispatchedbylab + form.cleaned_data.get('totalresultsdispatchedbylab')

#mostt likely to crush if we keep on joining comments 
            updateTotal.comment = updateTotal.comment + form.cleaned_data.get('comment')
            updateTotal.samplesReferredtoName = updateTotal.samplesReferredtoName + form.cleaned_data.get('samplesReferredtoName')
            updateTotal.errorratesabbott = updateTotal.errorratesabbott + form.cleaned_data.get('errorratesabbott')
            updateTotal.errorratesabbott = updateTotal.errorratesabbott + form.cleaned_data.get('errorratesabbott')




            updateTotal.save()

            form.save()
            #return render(request, 'success.html')
    form = Specimensreceivedcovid19Form()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/Specimens_Received.html', context)

def labcov19general(request):
    if request.method == 'POST':
        form = Generalcovid19Form(request.POST)
        if form.is_valid():
            updateTotal = generalbrticovid19.objects.get(dayofweek="Total",lab=request.user.lab,reportingweek=getReportingWeek())
            updateTotal.commentsregardingtestingandchallengesfacedbythelaboratory = updateTotal.commentsregardingtestingandchallengesfacedbythelaboratory + form.cleaned_data.get('commentsregardingtestingandchallengesfacedbythelaboratory')
            updateTotal.numberofstaffwhotestedpositivetocovid19atvllab = updateTotal.numberofstaffwhotestedpositivetocovid19atvllab + form.cleaned_data.get('numberofstaffwhotestedpositivetocovid19atvllab')
            updateTotal.numberOfStaffwhotestedpositivetocovid19athubs = updateTotal.numberOfStaffwhotestedpositivetocovid19athubs + form.cleaned_data.get('numberOfStaffwhotestedpositivetocovid19athubs')
            updateTotal.numberofstaffwhohavebeenvaccinated = updateTotal.numberofstaffwhohavebeenvaccinated + form.cleaned_data.get('numberofstaffwhohavebeenvaccinated')
            updateTotal.Comments = updateTotal.Comments + form.cleaned_data.get('Comments')
            # updateTotal.Requesttobrtifromthelaboratory = updateTotal.Requesttobrtifromthelaboratory + form.cleaned_data.get('Requesttobrtifromthelaboratory
            # updateTotal.numberofstaffwhohavebeenvaccinated = updateTotal.numberofstaffwhohavebeenvaccinated + form.cleaned_data.get('numberofstaffwhohavebeenvaccinated
            updateTotal.save()
            form.save()
            #return render(request, 'success.html')
    form = Generalcovid19Form()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/general.html', context)

def labcov19machine(request):
    if request.method == 'POST':
        form = machinedowntimereagentstockouttoolcovid19Form(request.POST)
        if form.is_valid():
            updateTotal = machinedowntimereagentstockouttoolbrticovid19.objects.get(dayofweek="Total", lab=request.user.lab,reportingweek=getReportingWeek())
            updateTotal.numberofmachinebreakdownsabbott = updateTotal.numberofmachinebreakdownsabbott + form.cleaned_data.get('numberofmachinebreakdownsabbott')
            updateTotal.numberofmachinebreakdownsbmx = updateTotal.numberofmachinebreakdownsbmx + form.cleaned_data.get('numberofmachinebreakdownsbmx')
            updateTotal.numberofmachinebreakdownsgenexpert = updateTotal.numberofmachinebreakdownsgenexpert + form.cleaned_data.get('numberofmachinebreakdownsgenexpert')
            updateTotal.numberofmachinebreakdownsquantstudio3 = updateTotal.numberofmachinebreakdownsquantstudio3 + form.cleaned_data.get('numberofmachinebreakdownsquantstudio3')
           
            updateTotal.numberofmachinebreakdownshologicpanther = updateTotal.numberofmachinebreakdownshologicpanther + form.cleaned_data.get('numberofmachinebreakdownshologicpanther')
            updateTotal.numberofmachinebreakdownscomments = updateTotal.numberofmachinebreakdownscomments + form.cleaned_data.get('numberofmachinebreakdownscomments')
            updateTotal.machinedowntimedaysabbott = updateTotal.machinedowntimedaysabbott + form.cleaned_data.get('machinedowntimedaysabbott')
            updateTotal.machinedowntimedaysbmx = updateTotal.machinedowntimedaysbmx + form.cleaned_data.get('machinedowntimedaysbmx')
           
            updateTotal.machinedowntimedaysgenexpert = updateTotal.machinedowntimedaysgenexpert + form.cleaned_data.get('machinedowntimedaysgenexpert')
            updateTotal.machinedowntimedaysquantstudio3 = updateTotal.machinedowntimedaysquantstudio3 + form.cleaned_data.get('machinedowntimedaysquantstudio3')
            updateTotal.machinedowntimedayshologicpanther = updateTotal.machinedowntimedayshologicpanther + form.cleaned_data.get('machinedowntimedayshologicpanther')
            updateTotal.machinedowntimedayscomments = updateTotal.machinedowntimedayscomments + form.cleaned_data.get('machinedowntimedayscomments')
           
            updateTotal.reagentstockoutabbort = updateTotal.reagentstockoutabbort + form.cleaned_data.get('reagentstockoutabbort')
            updateTotal.reagentstockoutbms = updateTotal.reagentstockoutbms + form.cleaned_data.get('reagentstockoutbms')
            updateTotal.reagentstockoutgenexpert = updateTotal.reagentstockoutgenexpert + form.cleaned_data.get('reagentstockoutgenexpert')
            
            updateTotal.reagentstockoutquantstudio3 = updateTotal.reagentstockoutquantstudio3 + form.cleaned_data.get('reagentstockoutquantstudio3')
            updateTotal.reagentstockouthologicpanther = updateTotal.reagentstockouthologicpanther + form.cleaned_data.get('reagentstockouthologicpanther')
            updateTotal.reagentstockoutcomments = updateTotal.reagentstockoutcomments + form.cleaned_data.get('reagentstockoutcomments')
            updateTotal.reagentstockoutcomments = updateTotal.reagentstockoutcomments + form.cleaned_data.get('reagentstockoutcomments')

            # updateTotal.Requesttobrtifromthelaboratory = updateTotal.Requesttobrtifromthelaboratory + form.cleaned_data.get('Requesttobrtifromthelaboratory
            # updateTotal.numberofstaffwhohavebeenvaccinated = updateTotal.numberofstaffwhohavebeenvaccinated + form.cleaned_data.get('numberofstaffwhohavebeenvaccinated
            updateTotal.save()
            form.save()
            #return render(request, 'success.html')
    form = machinedowntimereagentstockouttoolcovid19Form()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/Machine_Downtime_&_Reagent_stock_out_tool.html', context)





#-------------------------------------------lab eid-----------------------------------------------------------------------------------------

def labeidtop(request):
    if request.method == 'POST':
        form = TopbrtiweeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = TopbrtiweeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/top.html', context)

def labeidrun(request):
    if request.method == 'POST':
        form = SpecimensrunbrtivlweeklyForm(request.POST)
        if form.is_valid():


            form.save()
            #return render(request, 'success.html')
    form = SpecimensrunbrtivlweeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/Specimensrun.html', context)

def labeidrecieved(request):
    if request.method == 'POST':
        form = SpecimensreceivedbrtiweeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = SpecimensreceivedbrtiweeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/specimenreceived.html', context)

def labeidfailure(request):
    if request.method == 'POST':
        form = ReasonsforfailurebrtiweeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = ReasonsforfailurebrtiweeklyForm()
    context = {'form': form}
    return render(request, 'masvingo_brti_weekly_statistics_tool_june_2021/Reasonsforfailures.html', context)

def labeidelectric(request):
    if request.method == 'POST':
        form = ElectricoutagebrtiweeklyForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    form = ElectricoutagebrtiweeklyForm()
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

    # rows = Electric_outage_brti_vl_weekly.objects.all().values_list('day_of_week', 'number_of_hours_with_no_electricity_per_day','number_of_hours_generator_was_on_per_day', 'litres_of_fuel_added_to_generator_per_day', 'number_of_hours_machines_was_not_being_used_due_to_power_cut_per_day', 'total_tests_done_per_day_using_generator')
    # for row in rows:
    #     row_num += 1
    #     for col_num in range(len(row)):
    #         ws.write(row_num, col_num, row[col_num], font_style)
    #         ws.write(13, col_num, 5, font_style)


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

#         #form.cleaned_data.get('owner = str(self.request.user)
#         obj = form.cleaned_data.get('save(commit=False)
#         obj.owner = str(self.request.user)
#         obj.save()
#         #form.save()
#         return redirect('127.0.0.1:8000')

