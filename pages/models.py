from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse

# Create your models here.
# ------------------------------------------------------------------------------------------------------------------------------
# brticovid19weeklystatisticstool
class specimensrunbrticovid19(models.Model):
    labchoices=[
        ('NMRL','NMRL'),
        ('Mpilo','Mpilo'),
        ('BRIDH','BRIDH'),
        ('NTBRL','NTBRL'),
        ('Gweru','Gweru'),
        ('Chinhoyi','Chinhoyi'),
        ('Masvingo','Masvingo'),
        ('eid','eid'),
        ('Victoria Falls', 'Victoria Falls'),
        ('Bindura','Bindura'),
        ('Kadoma','Kadoma'),
        ('Marondera','Marondera'),
        ('St Lukes', 'St Lukes'),
        ('Gwanda','Gwanda'),
        ('Total','Total'),
    ]

    dayofweek = models.TextField(max_length=30, choices=labchoices, default='NMRL')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

#Roche
    testsdoneabbottrun = models.IntegerField(default=0,)
    testsdoneabbottfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdoneabbottfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdoneabbottrepeat= models.IntegerField(default=0,)

# bmx
    testsdonebmxrun = models.IntegerField(default=0,)
    testsdonebmxfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonebmxfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonebmxrepeat= models.IntegerField(default=0,)

# genexpert
    testsdonegenexpertrun = models.IntegerField(default=0,)
    testsdonegenexpertfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonegenexpertfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonegenexpertrepeat= models.IntegerField(default=0,)

# quantstudio3
    testsdonequantstudio3run = models.IntegerField(default=0,)
    testsdonequantstudio3failedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonequantstudio3failedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonequantstudio3repeat= models.IntegerField(default=0,)

# hologicpanther
    testsdonehologicpantherrun = models.IntegerField(default=0,)
    testsdonehologicpantherfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonehologicpantherfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonehologicpantherrepeat= models.IntegerField(default=0,)

# RDT
    testsdonerdtabrun = models.IntegerField(default=0,)
    testsdonerdtabfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonerdtabfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonerdtabrepeat= models.IntegerField(default=0,)

    testsdonerdtagrun = models.IntegerField(default=0,)
    testsdonerdtagfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonerdtagfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonerdtagrepeat= models.IntegerField(default=0,)

    totaltestsdone = models.IntegerField(default=0,)
    totalrepeats = models.IntegerField(default=0,)
    totalpatientsrun = models.IntegerField(default=0,)

    errorratesabbott = models.IntegerField(default=0,)
    errorratesbmx = models.IntegerField(default=0,)
    errorratesgenexpert = models.IntegerField(default=0,)
    errorratesquantstudio3 = models.IntegerField(default=0,)
    errorrateshologicpanther = models.IntegerField(default=0,)
    errorratesrdtab = models.IntegerField(default=0,)
    errorratesrdtag = models.IntegerField(default=0,)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")


class specimensreceivedbrticovid19(models.Model):
    labchoices=[
        ('NMRL','NMRL'),
        ('Mpilo','Mpilo'),
        ('BRIDH','BRIDH'),
        ('NTBRL','NTBRL'),
        ('Gweru','Gweru'),
        ('Chinhoyi','Chinhoyi'),
        ('Masvingo','Masvingo'),
        ('eid','eid'),
        ('Victoria Falls', 'Victoria Falls'),
        ('Bindura','Bindura'),
        ('Kadoma','Kadoma'),
        ('Marondera','Marondera'),
        ('St Lukes', 'St Lukes'),
        ('Gwanda','Gwanda'),
        ('Total','Total'),
    ]

    dayofweek = models.TextField(max_length=30, choices=labchoices, default='NMRL')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    samplescarriedoverpreviousweeks	= models.IntegerField(default=0,)

    samplesreceivedcurrentweeknasopharyngealswab = models.IntegerField(default=0,)
    samplesreceivedcurrentweeknasalswab = models.IntegerField(default=0,)
    samplesreceivedcurrentweekoropharyngealswab = models.IntegerField(default=0,)
    samplesreceivedcurrentweekmidturbinateswab = models.IntegerField(default=0,)
    samplesreceivedcurrentweeksputum = models.IntegerField(default=0,)
    samplesreceivedcurrentweekwholebloodorplasmaorserum = models.IntegerField(default=0,)
    samplesreceivedcurrentweekother = models.IntegerField(default=0,)

    samplesrejectedcurrentweek =	models.IntegerField(default=0,)
    totalsamplesreceivedcurrentweek	=	models.IntegerField(default=0,)

    numberofsamplesenteredintolims =	models.IntegerField(default=0,)
    totalsamplescurrentpluscarryover	 =	models.IntegerField(default=0,)
    samplesreferred	=	models.IntegerField(default=0,)
    samplesreferredtoname	=	models.IntegerField(default=0,)
    rejectionratecurrentweek = models.DecimalField(decimal_places=2,  max_digits=3)
    numberofresultsprintedlims =	models.IntegerField(default=0,)
    totalresultsdispatchedbylab	=	models.IntegerField(default=0,)
    comment= models.TextField(default='.',max_length=30, null=True)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class machinedowntimereagentstockouttoolbrticovid19(models.Model):
    labchoices=[
        ('NMRL','NMRL'),
        ('Mpilo','Mpilo'),
        ('BRIDH','BRIDH'),
        ('NTBRL','NTBRL'),
        ('Gweru','Gweru'),
        ('Chinhoyi','Chinhoyi'),
        ('Masvingo','Masvingo'),
        ('eid','eid'),
        ('Victoria Falls', 'Victoria Falls'),
        ('Bindura','Bindura'),
        ('Kadoma','Kadoma'),
        ('Marondera','Marondera'),
        ('St Lukes', 'St Lukes'),
        ('Gwanda','Gwanda'),
        ('Total','Total'),
    ]

    dayofweek = models.TextField(max_length=30, choices=labchoices, default='NMRL')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    numberofmachinebreakdownsabbott = models.IntegerField(default=0,)
    numberofmachinebreakdownsbmx = models.IntegerField(default=0,)
    numberofmachinebreakdownsgenexpert = models.IntegerField(default=0,)
    numberofmachinebreakdownsquantstudio3 = models.IntegerField(default=0,)
    numberofmachinebreakdownshologicpanther = models.IntegerField(default=0,)
    numberofmachinebreakdownscomments = models.TextField()

    machinedowntimedaysabbott = models.IntegerField(default=0,)
    machinedowntimedaysbmx = models.IntegerField(default=0,)
    machinedowntimedaysgenexpert = models.IntegerField(default=0,)
    machinedowntimedaysquantstudio3 = models.IntegerField(default=0,)
    machinedowntimedayshologicpanther = models.IntegerField(default=0,)
    machinedowntimedayscomments = models.TextField()

    reagentstockoutabbort = models.IntegerField(default=0,)
    reagentstockoutbms = models.IntegerField(default=0,)
    reagentstockoutgenexpert = models.IntegerField(default=0,)
    reagentstockoutquantstudio3 = models.IntegerField(default=0,)
    reagentstockouthologicpanther = models.IntegerField(default=0,)
    reagentstockoutcomments = models.TextField()
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class generalbrticovid19(models.Model):


    dayofweek = models.TextField(max_length=30, default='brti')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    commentsregardingtestingandchallengesfacedbythelaboratory = models.TextField(default='.',max_length=30, null=True)

    numberofstaffwhotestedpositivetocovid19atvllab	= models.IntegerField(default=0,)
    numberofstaffwhohavebeenvaccinated	= models.IntegerField(default=0,)
    Comments =models.TextField( max_length=30, null=True, default='null')
    Requesttobrtifromthelaboratory	= models.TextField(default='.',max_length=30, null=True)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")





# ------------------------------------------------------------------------------------------------------------------------------
# brtivleidweeklystatisticstool

class specimensrunbrtivleid(models.Model):


    dayofweek = models.TextField(max_length=30, default='Total')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)



#Roche
    testsdonerochenumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdonerochenumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdonerochefailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonerochefailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonerocherepeatplasma= models.IntegerField(default=0,)
    testsdonerochefailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonerochenumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdonerochenumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdonerochefailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonerochefailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonerocherepeatdbs= models.IntegerField(default=0,)
    testsdonerochefailedafterrepeattestingdbs = models.IntegerField(default=0,)
#BMX
    testsdonebmxnumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdonebmxfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonebmxnumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdonebmxfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxfailedafterrepeattestingdbs = models.IntegerField(default=0,)

#Abbott
    testsdoneabbottnumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdoneabbottfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdoneabbottnumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdoneabbottfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottfailedafterrepeattestingdbs = models.IntegerField(default=0,)

#Hologic Panther
    testsdonehologicpanthernumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)

    # testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    tests2 =models.IntegerField(default=0,)


    testsdonehologicpantherfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonehologicpanthernumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)

    # testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    tests1= models.IntegerField(default=0,)


    testsdonehologicpantherfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherfailedafterrepeattestingdbs = models.IntegerField(default=0,)

    totaltestsdone = models.IntegerField(default=0,)
    totalrepeats = models.IntegerField(default=0,)
    totalpatientsrun = models.IntegerField(default=0,)
    targetsweekly = models.IntegerField(default=0,)
    percentagetargetsachievements = models.DecimalField(decimal_places=2,  max_digits=3)


    percentageerrorraterocheplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorraterochedbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorratebmxplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorratebmxdbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorrateabbottplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorrateabbottdbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorratehologicpantherplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorratehologicpantherdbs = models.DecimalField(decimal_places=2,  max_digits=3)



    totalncsfromaudit=models.TextField(max_length=30,null=True)
    ncsnotyetclosed=models.TextField(max_length=30,null=True)
    ncsclosedthisweek=models.TextField(max_length=30,null=True)
    totalncsfromaudit1=models.TextField(max_length=30,null=True)
    ncsnotyetclosed1=models.TextField(max_length=30,null=True)
    ncsclosedthisweek1=models.TextField(max_length=30,null=True)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")
    key= models.TextField(max_length=5,default="vl")




class specimensreceivedbrtivleid(models.Model):
    labchoices=[
            ('NMRL','NMRL'),
            ('Mpilo','Mpilo'),
            ('BRIDH','BRIDH'),
            ('NTBRL','NTBRL'),
            ('Gweru','Gweru'),
            ('Chinhoyi','Chinhoyi'),
            ('Masvingo','Masvingo'),
            ('eid','eid'),
            ('Victoria Falls', 'Victoria Falls'),
            ('Bindura','Bindura'),
            ('Kadoma','Kadoma'),
            ('Marondera','Marondera'),
            ('St Lukes', 'St Lukes'),
            ('Gwanda','Gwanda'),
            ('Total','Total'),
        ]

    dayofweek = models.TextField(max_length=30, choices=labchoices, default='NMRL')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    samplescarriedoverpreviousweeknevertestedplasma = models.IntegerField(default=0,)
    samplescarriedoverpreviousweeknevertesteddbs = models.IntegerField(default=0,)

    samplescarriedoverpreviouspreviousfailedsamplesplasma = models.IntegerField(default=0,)
    samplescarriedoverpreviouspreviousfailedsamplesdbs = models.IntegerField(default=0,)

    samplesreceivedcurrentweekplasma = models.IntegerField(default=0,)
    samplesreceivedcurrentweekdbs = models.IntegerField(default=0,)

    samplesrejectedcurrentweekplasma = models.IntegerField(default=0,)
    samplesrejectedcurrentweekdbs = models.IntegerField(default=0,)

    totalsamplesreceivedcurrentweekplasma = models.IntegerField(default=0,)
    totalsamplesreceivedcurrentweekdbs = models.IntegerField(default=0,)

    numberofsamplesenteredintolimsondayofarrivalplasma = models.IntegerField(default=0,)
    numberofsamplesenteredintolimsondayofarrivaldbs = models.IntegerField(default=0,)

    numberofsamplesenteredintolimsafterdayofarrivalplasma = models.IntegerField(default=0,)
    numberofsamplesenteredintolimsafterdayofarrivaldbs = models.IntegerField(default=0,)

    numberofhourslimswasfunctional = models.IntegerField(default=0,)

    totalsamplescurrentandcarryoverplasma = models.IntegerField(default=0,)
    totalsamplescurrentandcarryoverdbs = models.IntegerField(default=0,)

    samplesrefferedplasma = models.IntegerField(default=0,)
    samplesreffereddbs = models.IntegerField(default=0,)

    labsamplesrefferedto = models.IntegerField(default=0,)

    percentagerejectionrateplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentagerejectionratedbs = models.DecimalField(decimal_places=2,  max_digits=3)

    numberofresultsprintedfromlimsplasma = models.IntegerField(default=0,)
    numberofresultsprintedfromlimsdbs = models.IntegerField(default=0,)

    totalresultsdispatchedbylabplasma	= models.IntegerField(default=0,)
    totalresultsdispatchedbylabdbs	= models.IntegerField(default=0,)

    totalresultsdispatchedbylabviasmsplasma	= models.IntegerField(default=0,)
    totalresultsdispatchedbylabviasmsdbs	= models.IntegerField(default=0,)

    reasonsforrejectionssamplequalitycompromisedplasma = models.IntegerField(default=0,)
    reasonsforrejectionssamplequalitycompromiseddbs = models.IntegerField(default=0,)

    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientplasma = models.IntegerField(default=0,)
    reasons6 = models.IntegerField(default=0,)

    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientdbs = models.IntegerField(default=0,)
    reasons5= models.IntegerField(default=0,)

    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchplasma = models.IntegerField(default=0,)
    reasons2= models.IntegerField(default=0,)

    #reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchdbs = models.IntegerField(default=0,)
    reasons1= models.IntegerField(default=0,)

    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingplasma = models.IntegerField(default=0,)
    reasons4 = models.IntegerField(default=0,)

    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingdbs = models.IntegerField(default=0,)
    reason3= models.IntegerField(default=0,)


    reasonsforrejectionssamplequalitycompromisedqdacheckplasma = models.IntegerField(default=0,)
    reasonsforrejectionssamplequalitycompromisedqdacheckdbs = models.IntegerField(default=0,)

    reasonsforsamplerefferalreagentorkitstockoutplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalreagentorkitstockoutdbs= models.IntegerField(default=0,)


    reasonsforsamplerefferalinstrumentmechanicalfailureplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinstrumentmechanicalfailuredbs= models.IntegerField(default=0,)

    reasonsforsamplerefferalinsufficientinstrumentcapacityplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinsufficientinstrumentcapacitydbs= models.IntegerField(default=0,)

    reasonsforsamplerefferalinsufficienthrcapacityplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinsufficienthrcapacitydbs= models.IntegerField(default=0,)

    reasonsforsamplerefferaldqacheckplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferaldqacheckdbs= models.IntegerField(default=0,)

    comments=models.TextField("Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=30, null=True)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class reasonsforfailurebrtivleid(models.Model):
    labchoices=[
        ('NMRL','NMRL'),
        ('Mpilo','Mpilo'),
        ('BRIDH','BRIDH'),
        ('NTBRL','NTBRL'),
        ('Gweru','Gweru'),
        ('Chinhoyi','Chinhoyi'),
        ('Masvingo','Masvingo'),
        ('eid','eid'),
        ('Victoria Falls', 'Victoria Falls'),
        ('Bindura','Bindura'),
        ('Kadoma','Kadoma'),
        ('Marondera','Marondera'),
        ('St Lukes', 'St Lukes'),
        ('Gwanda','Gwanda'),
        ('Total','Total'),
    ]

    dayofweek = models.TextField(max_length=30, choices=labchoices, default='NMRL')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    #roche

    rocheplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    rochedqacheckplasma = models.IntegerField(default=0,)

    rochedbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    rochedqacheckdbs = models.IntegerField(default=0,)

#bmx

    bmxplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    bmxdqacheckplasma = models.IntegerField(default=0,)

    bmxdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    bmxdqacheckdbs = models.IntegerField(default=0,)

#abbott

    abbottplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    abbottdqacheckplasma = models.IntegerField(default=0,)

    abbottdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    abbottdqacheckdbs = models.IntegerField(default=0,)

#Hologic Panther

    hologicpantherplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    hpantherplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    hologicpantherdqacheckplasma = models.IntegerField(default=0,)

    hologicpantherdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    hologicpantherdqacheckdbs = models.IntegerField(default=0,)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")


# ------------------------------------------------------------------------------------------------------------------------------

#skip masvingo brti covid weekly





# masvingbrtivlweeklystatisticstool31-6june2021
class Specimensrecievedbrtivlweekly(models.Model):


    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    samplescarriedoverpreviousweeknevertestedplasma = models.IntegerField(default=0,)
    samplescarriedoverpreviousweeknevertesteddbs = models.IntegerField(default=0,)

    samplescarriedoverpreviouspreviousfailedsamplesplasma = models.IntegerField(default=0,)
    samplescarriedoverpreviouspreviousfailedsamplesdbs = models.IntegerField(default=0,)


    samplesreceivedcurrentweekplasma = models.IntegerField(default=0,)
    samplesreceivedcurrentweekdbs = models.IntegerField(default=0,)

    samplesrejectedcurrentweekplasma = models.IntegerField(default=0,)
    samplesrejectedcurrentweekdbs = models.IntegerField(default=0,)


    totalsamplesreceivedcurrentweekplasma = models.IntegerField(default=0,)
    totalsamplesreceivedcurrentweekdbs = models.IntegerField(default=0,)

    numberofsamplesenteredintolimsondayofarrivalplasma = models.IntegerField(default=0,)
    numberofsamplesenteredintolimsondayofarrivaldbs = models.IntegerField(default=0,)


    numberofsamplesenteredintolimsafterdayofarrivalplasma = models.IntegerField(default=0,)
    numberofsamplesenteredintolimsafterdayofarrivaldbs = models.IntegerField(default=0,)

    numberofhourslimswasfunctional = models.IntegerField(default=0,)

    totalsamplescurrentandcarryoverplasma = models.IntegerField(default=0,)
    totalsamplescurrentandcarryoverdbs = models.IntegerField(default=0,)

    samplesrefferedplasma = models.IntegerField(default=0,)
    samplesreffereddbs = models.IntegerField(default=0,)

    labsamplesrefferedto = models.IntegerField(default=0,)

    percentagerejectionrateplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentagerejectionratedbs = models.DecimalField(decimal_places=2,  max_digits=3)


    numberofresultsprintedfromlimsplasma = models.IntegerField(default=0,)
    numberofresultsprintedfromlimsdbs = models.IntegerField(default=0,)

    totalresultsdispatchedbylabplasma	= models.IntegerField(default=0,)
    totalresultsdispatchedbylabdbs	= models.IntegerField(default=0,)

    totalresultsdispatchedbylabviasmsplasma	= models.IntegerField(default=0,)
    totalresultsdispatchedbylabviasmsdbs	= models.IntegerField(default=0,)



    reasonsforrejectionssamplequalitycompromisedplasma = models.IntegerField(default=0,)
    reasonsforrejectionssamplequalitycompromiseddbs = models.IntegerField(default=0,)


    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientplasma = models.IntegerField(default=0,)
    reasons6 = models.IntegerField(default=0,)


    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientdbs = models.IntegerField(default=0,)
    reasons5 = models.IntegerField(default=0,)


    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchplasma = models.IntegerField(default=0,)
    reasons2 = models.IntegerField(default=0,)

    #reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchdbs = models.IntegerField(default=0,)
    reasons1= models.IntegerField(default=0,)


    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingplasma = models.IntegerField(default=0,)
    reasons4 = models.IntegerField(default=0,)

    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingdbs = models.IntegerField(default=0,)
    reasons3= models.IntegerField(default=0,)

    reasonsforrejectionssamplequalitycompromisedqdacheckplasma = models.IntegerField(default=0,)
    reasonsforrejectionssamplequalitycompromisedqdacheckdbs = models.IntegerField(default=0,)


    reasonsforsamplerefferalreagentorkitstockoutplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalreagentorkitstockoutdbs= models.IntegerField(default=0,)


    reasonsforsamplerefferalinstrumentmechanicalfailureplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinstrumentmechanicalfailuredbs= models.IntegerField(default=0,)

    reasonsforsamplerefferalinsufficientinstrumentcapacityplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinsufficientinstrumentcapacitydbs= models.IntegerField(default=0,)

    reasonsforsamplerefferalinsufficienthrcapacityplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinsufficienthrcapacitydbs= models.IntegerField(default=0,)

    reasonsforsamplerefferaldqacheckplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferaldqacheckdbs= models.IntegerField(default=0,)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

    comments=models.TextField("Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=30, null=True)

    # def str(self):
    #     return self.courseTitle + " (" + self.courseTitle + ")"

    # def getabsoluteurl(self):
    #     return reverse('courselist', kwargs={'pk': self.pk})

    # def gettotalunit(self):
    #     t = 0
    #     total = Course.objects.all()
    #     for i in total:
    #         t +=i
    #     return i


# class Topbrtivlweekly(models.Model):
#     reportingweek = models.TextField(default='.',max_length=30,null=False)
#     month = models.TextField(default='.',max_length=30,null=False)
#     laboratory = models.TextField(default='.',max_length=30,null=False)
#     user= models.TextField(max_length=25,default="root")
#     lab= models.TextField(max_length=30,default="brti")



class Topagesexdissagregationofallspecimensreceivedbrtivlweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    agemalelessthan15 = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfwlessthan15 = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfwlessthan15 = models.TextField(default='.',max_length=30,null=False)
    ageunknownlessthan15 = models.TextField(default='.',max_length=30,null=False)
    agetotallessthan15 = models.TextField(default='.',max_length=30,null=False)


    agemale15to19 = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfw15to19 = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfw15to19 = models.TextField(default='.',max_length=30,null=False)
    ageunknown15to19 = models.TextField(default='.',max_length=30,null=False)
    agetotal15to19 = models.TextField(default='.',max_length=30,null=False)

    agemale20to24 = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfw20to24 = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfw20to24 = models.TextField(default='.',max_length=30,null=False)
    ageunknown20to24 = models.TextField(default='.',max_length=30,null=False)
    agetotal20to24 = models.TextField(default='.',max_length=30,null=False)


    agemale25to49 = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfw25to49 = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfw25to49 = models.TextField(default='.',max_length=30,null=False)
    ageunknown25to49 = models.TextField(default='.',max_length=30,null=False)
    agetotal25to49 = models.TextField(default='.',max_length=30,null=False)

    agemale50plus = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfw50plus = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfw50plus = models.TextField(default='.',max_length=30,null=False)
    ageunknown50plus = models.TextField(default='.',max_length=30,null=False)
    agetotal50plus = models.TextField(default='.',max_length=30,null=False)


    agemaleunknown = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfwunknown = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfwunknown = models.TextField(default='.',max_length=30,null=False)
    ageunknownunknown = models.TextField(default='.',max_length=30,null=False)
    agetotalunknown = models.TextField(default='.',max_length=30,null=False)


    agemaletotals = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfwtotals = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfwtotals = models.TextField(default='.',max_length=30,null=False)
    ageunknowntotals= models.TextField(default='.',max_length=30,null=False)
    agetotaltotals = models.TextField(default='.',max_length=30,null=False)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class Top3brtivlweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    tatmediancollectiontopickupplasmahrs = models.TextField(default='.',max_length=30,null=False)
    tatmedianspecimenhubtovllabplasmadays = models.TextField(default='.',max_length=30,null=False)
    tatmedianintralabplasmadays = models.TextField(default='.',max_length=30,null=False)
    tatmedianresultsvllabtohubplasmadays = models.TextField(default='.',max_length=30,null=False)
    tatmedianresultshubtoclinicplasmadays = models.TextField(default='.',max_length=30,null=False)

    tatmediancollectiontopickupdbshrs = models.TextField(default='.',max_length=30,null=False)
    tatmedianspecimenhubtovllabdbsdays = models.TextField(default='.',max_length=30,null=False)
    tatmedianintralabdbsdays = models.TextField(default='.',max_length=30,null=False)
    tatmedianresultsvllabtohubdbsdays = models.TextField(default='.',max_length=30,null=False)
    tatmedianresultshubtoclinicdbsdays = models.TextField(default='.',max_length=30,null=False)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class Top4brtivlweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    machinenumberofmachinebreakdownsroche = models.TextField(default='.',max_length=30,null=False)
    machinenumberofmachinebreakdownsabbott = models.TextField(default='.',max_length=30,null=False)
    machinenumberofmachinebreakdownshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinenumberofmachinebreakdownsbmx = models.TextField(default='.',max_length=30,null=False)

    machinereasonsroche = models.TextField(default='.',max_length=30,null=False)
    machinereasonsabbott = models.TextField(default='.',max_length=30,null=False)
    machinereasonshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinereasonsbmx = models.TextField(default='.',max_length=30,null=False)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")


class Top5brtivlweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    machinedowntimedaysroche = models.TextField(default='.',max_length=30,null=False)
    machinereasonsroche = models.TextField(default='.',max_length=30,null=False)
    machinetimetakenfordowntimetoberesolvedroche = models.TextField(default='.',max_length=30,null=False)

    machinedowntimedaysabbott = models.TextField(default='.',max_length=30,null=False)
    machinereasonsabbott = models.TextField(default='.',max_length=30,null=False)
    machinetimetakenfordowntimetoberesolvedabbott = models.TextField(default='.',max_length=30,null=False)

    machinedowntimedayshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinereasonshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinetimetakenfordowntimetoberesolvedhologicpanther = models.TextField(default='.',max_length=30,null=False)

    machinedowntimedaysbmx = models.TextField(default='.',max_length=30,null=False)
    machinereasonsbmx = models.TextField(default='.',max_length=30,null=False)
    machinetimetakenfordowntimetoberesolvedbmx = models.TextField(default='.',max_length=30,null=False)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")



class Top6brtivlweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    machinestockoutdaysroche = models.TextField(default='.',max_length=30,null=False)
    machinereasonsroche = models.TextField(default='.',max_length=30,null=False)

    machinestockoutdaysabbott = models.TextField(default='.',max_length=30,null=False)
    machinereasonsabbott = models.TextField(default='.',max_length=30,null=False)

    machinestockoutdayshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinereasonshologicpanther = models.TextField(default='.',max_length=30,null=False)


    machinestockoutdaysbmx = models.TextField(default='.',max_length=30,null=False)
    machinereasonsbmx = models.TextField(default='.',max_length=30,null=False)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class Top7brtivlweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)

    reagenttestsloanedouttootherlabsreagentloanedtowhichlabroche = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromotherlabsroche = models.TextField(default='.',max_length=30,null=False)
    reagent5= models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromwhichlabsroche = models.TextField(default='.',max_length=30,null=False)
    reagent9= models.TextField(default='.',max_length=30,null=False)


    reagenttestsloanedouttootherlabsstockonhandroche = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabstestsavailableroche = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabsmonthsofstockroche = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabstestsexpiredthismonthbeforeuseroche = models.TextField(default='.',max_length=30,null=False)
    reagent13= models.TextField(default='.',max_length=30,null=False)


    reagenttestsloanedouttootherlabsreagentloanedtowhichlababbott = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromotherlabsabbott = models.TextField(default='.',max_length=30,null=False)
    reagent2  = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromwhichlabsabbott = models.TextField(default='.',max_length=30,null=False)

    reagent6 = models.TextField(default='.',max_length=30,null=False)

    reagenttestsloanedouttootherlabsstockonhandabbott = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabstestsavailableabbott = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabsmonthsofstockabbott = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabstestsexpiredthismonthbeforeuseabbott = models.TextField(default='.',max_length=30,null=False)
    reagent10  = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentloanedtowhichlabhologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagent1 = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromotherlabshologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagent4 = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromwhichlabshologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagent8 = models.TextField(default='.',max_length=30,null=False)


    reagenttestsloanedouttootherlabsstockonhandhologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabstestsavailablehologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabsmonthsofstockhologicpanther = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabstestsexpiredthismonthbeforeusehologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagent12 = models.TextField(default='.',max_length=30,null=False)


    reagenttestsloanedouttootherlabsreagentloanedtowhichlabbmx = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromotherlabsbmx = models.TextField(default='.',max_length=30,null=False)
    reagent3 = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromwhichlabsbmx = models.TextField(default='.',max_length=30,null=False)
    reagent7= models.TextField(default='.',max_length=30,null=False)



    reagenttestsloanedouttootherlabsstockonhandbmx = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabstestsavailablebmx = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabsmonthsofstockbmx = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabstestsexpiredthismonthbeforeusebmx = models.TextField(default='.',max_length=30,null=False)
    reagent11 = models.TextField(default='.',max_length=30,null=False)


    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")






class Specimensrunbrtivlweekly(models.Model):

    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)



#Roche
    testsdonerochenumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdonerochenumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdonerochefailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonerochefailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonerocherepeatplasma= models.IntegerField(default=0,)
    testsdonerochefailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonerochenumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdonerochenumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdonerochefailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonerochefailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonerocherepeatdbs= models.IntegerField(default=0,)
    testsdonerochefailedafterrepeattestingdbs = models.IntegerField(default=0,)
#BMX
    testsdonebmxnumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdonebmxfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonebmxnumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdonebmxfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxfailedafterrepeattestingdbs = models.IntegerField(default=0,)

#Abbott
    testsdoneabbottnumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdoneabbottfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdoneabbottnumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdoneabbottfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottfailedafterrepeattestingdbs = models.IntegerField(default=0,)

#Hologic Panther
    testsdonehologicpanthernumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)


    # testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    tests2 =models.IntegerField(default=0,)

    testsdonehologicpantherfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonehologicpanthernumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)

    # testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    tests1= models.IntegerField(default=0,)

    testsdonehologicpantherfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherfailedafterrepeattestingdbs = models.IntegerField(default=0,)

    totaltestsdone = models.IntegerField(default=0,)
    totalrepeats = models.IntegerField(default=0,)
    totalpatientsrun = models.IntegerField(default=0,)
    targetsweekly = models.IntegerField(default=0,)
    percentagetargetsachievements = models.DecimalField(decimal_places=2,  max_digits=3)


    percentageerrorraterocheplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorraterochedbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorratebmxplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorratebmxdbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorrateabbottplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorrateabbottdbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorratehologicpantherplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorratehologicpantherdbs = models.DecimalField(decimal_places=2,  max_digits=3)


    totalncsfromaudit=models.TextField(max_length=30,null=True)
    ncsnotyetclosed=models.TextField(max_length=30,null=True)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")
    key= models.TextField(max_length=30,default="vl")



class Electricoutagebrtivlweekly(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)


    numberofhourswithnoelectricityperday	= models.IntegerField(default=0,)
    numberofhoursgeneratorwasonperday	= models.IntegerField(default=0,)
    litresoffueladdedtogeneratorperday	= models.IntegerField(default=0,)
    numberofhoursmachineswasnotbeingusedduetopowercutperday	= models.IntegerField(default=0,)
    totaltestsdoneperdayusinggenerator	= models.IntegerField(default=0,)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")









class Reasonsforfailurebrtivlweekly(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]



    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

#roche
    rocheplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    rochedqacheckplasma = models.IntegerField(default=0,)

    rochedbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    rochedqacheckdbs = models.IntegerField(default=0,)

#bmx

    bmxplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    bmxdqacheckplasma = models.IntegerField(default=0,)

    bmxdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    bmxdqacheckdbs = models.IntegerField(default=0,)



#abbott

    abbottplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    abbottdqacheckplasma = models.IntegerField(default=0,)

    abbottdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    abbottdqacheckdbs = models.IntegerField(default=0,)




#Hologic Panther

    hologicpantherplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    hpantherplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    hologicpantherdqacheckplasma = models.IntegerField(default=0,)

    hologicpantherdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    hologicpantherdqacheckdbs = models.IntegerField(default=0,)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")













#-----------------------------------------------------------lab cov 19--------------------------------------------------------------------------



#General Info masvingo brticovid19weeklystatisticstool


class Topagesexdissagregationofallspecimensreceivedcovid19(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    machinenumberofmachinebreakdownsabbott = models.TextField(default='.',max_length=30)
    machinereasonsabbott = models.TextField(default='.',max_length=30)
    machinedowntimedaysabbott = models.TextField(default='.',max_length=30)
    machinereasons2abbott = models.TextField(default='.',max_length=30)
    machinestockoutdaysabbott = models.TextField(default='.',max_length=30)
    machinereasons3abbott = models.TextField(default='.',max_length=30)

    machinenumberofmachinebreakdownsgenexpert = models.TextField(default='.',max_length=30)
    machinereasonsgenexpert = models.TextField(default='.',max_length=30)
    machinedowntimedaysgenexpert = models.TextField(default='.',max_length=30)
    machinereasons2genexpert = models.TextField(default='.',max_length=30)
    machinestockoutdaysgenexpert = models.TextField(default='.',max_length=30)
    machinereasons3genexpert = models.TextField(default='.',max_length=30)

    machinenumberofmachinebreakdownsroche = models.TextField(default='.',max_length=30)
    machinereasonsroche = models.TextField(default='.',max_length=30)
    machinedowntimedaysroche = models.TextField(default='.',max_length=30)
    machinereasons2roche = models.TextField(default='.',max_length=30)
    machinestockoutdaysroche = models.TextField(default='.',max_length=30)
    machinereasons3roche = models.TextField(default='.',max_length=30)

    machinenumberofmachinebreakdownsbmx = models.TextField(default='.',max_length=30)
    machinereasonsbmx = models.TextField(default='.',max_length=30)
    machinedowntimedaysbmx = models.TextField(default='.',max_length=30)
    machinereasons2bmx = models.TextField(default='.',max_length=30)
    machinestockoutdaysbmx = models.TextField(default='.',max_length=30)
    machinereasons3bmx = models.TextField(default='.',max_length=30)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class Top3covid19(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    numberofdaystat1 = models.TextField(default='.',max_length=30)
    numberofdaystat2 = models.TextField(default='.',max_length=30)
    numberofdaystat3 = models.TextField(default='.',max_length=30)
    numberofdaystattotal = models.TextField(default='.',max_length=30)

    numberofcompletedtransmittalsheetreceived = models.TextField(default='.',max_length=30)


    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class machinedowntimereagentstockouttoolcovid19(models.Model):
    labchoices=[
        ('NMRL','NMRL'),
        ('Mpilo','Mpilo'),
        ('BRIDH','BRIDH'),
        ('NTBRL','NTBRL'),
        ('Gweru','Gweru'),
        ('Chinhoyi','Chinhoyi'),
        ('Masvingo','Masvingo'),
        ('eid','eid'),
        ('Victoria Falls', 'Victoria Falls'),
        ('Bindura','Bindura'),
        ('Kadoma','Kadoma'),
        ('Marondera','Marondera'),
        ('St Lukes', 'St Lukes'),
        ('Gwanda','Gwanda'),
        ('Total','Total'),
    ]

    dayofweek = models.TextField(max_length=30, choices=labchoices, default='NMRL')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    numberofmachinebreakdownsabbott = models.IntegerField(default=0,)
    numberofmachinebreakdownsbmx = models.IntegerField(default=0,)
    numberofmachinebreakdownsgenexpert = models.IntegerField(default=0,)
    numberofmachinebreakdownsquantstudio3 = models.IntegerField(default=0,)
    numberofmachinebreakdownshologicpanther = models.IntegerField(default=0,)
    numberofmachinebreakdownscomments = models.TextField()

    machinedowntimedaysabbott = models.IntegerField(default=0,)
    machinedowntimedaysbmx = models.IntegerField(default=0,)
    machinedowntimedaysgenexpert = models.IntegerField(default=0,)
    machinedowntimedaysquantstudio3 = models.IntegerField(default=0,)
    machinedowntimedayshologicpanther = models.IntegerField(default=0,)
    machinedowntimedayscomments = models.TextField()

    reagentstockoutabbort = models.IntegerField(default=0,)
    reagentstockoutbms = models.IntegerField(default=0,)
    reagentstockoutgenexpert = models.IntegerField(default=0,)
    reagentstockoutquantstudio3 = models.IntegerField(default=0,)
    reagentstockouthologicpanther = models.IntegerField(default=0,)
    reagentstockoutcomments = models.TextField()
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")


class Generalcovid19(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
        ('Total','Total'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    commentsregardingtestingandchallengesfacedbythelaboratory = models.TextField(default='.',max_length=30, null=True)
    numberofstaffwhotestedpositivetocovid19atvllab	= models.IntegerField(default=0,)
    numberOfStaffwhotestedpositivetocovid19athubs= models.IntegerField(default=0,)
    numberofstaffwhohavebeenvaccinated	= models.IntegerField(default=0,)
    Comments =models.TextField( max_length=3000, null=True, default='null')
    Requesttobrtifromthelaboratory	= models.TextField(default='.',max_length=3000, null=True)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

#another


class Specimensreceivedcovid19(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
        ('Total','Total'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    samplescarriedoverpreviousweeks	= models.IntegerField(default=0,)

    samplesreceivedcurrentweeknasopharyngealswab = models.IntegerField(default=0,)
    samplesreceivedcurrentweeknasalswab = models.IntegerField(default=0,)
    samplesreceivedcurrentweekoropharyngealswab = models.IntegerField(default=0,)
    samplesreceivedcurrentweekmidturbinateswab = models.IntegerField(default=0,)
    samplesreceivedcurrentweeksputum = models.IntegerField(default=0,)
    samplesreceivedcurrentweekwholebloodorplasmaorserum = models.IntegerField(default=0,)
    samplesreceivedcurrentweekother = models.IntegerField(default=0,)

    samplesrejectedcurrentweek =	models.IntegerField(default=0,)
    totalsamplesreceivedcurrentweek	=	models.IntegerField(default=0,)

    numberofsamplesenteredintolims =	models.IntegerField(default=0,)
    totalsamplescurrentpluscarryover	 =	models.IntegerField(default=0,)
    samplesreferred	=	models.IntegerField(default=0,)
    rejectionratecurrentweek = models.DecimalField(decimal_places=2,  max_digits=5)
    numberofresultsprintedlims =	models.IntegerField(default=0,)
    totalresultsdispatchedbylab	=	models.IntegerField(default=0,)
    comment= models.TextField(default='.',max_length=300, null=True)
    samplesReferredtoName = models.TextField(max_length=300, default="null")
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")





class Specimensruncovid19(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
        ('Total','Total'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    testsdoneabbottrun = models.IntegerField(default=0,)
    testsdoneabbottfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdoneabbottfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdoneabbottrepeat= models.IntegerField(default=0,)


    testsdonebmxrun = models.IntegerField(default=0,)
    testsdonebmxfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonebmxfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonebmxrepeat= models.IntegerField(default=0,)

    # genexpert
    testsdonegenexpertrun = models.IntegerField(default=0,)
    testsdonegenexpertfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonegenexpertfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonegenexpertrepeat= models.IntegerField(default=0,)
# quantstudio3
    testsdonequantstudio3run = models.IntegerField(default=0,)
    testsdonequantstudio3failedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonequantstudio3failedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonequantstudio3repeat= models.IntegerField(default=0,)
# hologicpanther
    testsdonehologicpantherrun = models.IntegerField(default=0,)
    testsdonehologicpantherfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonehologicpantherfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonehologicpantherrepeat= models.IntegerField(default=0,)
# RDT
    testsdonerdtabrun = models.IntegerField(default=0,)
    testsdonerdtabfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonerdtabfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonerdtabrepeat= models.IntegerField(default=0,)

    testsdonerdtagrun = models.IntegerField(default=0,)
    testsdonerdtagfailedbuteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonerdtagfailedbutnoteligibaleforrepeat= models.IntegerField(default=0,)
    testsdonerdtagrepeat= models.IntegerField(default=0,)


    totaltestsdone = models.IntegerField(default=0,)
    totalrepeats = models.IntegerField(default=0,)
    totalpatientsrun = models.IntegerField(default=0,)


    errorratesabbott = models.IntegerField(default=0,)
    errorratesbmx = models.IntegerField(default=0,)
    errorratesgenexpert = models.IntegerField(default=0,)
    errorratesquantstudio3 = models.IntegerField(default=0,)
    errorrateshologicpanther = models.IntegerField(default=0,)
    errorratesrdtab = models.IntegerField(default=0,)
    errorratesrdtag = models.IntegerField(default=0,)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

 # ----------------------------------------------------------------------------------------------------------------------------------

#masvingbrtiweeklystatisticstool31-6june2021


# class Topbrtiweekly(models.Model):
#     reportingweek = models.TextField(default='.',max_length=30,null=False)
#     month = models.TextField(default='.',max_length=30,null=False)
#     laboratory = models.TextField(default='.',max_length=30,null=False)
#     user= models.TextField(max_length=25,default="root")
#     lab= models.TextField(max_length=30,default="brti")


class Topagesexdissagregationofallspecimensreceivedbrtiweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    agemalelessthan15 = models.TextField(default='.',max_length=5,null=False)
    agefemalenonpbfwlessthan15 = models.TextField(default='.',max_length=5,null=False)
    agefemalepbfwlessthan15 = models.TextField(default='.',max_length=5,null=False)
    ageunknownlessthan15 = models.TextField(default='.',max_length=5,null=False)
    agetotallessthan15 = models.TextField(default='.',max_length=5,null=False)


    agemale15to19 = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfw15to19 = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfw15to19 = models.TextField(default='.',max_length=30,null=False)
    ageunknown15to19 = models.TextField(default='.',max_length=30,null=False)
    agetotal15to19 = models.TextField(default='.',max_length=30,null=False)

    agemale20to24 = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfw20to24 = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfw20to24 = models.TextField(default='.',max_length=30,null=False)
    ageunknown20to24 = models.TextField(default='.',max_length=30,null=False)
    agetotal20to24 = models.TextField(default='.',max_length=30,null=False)


    agemale25to49 = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfw25to49 = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfw25to49 = models.TextField(default='.',max_length=30,null=False)
    ageunknown25to49 = models.TextField(default='.',max_length=30,null=False)
    agetotal25to49 = models.TextField(default='.',max_length=30,null=False)

    agemale50plus = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfw50plus = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfw50plus = models.TextField(default='.',max_length=30,null=False)
    ageunknown50plus = models.TextField(default='.',max_length=30,null=False)
    agetotal50plus = models.TextField(default='.',max_length=30,null=False)


    agemaleunknown = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfwunknown = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfwunknown = models.TextField(default='.',max_length=30,null=False)
    ageunknownunknown = models.TextField(default='.',max_length=30,null=False)
    agetotalunknown = models.TextField(default='.',max_length=30,null=False)


    agemaletotals = models.TextField(default='.',max_length=30,null=False)
    agefemalenonpbfwtotals = models.TextField(default='.',max_length=30,null=False)
    agefemalepbfwtotals = models.TextField(default='.',max_length=30,null=False)
    ageunknowntotals= models.TextField(default='.',max_length=30,null=False)
    agetotaltotals = models.TextField(default='.',max_length=30,null=False)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")


class Top3brtiweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    tatmediancollectiontopickupplasmahrs = models.TextField(default='.',max_length=30,null=False)
    tatmedianspecimenhubtovllabplasmadays = models.TextField(default='.',max_length=30,null=False)
    tatmedianintralabplasmadays = models.TextField(default='.',max_length=30,null=False)
    tatmedianresultsvllabtohubplasmadays = models.TextField(default='.',max_length=30,null=False)
    tatmedianresultshubtoclinicplasmadays = models.TextField(default='.',max_length=30,null=False)

    tatmediancollectiontopickupdbshrs = models.TextField(default='.',max_length=30,null=False)
    tatmedianspecimenhubtovllabdbsdays = models.TextField(default='.',max_length=30,null=False)
    tatmedianintralabdbsdays = models.TextField(default='.',max_length=30,null=False)
    tatmedianresultsvllabtohubdbsdays = models.TextField(default='.',max_length=30,null=False)
    tatmedianresultshubtoclinicdbsdays = models.TextField(default='.',max_length=30,null=False)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")



class Top4brtiweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    machinenumberofmachinebreakdownsroche = models.TextField(default='.',max_length=30,null=False)
    machinenumberofmachinebreakdownsabbott = models.TextField(default='.',max_length=30,null=False)
    machinenumberofmachinebreakdownshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinenumberofmachinebreakdownsbmx = models.TextField(default='.',max_length=30,null=False)

    machinereasonsroche = models.TextField(default='.',max_length=30,null=False)
    machinereasonsabbott = models.TextField(default='.',max_length=30,null=False)
    machinereasonshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinereasonsbmx = models.TextField(default='.',max_length=30,null=False)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")

class Top5brtiweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    machinedowntimedaysroche = models.TextField(default='.',max_length=30,null=False)
    machinereasonsroche = models.TextField(default='.',max_length=30,null=False)
    machinetimetakenfordowntimetoberesolvedroche = models.TextField(default='.',max_length=30,null=False)

    machinedowntimedaysabbott = models.TextField(default='.',max_length=30,null=False)
    machinereasonsabbott = models.TextField(default='.',max_length=30,null=False)
    machinetimetakenfordowntimetoberesolvedabbott = models.TextField(default='.',max_length=30,null=False)

    machinedowntimedayshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinereasonshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinetimetakenfordowntimetoberesolvedhologicpanther = models.TextField(default='.',max_length=30,null=False)

    machinedowntimedaysbmx = models.TextField(default='.',max_length=30,null=False)
    machinereasonsbmx = models.TextField(default='.',max_length=30,null=False)
    machinetimetakenfordowntimetoberesolvedbmx = models.TextField(default='.',max_length=30,null=False)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")


class Top6brtiweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    machinestockoutdaysroche = models.TextField(default='.',max_length=30,null=False)
    machinereasonsroche = models.TextField(default='.',max_length=30,null=False)

    machinestockoutdaysabbott = models.TextField(default='.',max_length=30,null=False)
    machinereasonsabbott = models.TextField(default='.',max_length=30,null=False)

    machinestockoutdayshologicpanther = models.TextField(default='.',max_length=30,null=False)
    machinereasonshologicpanther = models.TextField(default='.',max_length=30,null=False)


    machinestockoutdaysbmx = models.TextField(default='.',max_length=30,null=False)
    machinereasonsbmx = models.TextField(default='.',max_length=30,null=False)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")



class Top61brtiweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    machineamountofliquidwasteroche = models.TextField(default='.',max_length=30,null=False)
    machineamountofliquidwasteabbott = models.TextField(default='.',max_length=30,null=False)
    machineamountofliquidwastehologicpanther = models.TextField(default='.',max_length=30,null=False)
    machineamountofliquidwastebmx = models.TextField(default='.',max_length=30,null=False)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")


class Top7brtiweekly(models.Model):
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    reagenttestsloanedouttootherlabsreagentloanedtowhichlabroche = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromotherlabsroche = models.TextField(default='.',max_length=30,null=False)
    reagent5 = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromwhichlabsroche = models.TextField(default='.',max_length=30,null=False)
    reagent9= models.TextField(default='.',max_length=30,null=False)


    reagenttestsloanedouttootherlabsstockonhandroche = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabstestsavailableroche = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabsmonthsofstockroche = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabstestsexpiredthismonthbeforeuseroche = models.TextField(default='.',max_length=30,null=False)
    reagent13= models.TextField(default='.',max_length=30,null=False)


    reagenttestsloanedouttootherlabsreagentloanedtowhichlababbott = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromotherlabsabbott = models.TextField(default='.',max_length=30,null=False)
    reagent2  = models.TextField(default='.',max_length=30,null=False)



    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromwhichlabsabbott = models.TextField(default='.',max_length=30,null=False)
    reagent6 = models.TextField(default='.',max_length=30,null=False)



    reagenttestsloanedouttootherlabsstockonhandabbott = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabstestsavailableabbott = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabsmonthsofstockabbott = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabstestsexpiredthismonthbeforeuseabbott = models.TextField(default='.',max_length=30,null=False)
    reagent10  = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabsreagentloanedtowhichlabhologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagent1= models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromotherlabshologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagent4 = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromwhichlabshologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagent8= models.TextField(default='.',max_length=30,null=False)


    reagenttestsloanedouttootherlabsstockonhandhologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabstestsavailablehologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabsmonthsofstockhologicpanther = models.TextField(default='.',max_length=30,null=False)


    # reagenttestsloanedouttootherlabstestsexpiredthismonthbeforeusehologicpanther = models.TextField(default='.',max_length=30,null=False)
    reagent12 = models.TextField(default='.',max_length=30,null=False)

    reagenttestsloanedouttootherlabsreagentloanedtowhichlabbmx = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromotherlabsbmx = models.TextField(default='.',max_length=30,null=False)
    reagent3 = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabsreagentreceivedonloanfromwhichlabsbmx = models.TextField(default='.',max_length=30,null=False)
    reagent7= models.TextField(default='.',max_length=30,null=False)


    reagenttestsloanedouttootherlabsstockonhandbmx = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabstestsavailablebmx = models.TextField(default='.',max_length=30,null=False)
    reagenttestsloanedouttootherlabsmonthsofstockbmx = models.TextField(default='.',max_length=30,null=False)

    # reagenttestsloanedouttootherlabstestsexpiredthismonthbeforeusebmx = models.TextField(default='.',max_length=30,null=False)
    reagent11 = models.TextField(default='.',max_length=30,null=False)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")





class Specimensrunbrtiweekly(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)



#Roche
    testsdonerochenumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdonerochenumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdonerochefailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonerochefailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonerocherepeatplasma= models.IntegerField(default=0,)
    testsdonerochefailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonerochenumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdonerochenumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdonerochefailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonerochefailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonerocherepeatdbs= models.IntegerField(default=0,)
    testsdonerochefailedafterrepeattestingdbs = models.IntegerField(default=0,)
#BMX
    testsdonebmxnumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdonebmxfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxrepeatplasma= models.IntegerField(default=0,)
    testsdonebmxfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonebmxnumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdonebmxfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxrepeatdbs= models.IntegerField(default=0,)
    testsdonebmxfailedafterrepeattestingdbs = models.IntegerField(default=0,)

#Abbott
    testsdoneabbottnumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    testsdoneabbottfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottrepeatplasma= models.IntegerField(default=0,)
    testsdoneabbottfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdoneabbottnumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    testsdoneabbottfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottrepeatdbs= models.IntegerField(default=0,)
    testsdoneabbottfailedafterrepeattestingdbs = models.IntegerField(default=0,)

#Hologic Panther
    testsdonehologicpanthernumberofsamplesreceivedthisweekplasma = models.IntegerField(default=0,)

    # testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksplasma = models.IntegerField(default=0,)
    tests2 =models.IntegerField(default=0,)

    testsdonehologicpantherfailedbuteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherrepeatplasma= models.IntegerField(default=0,)
    testsdonehologicpantherfailedafterrepeattestingplasma = models.IntegerField(default=0,)


    testsdonehologicpanthernumberofsamplesreceivedthisweekdbs = models.IntegerField(default=0,)

    # testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksdbs = models.IntegerField(default=0,)
    tests1= models.IntegerField(default=0,)


    testsdonehologicpantherfailedbuteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherrepeatdbs= models.IntegerField(default=0,)
    testsdonehologicpantherfailedafterrepeattestingdbs = models.IntegerField(default=0,)

    totaltestsdone = models.IntegerField(default=0,)
    totalrepeats = models.IntegerField(default=0,)
    totalpatientsrun = models.IntegerField(default=0,)
    targetsweekly = models.IntegerField(default=0,)
    percentagetargetsachievements = models.DecimalField(decimal_places=2,  max_digits=3)


    percentageerrorraterocheplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorraterochedbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorratebmxplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorratebmxdbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorrateabbottplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorrateabbottdbs = models.DecimalField(decimal_places=2,  max_digits=3)

    percentageerrorratehologicpantherplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentageerrorratehologicpantherdbs = models.DecimalField(decimal_places=2,  max_digits=3)


    totalncsfromaudit=models.TextField(max_length=30,null=True)
    ncsnotyetclosed=models.TextField(max_length=30,null=True)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")



class Specimensreceivedbrtiweekly(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

    samplescarriedoverpreviousweeksnevertestedplasma = models.IntegerField(default=0,)
    samplescarriedoverpreviousweeksnevertesteddbs = models.IntegerField(default=0,)

    samplescarriedoverpreviousfailedsamplesplasma = models.IntegerField(default=0,)
    samplescarriedoverpreviousfailedsamplesdbs = models.IntegerField(default=0,)



    samplesreceivedcurrentweekplasma = models.IntegerField(default=0,)
    samplesreceivedcurrentweekdbs = models.IntegerField(default=0,)

    samplesrejectedcurrentweekplasma = models.IntegerField(default=0,)
    samplesrejectedcurrentweekdbs = models.IntegerField(default=0,)

    totalsamplesreceivedcurrentweekplasma = models.IntegerField(default=0,)
    totalsamplesreceivedcurrentweekdbs = models.IntegerField(default=0,)

    numberofsamplesenteredintolimsondayofarrivalplasma = models.IntegerField(default=0,)
    numberofsamplesenteredintolimsondayofarrivaldbs = models.IntegerField(default=0,)

    numberofsamplesenteredintolimsafterdayofarrivalplasma = models.IntegerField(default=0,)
    numberofsamplesenteredintolimsafterdayofarrivaldbs = models.IntegerField(default=0,)

    numberofhourslimswasfunctional	 = models.IntegerField(default=0,)

    totalsamplescurrentpluscarryoverplasma= models.IntegerField(default=0,)
    totalsamplescurrentpluscarryoverdbs= models.IntegerField(default=0,)

    samplesrefferedplasma = models.IntegerField(default=0,)
    samplesreffereddbs = models.IntegerField(default=0,)

    labsamplesrefferedto = models.IntegerField(default=0,)

    percentagerejectionrateplasma = models.DecimalField(decimal_places=2,  max_digits=3)
    percentagerejectionratedbs = models.DecimalField(decimal_places=2,  max_digits=3)


    numberofresultsprintedfromlimsplasma = models.IntegerField(default=0,)
    numberofresultsprintedfromlimsdbs = models.IntegerField(default=0,)

    totalresultsdispatchedbylabplasma	= models.IntegerField(default=0,)
    totalresultsdispatchedbylabdbs	= models.IntegerField(default=0,)

    totalresultsdispatchedbylabviasmsplasma	= models.IntegerField(default=0,)
    totalresultsdispatchedbylabviasmsdbs	= models.IntegerField(default=0,)



    reasonsforrejectionssamplequalitycompromisedplasma = models.IntegerField(default=0,)
    reasonsforrejectionssamplequalitycompromiseddbs = models.IntegerField(default=0,)


    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientplasma = models.IntegerField(default=0,)
    reasons6 = models.IntegerField(default=0,)



    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientdbs = models.IntegerField(default=0,)
    reasons5 = models.IntegerField(default=0,)


    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchplasma = models.IntegerField(default=0,)
    reasons2= models.IntegerField(default=0,)

    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchdbs = models.IntegerField(default=0,)
    reasons1= models.IntegerField(default=0,)



    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingplasma = models.IntegerField(default=0,)
    reasons4 = models.IntegerField(default=0,)

    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingdbs = models.IntegerField(default=0,)
    reasons3= models.IntegerField(default=0,)

    reasonsforrejectionssamplequalitycompromisedqdacheckplasma = models.IntegerField(default=0,)
    reasonsforrejectionssamplequalitycompromisedqdacheckdbs = models.IntegerField(default=0,)


    reasonsforsamplerefferalreagentorkitstockoutplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalreagentorkitstockoutdbs= models.IntegerField(default=0,)


    reasonsforsamplerefferalinstrumentmechanicalfailureplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinstrumentmechanicalfailuredbs= models.IntegerField(default=0,)

    reasonsforsamplerefferalinsufficientinstrumentcapacityplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinsufficientinstrumentcapacitydbs= models.IntegerField(default=0,)

    reasonsforsamplerefferalinsufficienthrcapacityplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferalinsufficienthrcapacitydbs= models.IntegerField(default=0,)

    reasonsforsamplerefferaldqacheckplasma= models.IntegerField(default=0,)
    reasonsforsamplerefferaldqacheckdbs= models.IntegerField(default=0,)

    comments=models.TextField("Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=30, null=True)
    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")



class Reasonsforfailurebrtiweekly(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)

#roche
    rocheplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    rocheplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    rochedqacheckplasma = models.IntegerField(default=0,)

    rochedbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    rochedbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    rochedqacheckdbs = models.IntegerField(default=0,)

#bmx

    bmxplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    bmxplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    bmxdqacheckplasma = models.IntegerField(default=0,)

    bmxdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    bmxdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    bmxdqacheckdbs = models.IntegerField(default=0,)



#abbott

    abbottplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    abbottplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    abbottdqacheckplasma = models.IntegerField(default=0,)

    abbottdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    abbottdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    abbottdqacheckdbs = models.IntegerField(default=0,)




#Hologic Panther

    hologicpantherplasmanumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    hpantherplasmanumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    hologicpantherplasmanumberoffailedtestsduetoother = models.IntegerField(default=0,)
    hologicpantherdqacheckplasma = models.IntegerField(default=0,)

    hologicpantherdbsnumberoffailedtestsduetosamplequalityissues = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoreagentqualityissues = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoduetoqcfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetopowerfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetomechanicalfailure = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoprocessingerror = models.IntegerField(default=0,)
    hologicpantherdbsnumberoffailedtestsduetoother = models.IntegerField(default=0,)
    hologicpantherdqacheckdbs = models.IntegerField(default=0,)

    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")


class Electricoutagebrtiweekly(models.Model):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = models.TextField(max_length=30, choices=dayschoices, default='Monday')
    reportingweek = models.TextField(default='.',max_length=30,null=False)
    dateofrecord = models.DateField(auto_now=True)


    numberofhourswithnoelectricityperday	= models.IntegerField(default=0,)
    numberofhoursgeneratorwasonperday	= models.IntegerField(default=0,)
    litresoffueladdedtogeneratorperday	= models.IntegerField(default=0,)
    numberofhoursmachineswasnotbeingusedduetopowercutperday	= models.IntegerField(default=0,)
    totaltestsdoneperdayusinggenerator	= models.IntegerField(default=0,)



    user= models.TextField(max_length=25,default="root")
    lab= models.TextField(max_length=30,default="brti")
#top.html not done




# masvingobrticovid19weeklystatisticstool31-6June2021




















