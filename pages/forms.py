from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
import datetime






# ------------------------------------------------------------------------------------------------------------------------------
# brticovid19weeklystatisticstool

class specimensreceivedbrticovid19Form(forms.ModelForm):

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

    dayofweek = forms.ChoiceField(choices=labchoices, initial="none", label="Select laboratory please" )
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")

    samplescarriedoverpreviousweeks	= forms.IntegerField(label="Samples Carried Over (Previous Weeks(s))")

    samplesreceivedcurrentweeknasopharyngealswab = forms.IntegerField(label="Nasopharyngeal Swab")
    samplesreceivedcurrentweeknasalswab = forms.IntegerField(label="Nasal Swab")
    samplesreceivedcurrentweekoropharyngealswab = forms.IntegerField(label="Oropharyngeal Swab")
    samplesreceivedcurrentweekmidturbinateswab = forms.IntegerField(label="Midturbinate Swab")
    samplesreceivedcurrentweeksputum = forms.IntegerField(label="Sputum")
    samplesreceivedcurrentweekwholebloodorplasmaorserum = forms.IntegerField(label="Whole Blood/Plasma/Serum")
    samplesreceivedcurrentweekother = forms.IntegerField(label="Other(specify)")

    samplesrejectedcurrentweek =	forms.IntegerField(label="Samples Rejected (Current Week)")
    totalsamplesreceivedcurrentweek	=	forms.IntegerField(label="Total Samples Received (Current Week)")

    numberofsamplesenteredintolims =	forms.IntegerField(label="# of Samples entered into LIMS")
    totalsamplescurrentpluscarryover	 =	forms.IntegerField(label="Total Samples Current + Carryover")
    samplesreferred	=	forms.IntegerField(label="Samples Referred")
    samplesreferredtoname	=	forms.IntegerField(label="Samples Referred to (Name)")
    rejectionratecurrentweek = forms.DecimalField(label="% Rejection Rate (Current Week)", decimal_places=5,  max_digits=5)
    numberofresultsprintedlims =	forms.IntegerField(label="Number of Results printed (LIMS)")
    totalresultsdispatchedbylab	=	forms.IntegerField(label="Total Results dispatched by Lab")
    comment= forms.CharField(label="Comment: [Please input any comment regarding  samples carryover; samples received; samples rejected; rejection rate; printing and dispatch of results and developments and policy changes if applicable]", max_length=5000)
    lab= models.TextField(max_length=30,default="brti")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = specimensreceivedbrticovid19
            fields = '__all__'

class specimensrunbrticovid19Form(forms.ModelForm):

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

    dayofweek = forms.ChoiceField(choices=labchoices, initial="none", label="Select laboratory please" )
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")

    testsdoneabbottrun = forms.IntegerField(label="Run")
    testsdoneabbottfailedbuteligibleforrepeat = forms.IntegerField(label="Failed but eligible for repeat	")
    testsdoneabbottfailedbutnoteligibleforrepeat = forms.IntegerField(label="Failed but not eligible for repeat	")
    testsdoneabbottrepeat = forms.IntegerField(label="Repeat")


    testsdonebmxrun = forms.IntegerField(label="Run")
    testsdonebmxfailedbuteligibleforrepeat = forms.IntegerField(label="Failed but eligible for repeat	")
    testsdonebmxfailedbutnoteligibleforrepeat = forms.IntegerField(label="Failed but not eligible for repeat	")
    testsdonebmxrepeat = forms.IntegerField(label="Repeat")


    testsdonegenexpertrun = forms.IntegerField(label="Run")
    testsdonegenexpertfailedbuteligibleforrepeat = forms.IntegerField(label="Failed but eligible for repeat	")
    testsdonegenexpertfailedbutnoteligibleforrepeat = forms.IntegerField(label="Failed but not eligible for repeat	")
    testsdonegenexpertrepeat = forms.IntegerField(label="Repeat")



    testsdonequantstudio3run = forms.IntegerField(label="Run")
    testsdonequantstudio3failedbuteligibleforrepeat = forms.IntegerField(label="Failed but eligible for repeat	")
    testsdonequantstudio3failedbutnoteligibleforrepeat = forms.IntegerField(label="Failed but not eligible for repeat	")
    testsdonequantstudio3repeat = forms.IntegerField(label="Repeat")


    testsdonehologicpantherrun = forms.IntegerField(label="Run")
    testsdonehologicpantherfailedbuteligibleforrepeat = forms.IntegerField(label="Failed but eligible for repeat	")
    testsdonehologicpantherfailedbutnoteligibleforrepeat = forms.IntegerField(label="Failed but not eligible for repeat	")
    testsdonehologicpantherrepeat = forms.IntegerField(label="Repeat")


    testsdonerdtantibodyrun = forms.IntegerField(label="Run")
    testsdonerdtantibodyfailedbuteligibleforrepeat = forms.IntegerField(label="Failed but eligible for repeat	")
    testsdonerdtantibodyfailedbutnoteligibleforrepeat = forms.IntegerField(label="Failed but not eligible for repeat	")
    testsdonerdtantibodyrepeat = forms.IntegerField(label="Repeat")


    testsdonerdtantigenrun = forms.IntegerField(label="Run")
    testsdonerdtantigenfailedbuteligibleforrepeat = forms.IntegerField(label="Failed but eligible for repeat	")
    testsdonerdtantigenfailedbutnoteligibleforrepeat = forms.IntegerField(label="Failed but not eligible for repeat	")
    testsdonerdtantigenrepeat = forms.IntegerField(label="Repeat")


    totaltestsdone = forms.IntegerField(label="Total Tests Done")
    totaltestsdonetotalrepeats = forms.IntegerField(label="Total Repeats	")

    totaltestsdonetotalpatientsrun = forms.IntegerField(label="Total Repeats	")



    errorratesabbott = forms.IntegerField(label="Abbott")

    errorratesbmx = forms.DecimalField(decimal_places=5,  max_digits=5, label="BMX")
    errorratesgenexpert = forms.DecimalField(decimal_places=5,  max_digits=5, label="GeneXpert")
    errorratesquantstudio3 = forms.DecimalField(decimal_places=5,  max_digits=5,label="Quant Studio3	")
    errorrateshologicpanther = forms.DecimalField(decimal_places=5,  max_digits=5,label="Hologic Panther	")
    errorratesrdtantibody = forms.DecimalField(decimal_places=5,  max_digits=5,label="RDT (Antibody)	")
    errorratesrdtantigen = forms.DecimalField(decimal_places=5,  max_digits=5,label="RDT(Antigen)	")


    lab = forms.CharField()
    user = forms.CharField()





    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = specimensrunbrticovid19
            fields = '__all__'




class machinedowntimereagentstockouttoolbrticovid19Form(forms.ModelForm):
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

    dayofweek = forms.ChoiceField(choices=labchoices, initial="none", label="Select laboratory please" )
    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")

    numberofmachinebreakdownsabbott = forms.IntegerField(label="Abbott")
    numberofmachinebreakdownsbmx = forms.IntegerField(label="BMX")
    numberofmachinebreakdownsgenexpert = forms.IntegerField(label="GeneXpert")
    numberofmachinebreakdownsquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    numberofmachinebreakdownshologicpanther = forms.IntegerField(label="Hologic Panther")
    numberofmachinebreakdownscomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )


    machinedowntimedaysabbott = forms.IntegerField(label="Abbott")
    machinedowntimedaysbmx = forms.IntegerField(label="BMX")
    machinedowntimedaysgenexpert = forms.IntegerField(label="GeneXpert")
    machinedowntimedaysquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    machinedowntimedayshologicpanther = forms.IntegerField(label="Hologic Panther")
    machinedowntimedayscomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )


    reagentstockoutabbort = forms.IntegerField(label="Abbott")
    reagentstockoutbms = forms.IntegerField(label="BMX")
    reagentstockoutgenexpert = forms.IntegerField(label="GeneXpert")
    reagentstockoutquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    reagentstockouthologicpanther = forms.IntegerField(label="Hologic Panther")
    reagentstockoutcomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = machinedowntimereagentstockouttoolbrticovid19
            fields = '__all__'




class generalbrticovid19Form(forms.ModelForm):

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

    dayofweek = forms.ChoiceField(choices=labchoices, initial="none", label="Select laboratory please")
    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")

    generalcommentsregardingtestingandchallengesfacedbythelaboratory = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )

    numberofstaffwhotestedpositivetocovid19atvllab	= forms.IntegerField()
    numberofstaffwhohavebeenvaccinated	= forms.IntegerField()
    Comments =forms.CharField( max_length=5000)
    Requesttobrtifromthelaboratory	= forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = generalbrticovid19
            fields = '__all__'



 # --------------------brtivleidweeklystatisticstool--------------------------------------------------------------------------------------------------------------

class specimensrunbrtivleidForm(forms.ModelForm):

    labchoices=[
        ('NMRL','NMRL'),
        ('Mpilo','Mpilo'),
        ('BRIDH','BRIDH'),
        ('NTBRL','NTBRL'),
        ('Gweru','Gweru'),
        ('Chinhoyi','Chinhoyi'),
        ('Masvingo','Masvingo'),
        ('EID','EID'),
        ('Victoria Falls', 'Victoria Falls'),
        ('Bindura','Bindura'),
        ('Kadoma','Kadoma'),
        ('Marondera','Marondera'),
        ('St Lukes', 'St Lukes'),
        ('Gwanda','Gwanda'),
        ('Total','Total'),
    ]

    dayofweek = forms.ChoiceField(choices=labchoices, initial="none", label="Select laboratory please")
    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")



#Roche
    testsdonerochenumberofsamplesreceivedthisweekplasma = forms.IntegerField()
    testsdonerochenumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField()
    testsdonerochefailedbuteligibaleforrepeatplasma= forms.IntegerField()
    testsdonerochefailedbutnoteligibaleforrepeatplasma= forms.IntegerField()
    testsdonerocherepeatplasma= forms.IntegerField()
    testsdonerochefailedafterrepeattestingplasma = forms.IntegerField()


    testsdonerochenumberofsamplesreceivedthisweekdbs = forms.IntegerField()
    testsdonerochenumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField()
    testsdonerochefailedbuteligibaleforrepeatdbs= forms.IntegerField()
    testsdonerochefailedbutnoteligibaleforrepeatdbs= forms.IntegerField()
    testsdonerocherepeatdbs= forms.IntegerField()
    testsdonerochefailedafterrepeattestingdbs = forms.IntegerField()
#BMX
    testsdonebmxnumberofsamplesreceivedthisweekplasma = forms.IntegerField()
    testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField()
    testsdonebmxfailedbuteligibaleforrepeatplasma= forms.IntegerField()
    testsdonebmxfailedbutnoteligibaleforrepeatplasma= forms.IntegerField()
    testsdonebmxrepeatplasma= forms.IntegerField()
    testsdonebmxfailedafterrepeattestingplasma = forms.IntegerField()


    testsdonebmxnumberofsamplesreceivedthisweekdbs = forms.IntegerField()
    testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField()
    testsdonebmxfailedbuteligibaleforrepeatdbs= forms.IntegerField()
    testsdonebmxfailedbutnoteligibaleforrepeatdbs= forms.IntegerField()
    testsdonebmxrepeatdbs= forms.IntegerField()
    testsdonebmxfailedafterrepeattestingdbs = forms.IntegerField()

#Abbott
    testsdoneabbottnumberofsamplesreceivedthisweekplasma = forms.IntegerField()
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField()
    testsdoneabbottfailedbuteligibaleforrepeatplasma= forms.IntegerField()
    testsdoneabbottfailedbutnoteligibaleforrepeatplasma= forms.IntegerField()
    testsdoneabbottrepeatplasma= forms.IntegerField()
    testsdoneabbottfailedafterrepeattestingplasma = forms.IntegerField()


    testsdoneabbottnumberofsamplesreceivedthisweekdbs = forms.IntegerField()
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField()
    testsdoneabbottfailedbuteligibaleforrepeatdbs= forms.IntegerField()
    testsdoneabbottfailedbutnoteligibaleforrepeatdbs= forms.IntegerField()
    testsdoneabbottrepeatdbs= forms.IntegerField()
    testsdoneabbottfailedafterrepeattestingdbs = forms.IntegerField()

#Hologic Panther
    testsdonehologicpanthernumberofsamplesreceivedthisweekplasma = forms.IntegerField()

    tests2= forms.IntegerField()
    #testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField()


    testsdonehologicpantherfailedbuteligibaleforrepeatplasma= forms.IntegerField()
    testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma= forms.IntegerField()
    testsdonehologicpantherrepeatplasma= forms.IntegerField()
    testsdonehologicpantherfailedafterrepeattestingplasma = forms.IntegerField()


    testsdonehologicpanthernumberofsamplesreceivedthisweekdbs = forms.IntegerField()
    tests1 = forms.IntegerField()
    #testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField()

    testsdonehologicpantherfailedbuteligibaleforrepeatdbs= forms.IntegerField()
    testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs= forms.IntegerField()
    testsdonehologicpantherrepeatdbs= forms.IntegerField()
    testsdonehologicpantherfailedafterrepeattestingdbs = forms.IntegerField()

    totaltestsdone = forms.IntegerField()
    totalrepeats = forms.IntegerField()
    totalpatientsrun = forms.IntegerField()
    targetsweekly = forms.IntegerField()
    percentagetargetsachievements = forms.DecimalField(decimal_places=5,  max_digits=5)


    percentageerrorraterocheplasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentageerrorraterochedbs = forms.DecimalField(decimal_places=5,  max_digits=5)

    percentageerrorratebmxplasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentageerrorratebmxdbs = forms.DecimalField(decimal_places=5,  max_digits=5)

    percentageerrorrateabbottplasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentageerrorrateabbottdbs = forms.DecimalField(decimal_places=5,  max_digits=5)

    percentageerrorratehologicpantherplasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentageerrorratehologicpantherdbs = forms.DecimalField(decimal_places=5,  max_digits=5)



    totalncsfromaudit=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)
    ncsnotyetclosed=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)
    ncsclosedthisweek=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)
    totalncsfromaudit1=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)
    ncsnotyetclosed1=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)
    ncsclosedthisweek1=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = specimensrunbrtivleid
            fields = '__all__'



class specimensreceivedbrtivleidForm(forms.ModelForm):
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

    dayofweek = forms.ChoiceField(choices=labchoices, initial="none", label="Select laboratory please")
    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")

    samplescarriedoverpreviousweeknevertestedplasma = forms.IntegerField()
    samplescarriedoverpreviousweeknevertesteddbs = forms.IntegerField()

    samplescarriedoverpreviouspreviousfailedsamplesplasma = forms.IntegerField()
    samplescarriedoverpreviouspreviousfailedsamplesdbs = forms.IntegerField()

    samplesreceivedcurrentweekplasma = forms.IntegerField()
    samplesreceivedcurrentweekdbs = forms.IntegerField()

    samplesrejectedcurrentweekplasma = forms.IntegerField()
    samplesrejectedcurrentweekdbs = forms.IntegerField()

    totalsamplesreceivedcurrentweekplasma = forms.IntegerField()
    totalsamplesreceivedcurrentweekdbs = forms.IntegerField()

    numberofsamplesenteredintolimsondayofarrivalplasma = forms.IntegerField()
    numberofsamplesenteredintolimsondayofarrivaldbs = forms.IntegerField()

    numberofsamplesenteredintolimsafterdayofarrivalplasma = forms.IntegerField()
    numberofsamplesenteredintolimsafterdayofarrivaldbs = forms.IntegerField()

    numberofhourslimswasfunctional = forms.IntegerField()

    totalsamplescurrentandcarryoverplasma = forms.IntegerField()
    totalsamplescurrentandcarryoverdbs = forms.IntegerField()

    samplesrefferedplasma = forms.IntegerField()
    samplesreffereddbs = forms.IntegerField()

    labsamplesrefferedto = forms.IntegerField()

    percentagerejectionrateplasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentagerejectionratedbs = forms.DecimalField(decimal_places=5,  max_digits=5)

    numberofresultsprintedfromlimsplasma = forms.IntegerField()
    numberofresultsprintedfromlimsdbs = forms.IntegerField()

    totalresultsdispatchedbylabplasma	= forms.IntegerField()
    totalresultsdispatchedbylabdbs	= forms.IntegerField()

    totalresultsdispatchedbylabviasmsplasma	= forms.IntegerField()
    totalresultsdispatchedbylabviasmsdbs	= forms.IntegerField()

    reasonsforrejectionssamplequalitycompromisedplasma = forms.IntegerField()
    reasonsforrejectionssamplequalitycompromiseddbs = forms.IntegerField()

    #reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientplasma = forms.IntegerField()

    reasons6= forms.IntegerField(label="plasma")


    #reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientdbs = forms.IntegerField()
    reasons5= forms.IntegerField()


    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchplasma = forms.IntegerField()
    reasons2= forms.IntegerField()


    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchdbs = forms.IntegerField()
    reasons1= forms.IntegerField()


    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingplasma = forms.IntegerField()
    reasons4= forms.IntegerField()

    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingdbs = forms.IntegerField()
    reasons3= forms.IntegerField()


    reasonsforrejectionssamplequalitycompromisedqdacheckplasma = forms.IntegerField()
    reasonsforrejectionssamplequalitycompromisedqdacheckdbs = forms.IntegerField()

    reasonsforsamplerefferalreagentorkitstockoutplasma= forms.IntegerField()
    reasonsforsamplerefferalreagentorkitstockoutdbs= forms.IntegerField()


    reasonsforsamplerefferalinstrumentmechanicalfailureplasma= forms.IntegerField()
    reasonsforsamplerefferalinstrumentmechanicalfailuredbs= forms.IntegerField()

    reasonsforsamplerefferalinsufficientinstrumentcapacityplasma= forms.IntegerField()
    reasonsforsamplerefferalinsufficientinstrumentcapacitydbs= forms.IntegerField()

    reasonsforsamplerefferalinsufficienthrcapacityplasma= forms.IntegerField()
    reasonsforsamplerefferalinsufficienthrcapacitydbs= forms.IntegerField()

    reasonsforsamplerefferaldqacheckplasma= forms.IntegerField()
    reasonsforsamplerefferaldqacheckdbs= forms.IntegerField()

    comments=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = specimensreceivedbrtivleid
            fields = '__all__'




class reasonsforfailurebrtivleidForm(forms.ModelForm):
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

    dayofweek = forms.ChoiceField(choices=labchoices, initial="none", label="Select laboratory please")
    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")

    #roche

    rocheplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    rocheplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    rocheplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    rocheplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    rocheplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    rocheplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    rocheplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    rochedqacheckplasma = forms.IntegerField(label="DQA check")

    rochedbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    rochedbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    rochedbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    rochedbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    rochedbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    rochedbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    rochedbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    rochedqacheckdbs = forms.IntegerField(label="DQA check")

#bmx

    bmxplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmxplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmxplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmxplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    bmxplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmxplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    bmxplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    bmxdqacheckplasma = forms.IntegerField(label="DQA check")

    bmxdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmxdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmxdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmxdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    bmxdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmxdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    bmxdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    bmxdqacheckdbs = forms.IntegerField(label="DQA check")

#abbott

    abbottplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbottplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbottplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbottplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    abbottplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbottplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    abbottplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    abbottdqacheckplasma = forms.IntegerField(label="DQA check")

    abbottdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbottdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbottdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbottdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    abbottdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbottdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    abbottdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    abbottdqacheckdbs = forms.IntegerField(label="DQA check")

#Hologic Panther

    hologicpantherplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologicpantherplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologicpantherplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologicpantherplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    hologicpantherplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologicpantherplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    hologicpantherplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    hologicpantherdqacheckplasma = forms.IntegerField(label="DQA check")

    hologicpantherdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologicpantherdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologicpantherdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologicpantherdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    hologicpantherdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologicpantherdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    hologicpantherdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    hologicpantherdqacheckdbs = forms.IntegerField(label="DQA check")
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.formclass = 'form-horizontal'
        self.helper.fieldclass = 'col-sm-6'
        self.helper.labelclass = 'col-sm-6'
        self.helper.layout = Layout(
        )

    class Meta:
            model = reasonsforfailurebrtivleid
            fields = '__all__'





 # ----------------------------------------------------------------------------------------------------------------------------------

#masvingbrtivlweeklystatisticstool31-6june2021

class SpecimensrunbrtivlweeklyForm(forms.ModelForm):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")
    dateofrecord = forms.CharField()



#Roche
    testsdonerochenumberofsamplesreceivedthisweekplasma = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonerochenumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonerochefailedbuteligibaleforrepeatplasma= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonerochefailedbutnoteligibaleforrepeatplasma= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonerocherepeatplasma= forms.IntegerField(label="Repeat")
    testsdonerochefailedafterrepeattestingplasma = forms.IntegerField(label="Failed After Repeat Testing")


    testsdonerochenumberofsamplesreceivedthisweekdbs = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonerochenumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonerochefailedbuteligibaleforrepeatdbs= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonerochefailedbutnoteligibaleforrepeatdbs= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonerocherepeatdbs= forms.IntegerField(label="Repeat")
    testsdonerochefailedafterrepeattestingdbs = forms.IntegerField(label="Failed After Repeat Testing")
#BMX
    testsdonebmxnumberofsamplesreceivedthisweekplasma = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonebmxfailedbuteligibaleforrepeatplasma= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonebmxfailedbutnoteligibaleforrepeatplasma= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonebmxrepeatplasma= forms.IntegerField(label="Repeat")
    testsdonebmxfailedafterrepeattestingplasma = forms.IntegerField(label="Failed After Repeat Testing")


    testsdonebmxnumberofsamplesreceivedthisweekdbs = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonebmxfailedbuteligibaleforrepeatdbs= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonebmxfailedbutnoteligibaleforrepeatdbs= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonebmxrepeatdbs= forms.IntegerField(label="Repeat")
    testsdonebmxfailedafterrepeattestingdbs = forms.IntegerField(label="Failed After Repeat Testing")

#Abbott
    testsdoneabbottnumberofsamplesreceivedthisweekplasma = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdoneabbottfailedbuteligibaleforrepeatplasma= forms.IntegerField(label="Failed but eligible for repeat")
    testsdoneabbottfailedbutnoteligibaleforrepeatplasma= forms.IntegerField(label="Failed not eligible for repeat")
    testsdoneabbottrepeatplasma= forms.IntegerField(label="Repeat")
    testsdoneabbottfailedafterrepeattestingplasma = forms.IntegerField(label="Failed After Repeat Testing")


    testsdoneabbottnumberofsamplesreceivedthisweekdbs = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdoneabbottfailedbuteligibaleforrepeatdbs= forms.IntegerField(label="Failed but eligible for repeat")
    testsdoneabbottfailedbutnoteligibaleforrepeatdbs= forms.IntegerField(label="Failed not eligible for repeat")
    testsdoneabbottrepeatdbs= forms.IntegerField(label="Repeat")
    testsdoneabbottfailedafterrepeattestingdbs = forms.IntegerField(label="Failed After Repeat Testing")

#Hologic Panther
    testsdonehologicpanthernumberofsamplesreceivedthisweekplasma = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonehologicpantherfailedbuteligibaleforrepeatplasma= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonehologicpantherrepeatplasma= forms.IntegerField(label="Repeat")
    testsdonehologicpantherfailedafterrepeattestingplasma = forms.IntegerField(label="Failed After Repeat Testing")


    testsdonehologicpanthernumberofsamplesreceivedthisweekdbs = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonehologicpantherfailedbuteligibaleforrepeatdbs= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonehologicpantherrepeatdbs= forms.IntegerField(label="Repeat")
    testsdonehologicpantherfailedafterrepeattestingdbs = forms.IntegerField(label="Failed After Repeat Testing")

    totaltestsdone = forms.IntegerField(label="Total Tests Done")
    totalrepeats = forms.IntegerField(label="Total Repeats")
    totalpatientsrun = forms.IntegerField(label="Total Patients Run")
    targetsweekly = forms.IntegerField(label="Target:Weekly")
    percentagetargetsachievements = forms.DecimalField(label="%Target Achievement", decimal_places=5,  max_digits=5)


    percentageerrorraterocheplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentageerrorraterochedbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)

    percentageerrorratebmxplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentageerrorratebmxdbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)

    percentageerrorrateabbottplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentageerrorrateabbottdbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)

    percentageerrorratehologicpantherplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentageerrorratehologicpantherdbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)


    totalncsfromaudit=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=300, label="Total NCs from Audit (exchange audits)")
    ncsnotyetclosed=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=300, label="NCs not yet closed")
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')
    key= forms.CharField(initial='123')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Specimensrunbrtivlweekly
            fields = '__all__'

class SpecimensrecievedbrtivlweeklyForm(forms.ModelForm):
    
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")
    dateofrecord = forms.CharField()



    samplescarriedoverpreviousweeknevertestedplasma = forms.IntegerField(label="Plasma")
    samplescarriedoverpreviousweeknevertesteddbs = forms.IntegerField(label="DBS")

    samplescarriedoverpreviouspreviousfailedsamplesplasma = forms.IntegerField(label="Plasma")
    samplescarriedoverpreviouspreviousfailedsamplesdbs = forms.IntegerField(label="DBS")


    samplesreceivedcurrentweekplasma = forms.IntegerField(label="Plasma")
    samplesreceivedcurrentweekdbs = forms.IntegerField(label="DBS")

    samplesrejectedcurrentweekplasma = forms.IntegerField(label="Plasma")
    samplesrejectedcurrentweekdbs = forms.IntegerField(label="DBS")


    totalsamplesreceivedcurrentweekplasma = forms.IntegerField(label="Plasma")
    totalsamplesreceivedcurrentweekdbs = forms.IntegerField(label="DBS")

    numberofsamplesenteredintolimsondayofarrivalplasma = forms.IntegerField(label="Plasma")
    numberofsamplesenteredintolimsondayofarrivaldbs = forms.IntegerField(label="DBS")


    numberofsamplesenteredintolimsafterdayofarrivalplasma = forms.IntegerField(label="Plasma")
    numberofsamplesenteredintolimsafterdayofarrivaldbs = forms.IntegerField(label="DBS")

    numberofhourslimswasfunctional = forms.IntegerField(label="# of hours LIMS was Functional")

    totalsamplescurrentandcarryoverplasma = forms.IntegerField(label="Plasma")
    totalsamplescurrentandcarryoverdbs = forms.IntegerField(label="DBS")

    samplesrefferedplasma = forms.IntegerField(label="Plasma")
    samplesreffereddbs = forms.IntegerField(label="DBS")

    labsamplesrefferedto = forms.IntegerField(label="Lab Samples Referred to")

    percentagerejectionrateplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentagerejectionratedbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)


    numberofresultsprintedfromlimsplasma = forms.IntegerField(label="Plasma")
    numberofresultsprintedfromlimsdbs = forms.IntegerField(label="DBS")

    totalresultsdispatchedbylabplasma	= forms.IntegerField(label="Plasma")
    totalresultsdispatchedbylabdbs	= forms.IntegerField(label="DBS")

    totalresultsdispatchedbylabviasmsplasma	= forms.IntegerField(label="Plasma")
    totalresultsdispatchedbylabviasmsdbs	= forms.IntegerField(label="DBS")



    reasonsforrejectionssamplequalitycompromisedplasma = forms.IntegerField(label="Plasma")
    reasonsforrejectionssamplequalitycompromiseddbs = forms.IntegerField(label="DBS")


    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientplasma = forms.IntegerField(label="Plasma")
    reasons6 = forms.IntegerField(label="Plasma")


    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientdbs = forms.IntegerField(label="DBS")
    reasons5 = forms.IntegerField(label="DBS")

    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchplasma = forms.IntegerField(label="Plasma")
    reasons2 = forms.IntegerField(label="Plasma")


    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchdbs = forms.IntegerField(label="DBS")
    reasons1 = forms.IntegerField(label="DBS")

    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingplasma = forms.IntegerField(label="Plasma")
    reasons4 = forms.IntegerField(label="Plasma")


    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingdbs = forms.IntegerField(label="DBS")
    reasons3= forms.IntegerField(label="DBS")


    reasonsforrejectionssamplequalitycompromisedqdacheckplasma = forms.IntegerField(label="Plasma")
    reasonsforrejectionssamplequalitycompromisedqdacheckdbs = forms.IntegerField(label="DBS")


    reasonsforsamplerefferalreagentorkitstockoutplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferalreagentorkitstockoutdbs= forms.IntegerField(label="DBS")


    reasonsforsamplerefferalinstrumentmechanicalfailureplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferalinstrumentmechanicalfailuredbs= forms.IntegerField(label="DBS")

    reasonsforsamplerefferalinsufficientinstrumentcapacityplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferalinsufficientinstrumentcapacitydbs= forms.IntegerField(label="DBS")

    reasonsforsamplerefferalinsufficienthrcapacityplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferalinsufficienthrcapacitydbs= forms.IntegerField(label="DBS")

    reasonsforsamplerefferaldqacheckplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferaldqacheckdbs= forms.IntegerField(label="DBS")

    comments=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), label="Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=5000)
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')
    key= forms.CharField(initial='123')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Specimensrecievedbrtivlweekly
            fields = '__all__'

class ReasonsforfailurebrtivlweeklyForm(forms.ModelForm):

    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")


#roche
    rocheplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    rocheplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    rocheplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    rocheplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    rocheplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    rocheplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    rocheplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    rochedqacheckplasma = forms.IntegerField(label="DQA check")

    rochedbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    rochedbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    rochedbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    rochedbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    rochedbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    rochedbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    rochedbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    rochedqacheckdbs = forms.IntegerField(label="DQA check")

#bmx

    bmxplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmxplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmxplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmxplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    bmxplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmxplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    bmxplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    bmxdqacheckplasma = forms.IntegerField(label="DQA check")

    bmxdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmxdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmxdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmxdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    bmxdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmxdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    bmxdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    bmxdqacheckdbs = forms.IntegerField(label="DQA check")

#abbott

    abbottplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbottplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbottplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbottplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    abbottplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbottplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    abbottplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    abbottdqacheckplasma = forms.IntegerField(label="DQA check")

    abbottdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbottdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbottdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbottdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    abbottdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbottdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    abbottdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    abbottdqacheckdbs = forms.IntegerField(label="DQA check")

#Hologic Panther

    hologicpantherplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologicpantherplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologicpantherplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologicpantherplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    hologicpantherplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologicpantherplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    hologicpantherplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    hologicpantherdqacheckplasma = forms.IntegerField(label="DQA check")

    hologicpantherdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologicpantherdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologicpantherdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologicpantherdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    hologicpantherdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologicpantherdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    hologicpantherdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    hologicpantherdqacheckdbs = forms.IntegerField(label="DQA check")
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')
    key= forms.CharField(initial='123')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Reasonsforfailurebrtivlweekly
            fields = '__all__'

class ElectricoutagebrtivlweeklyForm(forms.ModelForm):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")    
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")



    numberofhourswithnoelectricityperday	= forms.IntegerField(label="Number of hours with no electricity per day")
    numberofhoursgeneratorwasonperday	= forms.IntegerField(label="Number of hours generator was on per day")
    litresoffueladdedtogeneratorperday	= forms.IntegerField(label="Litres of Fuel added to generator per day")
    numberofhoursmachineswasnotbeingusedduetopowercutperday	= forms.IntegerField(label="Number of hours machine/s was not being used due to power cut per day")
    totaltestsdoneperdayusinggenerator	= forms.IntegerField(label="Total Tests done per day using generator")

    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')
    key= forms.CharField(initial='123')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Electricoutagebrtivlweekly
            fields = '__all__'
 # ----------------------------------------------------------------------------------------------------------------------------------
# ---------------------------eid---------------------------------
#masvingbrtiweeklystatisticstool31-6june2021


class Specimensrunbrtiweekly(forms.ModelForm):

    dayofweek = forms.CharField(widget=forms.HiddenInput(), initial="none", label="Select date" )
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")
    dateofrecord = models.CharField()



#Roche
    testsdonerochenumberofsamplesreceivedthisweekplasma = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonerochenumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonerochefailedbuteligibaleforrepeatplasma= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonerochefailedbutnoteligibaleforrepeatplasma= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonerocherepeatplasma= forms.IntegerField(label="Repeat")
    testsdonerochefailedafterrepeattestingplasma = forms.IntegerField(label="Failed After Repeat Testing")


    testsdonerochenumberofsamplesreceivedthisweekdbs = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonerochenumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonerochefailedbuteligibaleforrepeatdbs= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonerochefailedbutnoteligibaleforrepeatdbs= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonerocherepeatdbs= forms.IntegerField(label="Repeat")
    testsdonerochefailedafterrepeattestingdbs = forms.IntegerField(label="Failed After Repeat Testing")
#BMX
    testsdonebmxnumberofsamplesreceivedthisweekplasma = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonebmxnumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonebmxfailedbuteligibaleforrepeatplasma= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonebmxfailedbutnoteligibaleforrepeatplasma= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonebmxrepeatplasma= forms.IntegerField(label="Repeat")
    testsdonebmxfailedafterrepeattestingplasma = forms.IntegerField(label="Failed After Repeat Testing")


    testsdonebmxnumberofsamplesreceivedthisweekdbs = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdonebmxnumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdonebmxfailedbuteligibaleforrepeatdbs= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonebmxfailedbutnoteligibaleforrepeatdbs= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonebmxrepeatdbs= forms.IntegerField(label="Repeat")
    testsdonebmxfailedafterrepeattestingdbs = forms.IntegerField(label="Failed After Repeat Testing")

#Abbott
    testsdoneabbottnumberofsamplesreceivedthisweekplasma = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdoneabbottfailedbuteligibaleforrepeatplasma= forms.IntegerField(label="Failed but eligible for repeat")
    testsdoneabbottfailedbutnoteligibaleforrepeatplasma= forms.IntegerField(label="Failed but not eligible for repeat")
    testsdoneabbottrepeatplasma= forms.IntegerField(label="Repeat")
    testsdoneabbottfailedafterrepeattestingplasma = forms.IntegerField(label="Failed After Repeat Testing")


    testsdoneabbottnumberofsamplesreceivedthisweekdbs = forms.IntegerField(label="Run (Number of samples received this week)")
    testsdoneabbottnumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    testsdoneabbottfailedbuteligibaleforrepeatdbs= forms.IntegerField(label="Failed but eligible for repeat")
    testsdoneabbottfailedbutnoteligibaleforrepeatdbs= forms.IntegerField(label="Failed but not eligible for repeat")
    testsdoneabbottrepeatdbs= forms.IntegerField(label="Repeat")
    testsdoneabbottfailedafterrepeattestingdbs = forms.IntegerField(label="Failed After Repeat Testing")

#Hologic Panther
    testsdonehologicpanthernumberofsamplesreceivedthisweekplasma = forms.IntegerField(label="Run (Number of samples received this week)")
    # testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksplasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests2 = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")

    testsdonehologicpantherfailedbuteligibaleforrepeatplasma= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonehologicpantherfailedbutnoteligibaleforrepeatplasma= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonehologicpantherrepeatplasma= forms.IntegerField(label="Repeat")
    testsdonehologicpantherfailedafterrepeattestingplasma = forms.IntegerField(label="Failed After Repeat Testing")


    testsdonehologicpanthernumberofsamplesreceivedthisweekdbs = forms.IntegerField(label="Run (Number of samples received this week)")

    # testsdonehologicpanthernumberofsamplescarriedoverpreviousweeksdbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests1 = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")

    testsdonehologicpantherfailedbuteligibaleforrepeatdbs= forms.IntegerField(label="Failed but eligible for repeat")
    testsdonehologicpantherfailedbutnoteligibaleforrepeatdbs= forms.IntegerField(label="Failed not eligible for repeat")
    testsdonehologicpantherrepeatdbs= forms.IntegerField(label="Repeat")
    testsdonehologicpantherfailedafterrepeattestingdbs = forms.IntegerField(label="Failed After Repeat Testing")

    totaltestsdone = forms.IntegerField(label="Total Tests Done")
    totalrepeats = forms.IntegerField(label="Total Repeats")
    totalpatientsrun = forms.IntegerField(label="Total Patients Run")
    targetsweekly = forms.IntegerField(label="Target:Weekly")
    percentagetargetsachievements = forms.DecimalField(label="%Target Achievement", decimal_places=5,  max_digits=5)


    percentageerrorraterocheplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentageerrorraterochedbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)

    percentageerrorratebmxplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentageerrorratebmxdbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)

    percentageerrorrateabbottplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentageerrorrateabbottdbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)

    percentageerrorratehologicpantherplasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentageerrorratehologicpantherdbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)


    totalncsfromaudit=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, label="Total NCs from Audit (exchange audits)")
    ncsnotyetclosed=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, label="NCs not yet closed")
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Specimensrunbrtiweekly
            fields = '__all__'


class SpecimensreceivedbrtiweeklyForm(forms.ModelForm):
    
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")

    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")


    samplescarriedoverpreviousweeksnevertestedplasma = forms.IntegerField(label="Plasma")
    samplescarriedoverpreviousweeksnevertesteddbs = forms.IntegerField(label="DBS")

    samplescarriedoverpreviousfailedsamplesplasma = forms.IntegerField(label="Plasma")
    samplescarriedoverpreviousfailedsamplesdbs = forms.IntegerField(label="DBS")



    samplesreceivedcurrentweekplasma = forms.IntegerField(label="Plasma")
    samplesreceivedcurrentweekdbs = forms.IntegerField(label="DBS")

    samplesrejectedcurrentweekplasma = forms.IntegerField(label="Plasma")
    samplesrejectedcurrentweekdbs = forms.IntegerField(label="DBS")

    totalsamplesreceivedcurrentweekplasma = forms.IntegerField(label="Plasma")
    totalsamplesreceivedcurrentweekdbs = forms.IntegerField(label="DBS")

    numberofsamplesenteredintolimsondayofarrivalplasma = forms.IntegerField(label="Plasma")
    numberofsamplesenteredintolimsondayofarrivaldbs = forms.IntegerField(label="DBS")

    numberofsamplesenteredintolimsafterdayofarrivalplasma = forms.IntegerField(label="Plasma")
    numberofsamplesenteredintolimsafterdayofarrivaldbs = forms.IntegerField(label="DBS")

    numberofhourslimswasfunctional	 = forms.IntegerField(label="# of hours LIMS was Functional")

    totalsamplescurrentpluscarryoverplasma= forms.IntegerField(label="Plasma")
    totalsamplescurrentpluscarryoverdbs= forms.IntegerField(label="DBS")

    samplesrefferedplasma = forms.IntegerField(label="Plasma")
    samplesreffereddbs = forms.IntegerField(label="DBS")

    labsamplesrefferedto = forms.IntegerField(label="Lab Samples Referred to")

    percentagerejectionrateplasma = forms.DecimalField(label="Plasma",decimal_places=5,  max_digits=5)
    percentagerejectionratedbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)


    numberofresultsprintedfromlimsplasma = forms.IntegerField(label="Plasma")
    numberofresultsprintedfromlimsdbs = forms.IntegerField(label="DBS")

    totalresultsdispatchedbylabplasma	= forms.IntegerField(label="Plasma")
    totalresultsdispatchedbylabdbs	= forms.IntegerField(label="DBS")

    totalresultsdispatchedbylabviasmsplasma	= forms.IntegerField(label="Plasma")
    totalresultsdispatchedbylabviasmsdbs	= forms.IntegerField(label="DBS")


    reasonsforrejectionssamplequalitycompromisedplasma = forms.IntegerField(label="Plasma")
    reasonsforrejectionssamplequalitycompromiseddbs = forms.IntegerField(label="DBS")


    # reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientplasma = forms.IntegerField(label="Plasma")
    reason6 = forms.IntegerField(label="Plasma")

    #reasonsforrejectionssamplequalitycompromisedsamplequalityinsufficientdbs = forms.IntegerField(label="DBS")
    reasons5 = forms.IntegerField(label="DBS")


    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchplasma = forms.IntegerField(label="Plasma")
    reasons2 = forms.IntegerField(label="Plasma")

    # reasonsforrejectionssamplequalitycompromisedsampleinformationmismatchdbs = forms.IntegerField(label="DBS")
    reasons1 = forms.IntegerField(label="DBS")


    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingplasma = forms.IntegerField(label="Plasma")
    reasons4 = forms.IntegerField(label="Plasma")


    # reasonsforrejectionssamplequalitycompromisedsampleorrequestformmissingdbs = forms.IntegerField(label="DBS")
    reasons3  = forms.IntegerField(label="DBS")


    reasonsforrejectionssamplequalitycompromisedqdacheckplasma = forms.IntegerField(label="Plasma")
    reasonsforrejectionssamplequalitycompromisedqdacheckdbs = forms.IntegerField(label="DBS")


    reasonsforsamplerefferalreagentorkitstockoutplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferalreagentorkitstockoutdbs= forms.IntegerField(label="DBS")


    reasonsforsamplerefferalinstrumentmechanicalfailureplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferalinstrumentmechanicalfailuredbs= forms.IntegerField(label="DBS")

    reasonsforsamplerefferalinsufficientinstrumentcapacityplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferalinsufficientinstrumentcapacitydbs= forms.IntegerField(label="DBS")

    reasonsforsamplerefferalinsufficienthrcapacityplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferalinsufficienthrcapacitydbs= forms.IntegerField(label="DBS")

    reasonsforsamplerefferaldqacheckplasma= forms.IntegerField(label="Plasma")
    reasonsforsamplerefferaldqacheckdbs= forms.IntegerField(label="DBS")

    comments=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), label=" Comments: Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=5000)
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Specimensreceivedbrtiweekly
            fields = '__all__'


class ReasonsforfailurebrtiweeklyForm(forms.ModelForm):

    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")

    #dayofweek = forms.CharField(widget=forms.HiddenInput(), initial="none", label="Select date" )
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")
    dateofrecord = forms.CharField()

#roche
    rocheplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    rocheplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    rocheplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    rocheplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    rocheplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    rocheplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    rocheplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    rochedqacheckplasma = forms.IntegerField(label="DQA check")

    rochedbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    rochedbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    rochedbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    rochedbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    rochedbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    rochedbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    rochedbsnumberoffailedtestsduetoother = forms.IntegerField()
    rochedqacheckdbs = forms.IntegerField(label="DQA check")

#bmx

    bmxplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmxplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmxplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmxplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    bmxplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmxplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    bmxplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    bmxdqacheckplasma = forms.IntegerField(label="DQA check")

    bmxdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmxdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmxdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmxdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    bmxdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmxdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    bmxdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    bmxdqacheckdbs = forms.IntegerField(label="DQA check")



#abbott

    abbottplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbottplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbottplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbottplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    abbottplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbottplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    abbottplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    abbottdqacheckplasma = forms.IntegerField(label="DQA check")

    abbottdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbottdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbottdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbottdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    abbottdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbottdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    abbottdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    abbottdqacheckdbs = forms.IntegerField(label="DQA check")
#Hologic Panther

    hologicpantherplasmanumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologicpantherplasmanumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologicpantherplasmanumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologicpantherplasmanumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    hologicpantherplasmanumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologicpantherplasmanumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    hologicpantherplasmanumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    hologicpantherdqacheckplasma = forms.IntegerField(label="DQA check")

    hologicpantherdbsnumberoffailedtestsduetosamplequalityissues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologicpantherdbsnumberoffailedtestsduetoreagentqualityissues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologicpantherdbsnumberoffailedtestsduetoduetoqcfailure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologicpantherdbsnumberoffailedtestsduetopowerfailure = forms.IntegerField(label="# of failed tests due to power failure")
    hologicpantherdbsnumberoffailedtestsduetomechanicalfailure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologicpantherdbsnumberoffailedtestsduetoprocessingerror = forms.IntegerField(label="Processing Error")
    hologicpantherdbsnumberoffailedtestsduetoother = forms.IntegerField(label="Other Specify")
    hologicpantherdqacheckdbs = forms.IntegerField(label="DQA check")
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')
    key= forms.CharField(initial='vl')



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Reasonsforfailurebrtiweekly
            fields = '__all__'

class ElectricoutagebrtiweeklyForm(forms.ModelForm):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")
    dateofrecord = models.CharField()



    numberofhourswithnoelectricityperday	= forms.IntegerField(label="Number of hours with no electricity per day")
    numberofhoursgeneratorwasonperday	= forms.IntegerField(label="Number of hours generator was on per day")
    litresoffueladdedtogeneratorperday	= forms.IntegerField(label="Litres of Fuel added to generator per day")
    numberofhoursmachineswasnotbeingusedduetopowercutperday	= forms.IntegerField(label="Number of hours machine/s was not being used due to power cut per day")
    totaltestsdoneperdayusinggenerator	= forms.IntegerField(label="Total Tests done per day using generator")
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')

    key= forms.CharField(initial='eid')




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Electricoutagebrtiweekly
            fields = '__all__'

 # ----------------------------------------------------------------------------------------------------------------------------------
 #masvingo brticovid19weeklystatisticstool

class Specimensreceivedcovid19Form(forms.ModelForm):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")
    dateofrecord = models.CharField()
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")

    samplescarriedoverpreviousweeks	= forms.IntegerField(label="Samples Carried Over (Previous Weeks(s))")
    samplesreceivedcurrentweeknasopharyngealswab = forms.IntegerField(label="Nasopharyngeal Swab")
    samplesreceivedcurrentweeknasalswab = forms.IntegerField(label="Nasal Swab")
    samplesreceivedcurrentweekoropharyngealswab = forms.IntegerField(label="Oropharyngeal Swab")
    samplesreceivedcurrentweekmidturbinateswab = forms.IntegerField(label="Midturbinate Swab")
    samplesreceivedcurrentweeksputum = forms.IntegerField(label="Sputum")
    samplesreceivedcurrentweekwholebloodorplasmaorserum = forms.IntegerField(label="Whole Blood/Plasma/Serum")
    samplesreceivedcurrentweekother = forms.IntegerField(label="Other(specify)")


    samplesrejectedcurrentweek =	forms.IntegerField(label="Samples Rejected (Current Week)")
    totalsamplesreceivedcurrentweek	=	forms.IntegerField(label="Total Samples Received (Current Week)")

    numberofsamplesenteredintolims =	forms.IntegerField(label="# of Samples entered into LIMS")
    totalsamplescurrentpluscarryover	 =	forms.IntegerField(label="Total Samples Current + Carryover")
    samplesreferred	=	forms.IntegerField(label="Samples Referred")
    samplesReferredtoName = forms.CharField(max_length=500, label="Samples Referred to (Name)")
    rejectionratecurrentweek = forms.DecimalField(label="% Rejection Rate (Current Week)", decimal_places=5,  max_digits=5)
    numberofresultsprintedlims =	forms.IntegerField(label="Number of Results printed (LIMS)")
    totalresultsdispatchedbylab	=	forms.IntegerField(label="Total Results dispatched by Lab")
    comment= forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), label="Comment: [Please input any comment regarding  samples carryover; samples received; samples rejected; rejection rate; printing and dispatch of results and developments and policy changes if applicable]", max_length=5000)
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Specimensreceivedcovid19
            fields = '__all__'


class Specimensruncovid19Form(forms.ModelForm):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")    
    reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")
    dateofrecord = models.CharField()

    #Roche
    testsdoneabbottrun = forms.IntegerField(label="run")
    testsdoneabbottfailedbuteligibaleforrepeat= forms.IntegerField(label="Failed but elible for repeat")
    testsdoneabbottfailedbutnoteligibaleforrepeat= forms.IntegerField(label="failed but not eligible for repeat")
    testsdoneabbottrepeat= forms.IntegerField(label="Repeat")

    testsdonebmxrun = forms.IntegerField(label="run")
    testsdonebmxfailedbuteligibaleforrepeat= forms.IntegerField(label="Failed but elible for repeat")
    testsdonebmxfailedbutnoteligibaleforrepeat= forms.IntegerField(label="failed but not eligible for repeat")
    testsdonebmxrepeat= forms.IntegerField(label="Repeat")

    # genexpert
    testsdonegenexpertrun = forms.IntegerField(label="run")
    testsdonegenexpertfailedbuteligibaleforrepeat= forms.IntegerField(label="Failed but elible for repeat")
    testsdonegenexpertfailedbutnoteligibaleforrepeat= forms.IntegerField(label="failed but not eligible for repeat")
    testsdonegenexpertrepeat= forms.IntegerField(label="Repeat")
# quantstudio3
    testsdonequantstudio3run = forms.IntegerField(label="run")
    testsdonequantstudio3failedbuteligibaleforrepeat= forms.IntegerField(label="Failed but elible for repeat")
    testsdonequantstudio3failedbutnoteligibaleforrepeat= forms.IntegerField(label="failed but not eligible for repeat")
    testsdonequantstudio3repeat= forms.IntegerField(label="Repeat")
# hologicpanther
    testsdonehologicpantherrun = forms.IntegerField(label="run")
    testsdonehologicpantherfailedbuteligibaleforrepeat= forms.IntegerField(label="Failed but elible for repeat")
    testsdonehologicpantherfailedbutnoteligibaleforrepeat= forms.IntegerField(label="failed but not eligible for repeat")
    testsdonehologicpantherrepeat= forms.IntegerField(label="Repeat")
# RDT
    testsdonerdtabrun = forms.IntegerField(label="run")
    testsdonerdtabfailedbuteligibaleforrepeat= forms.IntegerField(label="Failed but elible for repeat")
    testsdonerdtabfailedbutnoteligibaleforrepeat= forms.IntegerField(label="failed but not eligible for repeat")
    testsdonerdtabrepeat= forms.IntegerField(label="Repeat")

    testsdonerdtagrun = forms.IntegerField(label="run")
    testsdonerdtagfailedbuteligibaleforrepeat= forms.IntegerField(label="Failed but elible for repeat")
    testsdonerdtagfailedbutnoteligibaleforrepeat= forms.IntegerField(label="failed but not eligible for repeat")
    testsdonerdtagrepeat = forms.IntegerField(label="Repeat")

    totaltestsdone = forms.IntegerField(label="Total Tests Done")
    totalrepeats = forms.IntegerField( label="Total Repeats")
    totalpatientsrun = forms.IntegerField(label="Total Patients Run")

    errorratesabbott = forms.IntegerField(label="Abbot")
    errorratesbmx = forms.IntegerField(label="BMX")
    errorratesgenexpert = forms.IntegerField(label="GeneXper")
    errorratesquantstudio3 = forms.IntegerField(label="Quant Studio3")
    errorrateshologicpanther = forms.IntegerField(label="Hologic panther")
    errorratesrdtab = forms.IntegerField(label="RDT(Antibody")
    errorratesrdtag = forms.IntegerField(label="RDT(Antigen)")

    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Specimensruncovid19
            fields = '__all__'

            
class machinedowntimereagentstockouttoolcovid19Form(forms.ModelForm):


    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")
    dateofrecord = forms.DateField()
    reportingweek = forms.CharField()

    numberofmachinebreakdownsabbott = forms.IntegerField(label="Abbott")
    numberofmachinebreakdownsbmx = forms.IntegerField(label="BMX")
    numberofmachinebreakdownsgenexpert = forms.IntegerField(label="GeneXpert")
    numberofmachinebreakdownsquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    numberofmachinebreakdownshologicpanther = forms.IntegerField(label="Hologic Panther")
    numberofmachinebreakdownscomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )


    machinedowntimedaysabbott = forms.IntegerField(label="Abbott")
    machinedowntimedaysbmx = forms.IntegerField(label="BMX")
    machinedowntimedaysgenexpert = forms.IntegerField(label="GeneXpert")
    machinedowntimedaysquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    machinedowntimedayshologicpanther = forms.IntegerField(label="Hologic Panther")
    machinedowntimedayscomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )


    reagentstockoutabbort = forms.IntegerField(label="Abbott")
    reagentstockoutbms = forms.IntegerField(label="BMX")
    reagentstockoutgenexpert = forms.IntegerField(label="GeneXpert")
    reagentstockoutquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    reagentstockouthologicpanther = forms.IntegerField(label="Hologic Panther")
    reagentstockoutcomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = machinedowntimereagentstockouttoolcovid19
            fields = '__all__'




#not being used ryt now
class machinecovid19Form(forms.ModelForm):


    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please")    #reportingweek = forms.CharField(label="Reporting week in the format  1:3-10")

    numberofmachinebreakdownsabbott = forms.IntegerField(label="Abbott")
    numberofmachinebreakdownsbmx = forms.IntegerField(label="BMX")
    numberofmachinebreakdownsgenexpert = forms.IntegerField(label="GeneXpert")
    numberofmachinebreakdownsquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    numberofmachinebreakdownshologicpanther = forms.IntegerField(label="Hologic Panther")
    numberofmachinebreakdownscomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )


    machinedowntimedaysabbott = forms.IntegerField(label="Abbott")
    machinedowntimedaysbmx = forms.IntegerField(label="BMX")
    machinedowntimedaysgenexpert = forms.IntegerField(label="GeneXpert")
    machinedowntimedaysquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    machinedowntimedayshologicpanther = forms.IntegerField(label="Hologic Panther")
    machinedowntimedayscomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )


    reagentstockoutabbort = forms.IntegerField(label="Abbott")
    reagentstockoutbms = forms.IntegerField(label="BMX")
    reagentstockoutgenexpert = forms.IntegerField(label="GeneXpert")
    reagentstockoutquantstudio3 = forms.IntegerField(label="Quant Studio 3")
    reagentstockouthologicpanther = forms.IntegerField(label="Hologic Panther")
    reagentstockoutcomments = forms.CharField(label="comments", widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, )
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = machinedowntimereagentstockouttoolcovid19
            fields = '__all__'



 # ---------------------------------------------------------------------------------------------------------------------------------- 

# class Top_brti_weeklyForm(forms.ModelForm):
#     reporting_week = forms.CharField(label="Reporting week", max_length=20)
#     month = forms.CharField(label="Month", max_length=20)
#     laboratory = forms.CharField(label="laboratory", max_length=20)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.formclass = 'form-horizontal'
#         self.helper.fieldclass = 'col-sm-6'
#         self.helper.labelclass = 'col-sm-6'
#         self.helper.layout = Layout(
#         )

#     class Meta:
#             model = Top_brti_weekly
#             fields = '__all__'

 # ----------------------------------------------------------------------------------------------------------------------------------

# class TopbrtiweeklyForm(forms.ModelForm):
#     #reportingweek = forms.CharField(label="Reporting week", max_length=20)
#     month = forms.CharField(label="Month", max_length=20)
#     laboratory = forms.CharField(label="laboratory", max_length=20)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.formclass = 'form-horizontal'
#         self.helper.fieldclass = 'col-sm-6'
#         self.helper.labelclass = 'col-sm-6'
#         self.helper.layout = Layout(
#         )

    class Meta:
            # model = Topbrtiweekly
            fields = '__all__'

class Generalcovid19Form(forms.ModelForm):
    dayschoices=[
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    dayofweek = forms.ChoiceField(choices=dayschoices, initial="none", label="Select Day please") 
    reportingweek = forms.CharField(initial='1')
    dateofrecord = forms.CharField(initial=datetime.date.today())


    commentsregardingtestingandchallengesfacedbythelaboratory = forms.CharField( label="comments")
    numberofstaffwhotestedpositivetocovid19atvllab	= forms.IntegerField(label="number of staff who tested positive at vl lab")
    numberOfStaffwhotestedpositivetocovid19athubs= forms.IntegerField(label="number Of Staff who tested positive to covid19 at hubs")
    numberofstaffwhohavebeenvaccinated	= forms.IntegerField(label="number of staff who have been vaccinated")
    Comments =forms.CharField( label="comments")
    Requesttobrtifromthelaboratory	= forms.CharField(label="Request to brti from the laboratory")
    user= forms.CharField(initial='123')
    lab= forms.CharField(initial='123')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )

    class Meta:
            model = Generalcovid19
            fields = '__all__'
            exclude=('dateofentry',)