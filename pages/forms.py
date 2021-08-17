from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit



 # ---------------------------------------------------------------------------------------------------------------------------------- 

#masving_brti_vl_weekly_statistics_tool_31-6_june_2021

class Specimens_runForm(forms.ModelForm):

    day_of_week = forms.CharField(max_length=20)

#Roche
    tests_done_roche_number_of_samples_received_this_week_plasma = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_roche_number_of_samples_carried_over_previous_weeks_plasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_roche_failed_but_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_roche_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed not eligible for repeat")
    tests_done_roche_repeat_plasma= forms.IntegerField(label="Repeat")
    tests_done_roche_failed_after_repeat_testing_plasma = forms.IntegerField(label="Failed After Repeat Testing")


    tests_done_roche_number_of_samples_received_this_week_dbs = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_roche_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_roche_failed_but_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_roche_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed not eligible for repeat")
    tests_done_roche_repeat_dbs= forms.IntegerField(label="Repeat")
    tests_done_roche_failed_after_repeat_testing_dbs = forms.IntegerField(label="Failed After Repeat Testing")
#BMX
    tests_done_bmx_number_of_samples_received_this_week_plasma = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_bmx_number_of_samples_carried_over_previous_weeks_plasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_bmx_failed_but_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_bmx_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed not eligible for repeat")
    tests_done_bmx_repeat_plasma= forms.IntegerField(label="Repeat")
    tests_done_bmx_failed_after_repeat_testing_plasma = forms.IntegerField(label="Failed After Repeat Testing")


    tests_done_bmx_number_of_samples_received_this_week_dbs = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_bmx_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_bmx_failed_but_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_bmx_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed not eligible for repeat")
    tests_done_bmx_repeat_dbs= forms.IntegerField(label="Repeat")
    tests_done_bmx_failed_after_repeat_testing_dbs = forms.IntegerField(label="Failed After Repeat Testing")

#Abbott
    tests_done_abbott_number_of_samples_received_this_week_plasma = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_plasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_abbott_failed_but_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_abbott_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed not eligible for repeat")
    tests_done_abbott_repeat_plasma= forms.IntegerField(label="Repeat")
    tests_done_abbott_failed_after_repeat_testing_plasma = forms.IntegerField(label="Failed After Repeat Testing")


    tests_done_abbott_number_of_samples_received_this_week_dbs = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_abbott_failed_but_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_abbott_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed not eligible for repeat")
    tests_done_abbott_repeat_dbs= forms.IntegerField(label="Repeat")
    tests_done_abbott_failed_after_repeat_testing_dbs = forms.IntegerField(label="Failed After Repeat Testing")

#Hologic Panther
    tests_done_hologic_panther_number_of_samples_received_this_week_plasma = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_hologic_panther_number_of_samples_carried_over_previous_weeks_plasma = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_hologic_panther_failed_but_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed not eligible for repeat")
    tests_done_hologic_panther_repeat_plasma= forms.IntegerField(label="Repeat")
    tests_done_hologic_panther_failed_after_repeat_testing_plasma = forms.IntegerField(label="Failed After Repeat Testing")


    tests_done_hologic_panther_number_of_samples_received_this_week_dbs = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_hologic_panther_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_hologic_panther_failed_but_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed not eligible for repeat")
    tests_done_hologic_panther_repeat_dbs= forms.IntegerField(label="Repeat")
    tests_done_hologic_panther_failed_after_repeat_testing_dbs = forms.IntegerField(label="Failed After Repeat Testing")

    total_tests_done = forms.IntegerField(label="Total Tests Done")
    total_repeats = forms.IntegerField(label="Total Repeats")
    total_patients_run = forms.IntegerField(label="Total Patients Run")
    targets_weekly = forms.IntegerField(label="Target:Weekly")
    percentage_targets_achievements = forms.DecimalField(label="%Target Achievement", decimal_places=5,  max_digits=5)


    percentage_error_rate_roche_plasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentage_error_rate_roche_dbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)

    percentage_error_rate_bmx_plasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentage_error_rate_bmx_dbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5) 

    percentage_error_rate_abbott_plasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentage_error_rate_abbott_dbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5) 

    percentage_error_rate_hologic_panther_plasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentage_error_rate_hologic_panther_dbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5) 


    total_ncs_from_audit=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=300, label="Total NCs from Audit (exchange audits)")
    ncs_not_yet_closed=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=300, label="NCs not yet closed")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-3'
        self.helper.label_class = 'col-lg-9' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Specimens_run
            fields = '__all__'
 # ----------------------------------------------------------------------------------------------------------------------------------         

class SpecimensrunForm(forms.ModelForm):
    day_of_week = forms.CharField(max_length=20)



#Roche
    tests_done_roche_number_of_samples_received_this_week_plasma = forms.IntegerField()
    tests_done_roche_number_of_samples_carried_over_previous_weeks_plasma = forms.IntegerField()
    tests_done_roche_failed_but_eligibale_for_repeat_plasma= forms.IntegerField()
    tests_done_roche_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField()
    tests_done_roche_repeat_plasma= forms.IntegerField()
    tests_done_roche_failed_after_repeat_testing_plasma = forms.IntegerField()


    tests_done_roche_number_of_samples_received_this_week_dbs = forms.IntegerField()
    tests_done_roche_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField()
    tests_done_roche_failed_but_eligibale_for_repeat_dbs= forms.IntegerField()
    tests_done_roche_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField()
    tests_done_roche_repeat_dbs= forms.IntegerField()
    tests_done_roche_failed_after_repeat_testing_dbs = forms.IntegerField()
#BMX
    tests_done_bmx_number_of_samples_received_this_week_plasma = forms.IntegerField()
    tests_done_bmx_number_of_samples_carried_over_previous_weeks_plasma = forms.IntegerField()
    tests_done_bmx_failed_but_eligibale_for_repeat_plasma= forms.IntegerField()
    tests_done_bmx_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField()
    tests_done_bmx_repeat_plasma= forms.IntegerField()
    tests_done_bmx_failed_after_repeat_testing_plasma = forms.IntegerField()


    tests_done_bmx_number_of_samples_received_this_week_dbs = forms.IntegerField()
    tests_done_bmx_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField()
    tests_done_bmx_failed_but_eligibale_for_repeat_dbs= forms.IntegerField()
    tests_done_bmx_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField()
    tests_done_bmx_repeat_dbs= forms.IntegerField()
    tests_done_bmx_failed_after_repeat_testing_dbs = forms.IntegerField()

#Abbott
    tests_done_abbott_number_of_samples_received_this_week_plasma = forms.IntegerField()
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_plasma = forms.IntegerField()
    tests_done_abbott_failed_but_eligibale_for_repeat_plasma= forms.IntegerField()
    tests_done_abbott_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField()
    tests_done_abbott_repeat_plasma= forms.IntegerField()
    tests_done_abbott_failed_after_repeat_testing_plasma = forms.IntegerField()


    tests_done_abbott_number_of_samples_received_this_week_dbs = forms.IntegerField()
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField()
    tests_done_abbott_failed_but_eligibale_for_repeat_dbs= forms.IntegerField()
    tests_done_abbott_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField()
    tests_done_abbott_repeat_dbs= forms.IntegerField()
    tests_done_abbott_failed_after_repeat_testing_dbs = forms.IntegerField()

#Hologic Panther
    tests_done_hologic_panther_number_of_samples_received_this_week_plasma = forms.IntegerField()
    tests_done_hologic_panther_number_of_samples_carried_over_previous_weeks_plasma = forms.IntegerField()
    tests_done_hologic_panther_failed_but_eligibale_for_repeat_plasma= forms.IntegerField()
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField()
    tests_done_hologic_panther_repeat_plasma= forms.IntegerField()
    tests_done_hologic_panther_failed_after_repeat_testing_plasma = forms.IntegerField()


    tests_done_hologic_panther_number_of_samples_received_this_week_dbs = forms.IntegerField()
    tests_done_hologic_panther_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField()
    tests_done_hologic_panther_failed_but_eligibale_for_repeat_dbs= forms.IntegerField()
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField()
    tests_done_hologic_panther_repeat_dbs= forms.IntegerField()
    tests_done_hologic_panther_failed_after_repeat_testing_dbs = forms.IntegerField()

    total_tests_done = forms.IntegerField()
    total_repeats = forms.IntegerField()
    total_patients_run = forms.IntegerField()
    targets_weekly = forms.IntegerField()
    percentage_targets_achievements = forms.DecimalField(decimal_places=5,  max_digits=5)


    percentage_error_rate_roche_plasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_roche_dbs = forms.DecimalField(decimal_places=5,  max_digits=5)

    percentage_error_rate_bmx_plasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_bmx_dbs = forms.DecimalField(decimal_places=5,  max_digits=5) 

    percentage_error_rate_abbott_plasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_abbott_dbs = forms.DecimalField(decimal_places=5,  max_digits=5) 

    percentage_error_rate_hologic_panther_plasma = forms.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_hologic_panther_dbs = forms.DecimalField(decimal_places=5,  max_digits=5) 


    total_ncs_from_audit=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)
    ncs_not_yet_closed=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000)



class Electric_outageForm(forms.ModelForm):
    day_of_week = forms.CharField(max_length=20)


    number_of_hours_with_no_electricity_per_day	= forms.IntegerField()
    number_of_hours_generator_was_on_per_day	= forms.IntegerField()
    litres_of_fuel_added_to_generator_per_day	= forms.IntegerField()
    number_of_hours_machines_was_not_being_used_due_to_power_cut_per_day	= forms.IntegerField()
    total_tests_done_per_day_using_generator	= forms.IntegerField()


class Reasons_for_failureForm(forms.ModelForm):
    day_of_week = forms.CharField(max_length=20)
#roche
    roche_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_other = forms.IntegerField()
    dqa_check_plasma = forms.IntegerField()

    roche_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_other = forms.IntegerField()
    roche_dqa_check_dbs = forms.IntegerField()

#bmx

    bmx_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_other = forms.IntegerField()
    bmx_dqa_check_plasma = forms.IntegerField()

    bmx_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_other = forms.IntegerField()
    bmx_dqa_check_dbs = forms.IntegerField()



#abbott

    abbott_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_other = forms.IntegerField()
    abbott_dqa_check_plasma = forms.IntegerField()

    abbott_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_other = forms.IntegerField()
    abbott_dqa_check_dbs = forms.IntegerField()




#Hologic Panther

    hologic_panther_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_other = forms.IntegerField()
    hologic_panther_dqa_check_plasma = forms.IntegerField()

    hologic_panther_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_other = forms.IntegerField()
    hologic_panther_dqa_check_dbs = forms.IntegerField()



#General Info


class General_infoForm(forms.ModelForm):
    general_comments_regarding_testing_and_challenges_faced_by_the_laboratory = forms.CharField( max_length=5000)
    number_of_staff_who_tested_positive_to_covid_19_at_vl_lab	= forms.IntegerField()
    number_of_staff_who_have_been_vaccinated	= forms.IntegerField()
    Comments =forms.CharField( max_length=5000)
    Request_to_brti_from_the_laboratory	= forms.CharField( max_length=5000)




class Specimens_received_covid19Form(forms.ModelForm):
    samples_carried_over_previous_weeks	= forms.IntegerField()

    samples_received_current_week_nasopharyngeal_swab = forms.IntegerField()
    samples_received_current_week_nasal_swab = forms.IntegerField()
    samples_received_current_week_oropharyngeal_swab = forms.IntegerField()
    samples_received_current_week_midturbinate_swab = forms.IntegerField()
    samples_received_current_week_sputum = forms.IntegerField()
    samples_received_current_week_whole_blood_or_plasma_or_serum = forms.IntegerField()
    samples_received_current_week_other = forms.IntegerField()


    samples_rejected_current_week =	forms.IntegerField()
    total_samples_received_current_week	=	forms.IntegerField()

    number_of_samples_entered_into_lims =	forms.IntegerField()
    total_samples_current_plus_carryover	 =	forms.IntegerField()
    samples_referred	=	forms.IntegerField()
    rejection_rate_current_week = forms.DecimalField(decimal_places=5,  max_digits=5)
    number_of_results_printed_lims =	forms.IntegerField()
    total_results_dispatched_by_lab	=	forms.IntegerField()
    comment= forms.CharField( max_length=5000)

class Machine_downtime_Reagent_stock_out_tool_covid19Form(forms.ModelForm):
    machine_breakdown_number_abbott	=	forms.IntegerField()
    machine_breakdown_number_bmx	=	forms.IntegerField()
    machine_breakdown_number_genexpert	=	forms.IntegerField()
    machine_breakdown_number_quant_studio_3	=	forms.IntegerField()
    machine_breakdown_number_hologic_panther	=	forms.IntegerField()
    machine_breakdown_number_comments	= forms.CharField( max_length=5000)

    machine_downtime_days_abbott = 	forms.IntegerField()
    machine_downtime_days_bmx = 	forms.IntegerField()
    machine_downtime_days_genexpert = 	forms.IntegerField()
    machine_downtime_days_quant_studio_3 = 	forms.IntegerField()
    machine_downtime_days_hologic_panther = 	forms.IntegerField()
    machine_downtime_days_comments = 	forms.CharField( max_length=5000)

    #reagent_stockout	

    reagent_stockout_abbott = 	forms.IntegerField()
    reagent_stockout_bmx = 	forms.IntegerField()
    reagent_stockout_genexpert = 	forms.IntegerField()
    reagent_stockout_quant_studio_3 = 	forms.IntegerField()
    reagent_stockout_hologic_panther = 	forms.IntegerField()
    reagent_stockout_comments = 	forms.CharField( max_length=5000)




class Specimens_run_covid19Form(forms.ModelForm):
    #Roche
    tests_done_abbott_run = forms.IntegerField()
    tests_done_abbott_failed_but_eligibale_for_repeat= forms.IntegerField()
    tests_done_abbott_failed_but_not_eligibale_for_repeat= forms.IntegerField()
    tests_done_abbott_repeat= forms.IntegerField()


    tests_done_bmx_run = forms.IntegerField()
    tests_done_bmx_failed_but_eligibale_for_repeat= forms.IntegerField()
    tests_done_bmx_failed_but_not_eligibale_for_repeat= forms.IntegerField()
    tests_done_bmx_repeat= forms.IntegerField()

    # genexpert
    tests_done_genexpert_run = forms.IntegerField()
    tests_done_genexpert_failed_but_eligibale_for_repeat= forms.IntegerField()
    tests_done_genexpert_failed_but_not_eligibale_for_repeat= forms.IntegerField()
    tests_done_genexpert_repeat= forms.IntegerField()
# quant_studio_3
    tests_done_quant_studio_3_run = forms.IntegerField()
    tests_done_quant_studio_3_failed_but_eligibale_for_repeat= forms.IntegerField()
    tests_done_quant_studio_3_failed_but_not_eligibale_for_repeat= forms.IntegerField()
    tests_done_quant_studio_3_repeat= forms.IntegerField()
# hologic_panther	
    tests_done_hologic_panther_run = forms.IntegerField()
    tests_done_hologic_panther_failed_but_eligibale_for_repeat= forms.IntegerField()
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat= forms.IntegerField()
    tests_done_hologic_panther_repeat= forms.IntegerField()
# RDT
    tests_done_rdt_ab_run = forms.IntegerField()
    tests_done_rdt_ab_failed_but_eligibale_for_repeat= forms.IntegerField()
    tests_done_rdt_ab_failed_but_not_eligibale_for_repeat= forms.IntegerField()
    tests_done_rdt_ab_repeat= forms.IntegerField()

    tests_done_rdt_ag_run = forms.IntegerField()
    tests_done_rdt_ag_failed_but_eligibale_for_repeat= forms.IntegerField()
    tests_done_rdt_ag_failed_but_not_eligibale_for_repeat= forms.IntegerField()
    tests_done_rdt_ag_repeat= forms.IntegerField()


    total_tests_done = forms.IntegerField()
    total_repeats = forms.IntegerField()
    total_patients_run = forms.IntegerField()


    error_rates_abbott = forms.IntegerField()
    error_rates_bmx = forms.IntegerField()
    error_rates_genexpert = forms.IntegerField()
    error_rates_quant_studio_3 = forms.IntegerField()
    error_rates_hologic_panther = forms.IntegerField()
    error_rates_rdt_ab = forms.IntegerField()
    error_rates_rdt_ag = forms.IntegerField()

# ---------------------------------------------------------------------------------------------------------------------------------- 
  # ---------------------------------------------------------------------------------------------------------------------------------- 
   # ---------------------------------------------------------------------------------------------------------------------------------- 