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

    return "1:30 august - 5 september"


















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

            updateTotal.testsdonerochenumberofsamplesreceivedthisweekplasma = updateTotal.testsdonerochenumberofsamplesreceivedthisweekplasma + form.testsdonerochenumberofsamplesreceivedthisweekplasma
            updateTotal.testsdonerochenumberofsamplescarriedoverpreviousweeksplasma = updateTotal.testsdonerochenumberofsamplescarriedoverpreviousweeksplasma + form.testsdoneabbottrun
            
            updateTotal.testsdonerochefailedbuteligibaleforrepeatplasma += form.testsdonerochefailedbuteligibaleforrepeatplasma
            updateTotal.testsdonerochefailedbutnoteligibaleforrepeatplasma += form.testsdonerochefailedbutnoteligibaleforrepeatplasma
            updateTotal.testsdonerocherepeatplasma += form.testsdonerocherepeatplasma
            updateTotal.testsdonerochefailedafterrepeattestingplasma += form.testsdonerochefailedafterrepeattestingplasma
            updateTotal.testsdonerochenumberofsamplesreceivedthisweekdbs += form.testsdonerochenumberofsamplesreceivedthisweekdbs

            updateTotal.testsdonerochenumberofsamplescarriedoverpreviousweeksdbs += form.testsdonerochenumberofsamplescarriedoverpreviousweeksdbs
            updateTotal.testsdonerochefailedbuteligibaleforrepeatdbs += form.testsdonerochefailedbuteligibaleforrepeatdbs
            updateTotal.testsdonerochefailedbutnoteligibaleforrepeatdbs += form.testsdonerochefailedbutnoteligibaleforrepeatdbs
            updateTotal.testsdonerocherepeatdbs += form.testsdonerocherepeatdbs
            updateTotal.testsdonerochefailedafterrepeattestingdbs += form.testsdonerochefailedafterrepeattestingdbs
            updateTotal.testsdonebmxnumberofsamplesreceivedthisweekplasma += form.testsdonebmxnumberofsamplesreceivedthisweekplasma

            updateTotal.testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma += form.testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma
            updateTotal.testsdonebmxfailedbuteligibaleforrepeatplasma += form.testsdonebmxfailedbuteligibaleforrepeatplasma
            updateTotal.testsdonebmxfailedbutnoteligibaleforrepeatplasma += form.testsdonebmxfailedbutnoteligibaleforrepeatplasma
            updateTotal.testsdonebmxrepeatplasma += form.testsdonebmxrepeatplasma
            updateTotal.testsdonebmxfailedafterrepeattestingplasma += form.testsdonebmxfailedafterrepeattestingplasma
            updateTotal.testsdonebmxnumberofsamplesreceivedthisweekdbs += form.testsdonebmxnumberofsamplesreceivedthisweekdbs

            updateTotal.testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs += form.testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs
            updateTotal.testsdonebmxfailedbuteligibaleforrepeatdbs += form.testsdonebmxfailedbuteligibaleforrepeatdbs
            updateTotal.testsdonebmxfailedbutnoteligibaleforrepeatdbs += form.testsdonebmxfailedbutnoteligibaleforrepeatdbs
            updateTotal.testsdonebmxrepeatdbs += form.testsdonebmxrepeatdbs
            updateTotal.testsdonebmxfailedafterrepeattestingdbs += form.testsdonebmxfailedafterrepeattestingdbs
            updateTotal.testsdoneabbottnumberofsamplesreceivedthisweekplasma += form.testsdoneabbottnumberofsamplesreceivedthisweekplasma

            updateTotal.testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma += form.testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma
            updateTotal.testsdoneabbottfailedbuteligibaleforrepeatplasma += form.testsdoneabbottfailedbuteligibaleforrepeatplasma
            updateTotal.testsdoneabbottfailedbutnoteligibaleforrepeatplasma += form.testsdoneabbottfailedbutnoteligibaleforrepeatplasma
            updateTotal.testsdoneabbottrepeatplasma += form.testsdoneabbottrepeatplasma
            updateTotal.testsdoneabbottfailedafterrepeattestingplasma += form.testsdoneabbottfailedafterrepeattestingplasma
            updateTotal.testsdoneabbottnumberofsamplesreceivedthisweekdbs += form.testsdoneabbottnumberofsamplesreceivedthisweekdbs

            updateTotal.testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs += form.testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs
            updateTotal.testsdoneabbottfailedbuteligibaleforrepeatdbs += form.testsdoneabbottfailedbuteligibaleforrepeatdbs
            updateTotal.testsdoneabbottfailedbutnoteligibaleforrepeatdbs += form.testsdoneabbottfailedbutnoteligibaleforrepeatdbs
            updateTotal.testsdoneabbottrepeatdbs += form.testsdoneabbottrepeatdbs
            updateTotal.testsdoneabbottfailedafterrepeattestingdbs += form.testsdoneabbottfailedafterrepeattestingdbs
            updateTotal.testsdonehologicpanthernumberofsamplesreceivedthisweekplasma += form.testsdonehologicpanthernumberofsamplesreceivedthisweekplasma

            updateTotal.tests2 += form.tests2
            updateTotal.testsdonehologicpantherfailedbuteligibaleforrepeatplasma += form.testsdonehologicpantherfailedbuteligibaleforrepeatplasma
            updateTotal.testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma += form.testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma
            updateTotal.testsdonehologicpantherrepeatplasma += form.testsdonehologicpantherrepeatplasma
            updateTotal.testsdonehologicpantherfailedafterrepeattestingplasma += form.testsdonehologicpantherfailedafterrepeattestingplasma
            updateTotal.testsdonehologicpanthernumberofsamplesreceivedthisweekdbs += form.testsdonehologicpanthernumberofsamplesreceivedthisweekdbs

            updateTotal.tests1 += form.tests1
            updateTotal.testsdonehologicpantherfailedbuteligibaleforrepeatdbs += form.testsdonehologicpantherfailedbuteligibaleforrepeatdbs
            updateTotal.testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs += form.testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs
            updateTotal.testsdonehologicpantherrepeatdbs += form.testsdonehologicpantherrepeatdbs
            updateTotal.testsdonehologicpantherfailedafterrepeattestingdbs += form.testsdonehologicpantherfailedafterrepeattestingdbs
            updateTotal.totaltestsdone += form.totaltestsdone

            updateTotal.totalrepeats += form.totalrepeats
            updateTotal.totalpatientsrun += form.totalpatientsrun
            updateTotal.targetsweekly += form.targetsweekly
            updateTotal.percentagetargetsachievements += form.percentagetargetsachievements
            updateTotal.percentageerrorraterocheplasma += form.percentageerrorraterocheplasma
            updateTotal.percentageerrorraterochedbs += form.percentageerrorraterochedbs

            updateTotal.percentageerrorratebmxplasma += form.percentageerrorratebmxplasma
            updateTotal.percentageerrorratebmxdbs += form.percentageerrorratebmxdbs
            updateTotal.percentageerrorrateabbottplasma += form.percentageerrorrateabbottplasma
            updateTotal.percentageerrorrateabbottdbs += form.percentageerrorrateabbottdbs
            updateTotal.percentageerrorratehologicpantherplasma += form.percentageerrorratehologicpantherplasma
            updateTotal.percentageerrorratehologicpantherdbs += form.percentageerrorratehologicpantherdbs

            updateTotal.totalncsfromaudit += form.totalncsfromaudit
            updateTotal.ncsnotyetclosed += form.ncsnotyetclosed
            updateTotal.lab = request.user.lab
            updateTotal.key = "vl"
            updateTotal.testsdoneabbottrun += form.testsdoneabbottrun
            updateTotal.testsdoneabbottrun += form.testsdoneabbottrun



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

            updateTotal.totalncsfromaudit += form.totalncsfromaudit


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
            #get the object for brti cov19 and disect the form object and assign or update the total entry and save
            updateTotal = Specimensruncovid19.objects.get(dayofweek="Total", lab=request.user.lab,reportingweek=getReportingWeek() )
            

            
            updateTotal.testsdoneabbottrun = updateTotal.testsdoneabbottrun + form.testsdoneabbottrun
            updateTotal.testsdoneabbottfailedbuteligibaleforrepeat = updateTotal.testsdoneabbottfailedbuteligibaleforrepeat + form.testsdoneabbottfailedbuteligibaleforrepeat
            updateTotal.testsdoneabbottfailedbutnoteligibaleforrepeat = updateTotal.testsdoneabbottfailedbutnoteligibaleforrepeat + form.testsdoneabbottfailedbutnoteligibaleforrepeat
            updateTotal.testsdoneabbottrepeat = updateTotal.testsdoneabbottrepeat + form.testsdoneabbottrepeat


            updateTotal.testsdonebmxrun = updateTotal.testsdonebmxrun + form.testsdonebmxrun
            updateTotal.testsdonebmxfailedbuteligibaleforrepeat = updateTotal.testsdonebmxfailedbuteligibaleforrepeat + form.testsdonebmxfailedbuteligibaleforrepeat
            updateTotal.testsdonebmxfailedbutnoteligibaleforrepeat = updateTotal.testsdonebmxfailedbutnoteligibaleforrepeat + form.testsdonebmxfailedbutnoteligibaleforrepeat
            updateTotal.testsdonebmxrepeat = updateTotal.testsdonebmxrepeat + form.testsdonebmxrepeat
            updateTotal.testsdonegenexpertrun = updateTotal.testsdonegenexpertrun + form.testsdonegenexpertrun
            updateTotal.testsdonegenexpertfailedbuteligibaleforrepeat = updateTotal.testsdonegenexpertfailedbuteligibaleforrepeat + form.testsdonegenexpertfailedbuteligibaleforrepeat
            updateTotal.testsdonegenexpertfailedbutnoteligibaleforrepeat = updateTotal.testsdonegenexpertfailedbutnoteligibaleforrepeat + form.testsdonegenexpertfailedbutnoteligibaleforrepeat
            updateTotal.testsdonegenexpertrepeat = updateTotal.testsdonegenexpertrepeat + form.testsdonegenexpertrepeat


            updateTotal.testsdonequantstudio3run = updateTotal.testsdonequantstudio3run + form.testsdonequantstudio3run
            updateTotal.testsdonequantstudio3failedbuteligibaleforrepeat = updateTotal.testsdonequantstudio3failedbuteligibaleforrepeat + form.testsdonequantstudio3failedbuteligibaleforrepeat
            updateTotal.testsdonequantstudio3failedbutnoteligibaleforrepeat = updateTotal.testsdonequantstudio3failedbutnoteligibaleforrepeat + form.testsdonequantstudio3failedbutnoteligibaleforrepeat
            updateTotal.testsdonequantstudio3repeat = updateTotal.testsdonequantstudio3repeat + form.testsdonequantstudio3repeat


            updateTotal.testsdonehologicpantherrun = updateTotal.testsdonehologicpantherrun + form.testsdonehologicpantherrun
            updateTotal.testsdonehologicpantherfailedbuteligibaleforrepeat = updateTotal.testsdonehologicpantherfailedbuteligibaleforrepeat + form.testsdonehologicpantherfailedbuteligibaleforrepeat
            updateTotal.testsdonehologicpantherfailedbutnoteligibaleforrepeat = updateTotal.testsdonehologicpantherfailedbutnoteligibaleforrepeat + form.testsdonehologicpantherfailedbutnoteligibaleforrepeat
            updateTotal.testsdonehologicpantherrepeat = updateTotal.testsdonehologicpantherrepeat + form.testsdonehologicpantherrepeat
            updateTotal.testsdonerdtabrun = updateTotal.testsdonerdtabrun + form.testsdonerdtabrun


            updateTotal.testsdonerdtabfailedbuteligibaleforrepeat = updateTotal.testsdonerdtabfailedbuteligibaleforrepeat + form.testsdonerdtabfailedbuteligibaleforrepeat
            updateTotal.testsdonerdtabfailedbutnoteligibaleforrepeat = updateTotal.testsdonerdtabfailedbutnoteligibaleforrepeat + form.testsdonerdtabfailedbutnoteligibaleforrepeat
            updateTotal.testsdonerdtabrepeat = updateTotal.testsdonerdtabrepeat + form.testsdonerdtabrepeat


            updateTotal.testsdonerdtagrun = updateTotal.testsdonerdtagrun + form.testsdonerdtagrun
            updateTotal.testsdonerdtagfailedbuteligibaleforrepeat = updateTotal.testsdonerdtagfailedbuteligibaleforrepeat + form.testsdonerdtagfailedbuteligibaleforrepeat
            updateTotal.testsdonerdtagfailedbutnoteligibaleforrepeat = updateTotal.testsdonerdtagfailedbutnoteligibaleforrepeat + form.testsdonerdtagfailedbutnoteligibaleforrepeat
            
            updateTotal.testsdonerdtagrepeat = updateTotal.testsdonerdtagrepeat + form.testsdonerdtagrepeat
            updateTotal.totaltestsdone = updateTotal.totaltestsdone + form.totaltestsdone
            updateTotal.totalrepeats = updateTotal.totalrepeats + form.totalrepeats
            updateTotal.totalpatientsrun = updateTotal.totalpatientsrun + form.totalpatientsrun

            updateTotal.errorratesabbott = updateTotal.errorratesabbott + form.errorratesabbott
            updateTotal.errorratesbmx = updateTotal.errorratesbmx + form.errorratesbmx
            updateTotal.errorratesgenexpert = updateTotal.errorratesgenexpert + form.errorratesgenexpert
            updateTotal.errorratesquantstudio3 = updateTotal.errorratesquantstudio3 + form.errorratesquantstudio3
            updateTotal.errorrateshologicpanther = updateTotal.errorrateshologicpanther + form.errorrateshologicpanther
            updateTotal.errorratesrdtab = updateTotal.errorratesrdtab + form.errorratesrdtab
            updateTotal.errorratesrdtag = updateTotal.errorratesrdtag + form.errorratesrdtag

           
            updateTotal.save()

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

            updateTotal = Specimensruncovid19.objects.get(dayofweek="Total",lab=request.user.lab,reportingweek=getReportingWeek())
            updateTotal.samplescarriedoverpreviousweeks = updateTotal.samplescarriedoverpreviousweeks + form.samplescarriedoverpreviousweeks
            updateTotal.samplesreceivedcurrentweeknasopharyngealswab = updateTotal.samplesreceivedcurrentweeknasopharyngealswab + form.samplesreceivedcurrentweeknasopharyngealswab
            updateTotal.samplesreceivedcurrentweeknasalswab = updateTotal.samplesreceivedcurrentweeknasalswab + form.samplesreceivedcurrentweeknasalswab
            updateTotal.samplesreceivedcurrentweekoropharyngealswab = updateTotal.samplesreceivedcurrentweekoropharyngealswab + form.samplesreceivedcurrentweekoropharyngealswab

            updateTotal.samplesreceivedcurrentweekmidturbinateswab = updateTotal.samplesreceivedcurrentweekmidturbinateswab + form.samplesreceivedcurrentweekmidturbinateswab
            updateTotal.samplesreceivedcurrentweeksputum = updateTotal.samplesreceivedcurrentweeksputum + form.samplesreceivedcurrentweeksputum
            updateTotal.samplesreceivedcurrentweekwholebloodorplasmaorserum = updateTotal.samplesreceivedcurrentweekwholebloodorplasmaorserum + form.samplesreceivedcurrentweekwholebloodorplasmaorserum
            updateTotal.samplesreceivedcurrentweekother = updateTotal.samplesreceivedcurrentweekother + form.samplesreceivedcurrentweekother

            updateTotal.samplesrejectedcurrentweek = updateTotal.samplesrejectedcurrentweek + form.samplesrejectedcurrentweek
            updateTotal.totalsamplesreceivedcurrentweek = updateTotal.totalsamplesreceivedcurrentweek + form.totalsamplesreceivedcurrentweek
            updateTotal.numberofsamplesenteredintolims = updateTotal.numberofsamplesenteredintolims + form.numberofsamplesenteredintolims
            updateTotal.totalsamplescurrentpluscarryover = updateTotal.totalsamplescurrentpluscarryover + form.totalsamplescurrentpluscarryover

            updateTotal.samplesreferred = updateTotal.samplesreferred + form.samplesreferred
            updateTotal.rejectionratecurrentweek = updateTotal.rejectionratecurrentweek + form.rejectionratecurrentweek
            updateTotal.numberofresultsprintedlims = updateTotal.numberofresultsprintedlims + form.numberofresultsprintedlims
            updateTotal.totalresultsdispatchedbylab = updateTotal.totalresultsdispatchedbylab + form.totalresultsdispatchedbylab
#mostt likely to crush if we keep on joining comments 
            updateTotal.comment = updateTotal.comment + form.comment
            updateTotal.samplesReferredtoName = updateTotal.samplesReferredtoName + form.samplesReferredtoName
            updateTotal.errorratesabbott = updateTotal.errorratesabbott + form.errorratesabbott
            updateTotal.errorratesabbott = updateTotal.errorratesabbott + form.errorratesabbott




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
            updateTotal.commentsregardingtestingandchallengesfacedbythelaboratory = updateTotal.commentsregardingtestingandchallengesfacedbythelaboratory + form.commentsregardingtestingandchallengesfacedbythelaboratory
            updateTotal.numberofstaffwhotestedpositivetocovid19atvllab = updateTotal.numberofstaffwhotestedpositivetocovid19atvllab + form.numberofstaffwhotestedpositivetocovid19atvllab
            updateTotal.numberOfStaffwhotestedpositivetocovid19athubs = updateTotal.numberOfStaffwhotestedpositivetocovid19athubs + form.numberOfStaffwhotestedpositivetocovid19athubs
            updateTotal.numberofstaffwhohavebeenvaccinated = updateTotal.numberofstaffwhohavebeenvaccinated + form.numberofstaffwhohavebeenvaccinated
            updateTotal.Comments = updateTotal.Comments + form.Comments
            # updateTotal.Requesttobrtifromthelaboratory = updateTotal.Requesttobrtifromthelaboratory + form.Requesttobrtifromthelaboratory
            # updateTotal.numberofstaffwhohavebeenvaccinated = updateTotal.numberofstaffwhohavebeenvaccinated + form.numberofstaffwhohavebeenvaccinated
            updateTotal.save()
            form.save()
            #return render(request, 'success.html')
    form = Generalcovid19Form()
    context = {'form': form}
    return render(request, 'masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021/general.html', context)

def labcov19machine(request):
    if request.method == 'POST':
        form = machinedowntimere
        agentstockouttoolcovid19Form(request.POST)
        if form.is_valid():
            updateTotal = machinedowntimereagentstockouttoolcovid19.objects.get(dayofweek="Total", lab=request.user.lab,reportingweek=getReportingWeek())
            updateTotal.numberofmachinebreakdownsabbott = updateTotal.numberofmachinebreakdownsabbott + form.numberofmachinebreakdownsabbott
            updateTotal.numberofmachinebreakdownsbmx = updateTotal.numberofmachinebreakdownsbmx + form.numberofmachinebreakdownsbmx
            updateTotal.numberofmachinebreakdownsgenexpert = updateTotal.numberofmachinebreakdownsgenexpert + form.numberofmachinebreakdownsgenexpert
            updateTotal.numberofmachinebreakdownsquantstudio3 = updateTotal.numberofmachinebreakdownsquantstudio3 + form.numberofmachinebreakdownsquantstudio3
           
            updateTotal.numberofmachinebreakdownshologicpanther = updateTotal.numberofmachinebreakdownshologicpanther + form.numberofmachinebreakdownshologicpanther
            updateTotal.numberofmachinebreakdownscomments = updateTotal.numberofmachinebreakdownscomments + form.numberofmachinebreakdownscomments
            updateTotal.machinedowntimedaysabbott = updateTotal.machinedowntimedaysabbott + form.machinedowntimedaysabbott
            updateTotal.machinedowntimedaysbmx = updateTotal.machinedowntimedaysbmx + form.machinedowntimedaysbmx
           
            updateTotal.machinedowntimedaysgenexpert = updateTotal.machinedowntimedaysgenexpert + form.machinedowntimedaysgenexpert
            updateTotal.machinedowntimedaysquantstudio3 = updateTotal.machinedowntimedaysquantstudio3 + form.machinedowntimedaysquantstudio3
            updateTotal.machinedowntimedayshologicpanther = updateTotal.machinedowntimedayshologicpanther + form.machinedowntimedayshologicpanther
            updateTotal.machinedowntimedayscomments = updateTotal.machinedowntimedayscomments + form.machinedowntimedayscomments
           
            updateTotal.reagentstockoutabbort = updateTotal.reagentstockoutabbort + form.reagentstockoutabbort
            updateTotal.reagentstockoutbms = updateTotal.reagentstockoutbms + form.reagentstockoutbms
            updateTotal.reagentstockoutgenexpert = updateTotal.reagentstockoutgenexpert + form.reagentstockoutgenexpert
            
            updateTotal.reagentstockoutquantstudio3 = updateTotal.reagentstockoutquantstudio3 + form.reagentstockoutquantstudio3
            updateTotal.reagentstockouthologicpanther = updateTotal.reagentstockouthologicpanther + form.reagentstockouthologicpanther
            updateTotal.reagentstockoutcomments = updateTotal.reagentstockoutcomments + form.reagentstockoutcomments
            updateTotal.reagentstockoutcomments = updateTotal.reagentstockoutcomments + form.reagentstockoutcomments

            # updateTotal.Requesttobrtifromthelaboratory = updateTotal.Requesttobrtifromthelaboratory + form.Requesttobrtifromthelaboratory
            # updateTotal.numberofstaffwhohavebeenvaccinated = updateTotal.numberofstaffwhohavebeenvaccinated + form.numberofstaffwhohavebeenvaccinated
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

#         #form.owner = str(self.request.user)
#         obj = form.save(commit=False)
#         obj.owner = str(self.request.user)
#         obj.save()
#         #form.save()
#         return redirect('127.0.0.1:8000')

