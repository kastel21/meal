from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit



 # ---------------------------------------------------------------------------------------------------------------------------------- 

#masving_brti_vl_weekly_statistics_tool_31-6_june_2021

class Specimens_run_brti_vl_weeklyForm(forms.ModelForm):

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
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Specimens_run_brti_vl_weekly
            fields = '__all__'

class Specimens_recieved_brti_vl_weeklyForm(forms.ModelForm):
    day_of_week = forms.CharField(max_length=20)


    samples_carried_over_previous_week_never_tested_plasma = forms.IntegerField(label="Plasma")
    samples_carried_over_previous_week_never_tested_dbs = forms.IntegerField(label="DBS")

    samples_carried_over_previous_previous_failed_samples_plasma = forms.IntegerField(label="Plasma")
    samples_carried_over_previous_previous_failed_samples_dbs = forms.IntegerField(label="DBS")


    samples_received_current_week_plasma = forms.IntegerField(label="Plasma")
    samples_received_current_week_dbs = forms.IntegerField(label="DBS")

    samples_rejected_current_week_plasma = forms.IntegerField(label="Plasma")
    samples_rejected_current_week_dbs = forms.IntegerField(label="DBS")


    total_samples_received_current_week_plasma = forms.IntegerField(label="Plasma")
    total_samples_received_current_week_dbs = forms.IntegerField(label="DBS")

    number_of_samples_entered_into_lims_on_day_of_arrival_plasma = forms.IntegerField(label="Plasma")
    number_of_samples_entered_into_lims_on_day_of_arrival_dbs = forms.IntegerField(label="DBS")


    number_of_samples_entered_into_lims_after_day_of_arrival_plasma = forms.IntegerField(label="Plasma")
    number_of_samples_entered_into_lims_after_day_of_arrival_dbs = forms.IntegerField(label="DBS")

    number_of_hours_lims_was_functional = forms.IntegerField(label="# of hours LIMS was Functional")

    total_samples_current_and_carryover_plasma = forms.IntegerField(label="Plasma")
    total_samples_current_and_carryover_dbs = forms.IntegerField(label="DBS")

    samples_reffered_plasma = forms.IntegerField(label="Plasma")
    samples_reffered_dbs = forms.IntegerField(label="DBS")

    lab_samples_reffered_to = forms.IntegerField(label="Lab Samples Referred to")

    percentage_rejection_rate_plasma = forms.DecimalField(label="Plasma", decimal_places=5,  max_digits=5)
    percentage_rejection_rate_dbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)


    number_of_results_printed_from_lims_plasma = forms.IntegerField(label="Plasma")
    number_of_results_printed_from_lims_dbs = forms.IntegerField(label="DBS")

    total_results_dispatched_by_lab_plasma	= forms.IntegerField(label="Plasma")
    total_results_dispatched_by_lab_dbs	= forms.IntegerField(label="DBS")

    total_results_dispatched_by_lab_via_sms_plasma	= forms.IntegerField(label="Plasma")
    total_results_dispatched_by_lab_via_sms_dbs	= forms.IntegerField(label="DBS")



    reasons_for_rejections_sample_quality_compromised_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_dbs = forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_sample_quality_insufficient_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_sample_quality_insufficient_dbs = forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_sample_information_mismatch_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_sample_information_mismatch_dbs = forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_sample_or_request_form_missing_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_sample_or_request_form_missing_dbs = forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_qda_check_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_qda_check_dbs = forms.IntegerField(label="DBS")


    reasons_for_sample_refferal_reagent_or_kit_stockout_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_reagent_or_kit_stockout_dbs= forms.IntegerField(label="DBS")


    reasons_for_sample_refferal_instrument_mechanical_failure_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_instrument_mechanical_failure_dbs= forms.IntegerField(label="DBS")

    reasons_for_sample_refferal_insufficient_instrument_capacity_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_insufficient_instrument_capacity_dbs= forms.IntegerField(label="DBS")

    reasons_for_sample_refferal_insufficient_hr_capacity_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_insufficient_hr_capacity_dbs= forms.IntegerField(label="DBS")

    reasons_for_sample_refferal_dqa_check_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_dqa_check_dbs= forms.IntegerField(label="DBS")

    comments=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), label="Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=5000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Specimens_recieved_brti_vl_weekly
            fields = '__all__'

class Reasons_for_failure_brti_vl_weeklyForm(forms.ModelForm):

    day_of_week = forms.CharField(max_length=20)

#roche
    roche_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    roche_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    roche_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    roche_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    roche_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    roche_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    roche_plasma_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    roche_dqa_check_plasma = forms.IntegerField(label="DQA check")

    roche_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    roche_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    roche_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    roche_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    roche_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    roche_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    roche_dbs_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    roche_dqa_check_dbs = forms.IntegerField(label="DQA check")

#bmx

    bmx_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmx_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmx_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmx_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    bmx_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmx_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    bmx_plasma_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    bmx_dqa_check_plasma = forms.IntegerField(label="DQA check")

    bmx_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmx_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmx_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmx_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    bmx_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmx_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    bmx_dbs_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    bmx_dqa_check_dbs = forms.IntegerField(label="DQA check")

#abbott

    abbott_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbott_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbott_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbott_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    abbott_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbott_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    abbott_plasma_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    abbott_dqa_check_plasma = forms.IntegerField(label="DQA check")

    abbott_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbott_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbott_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbott_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    abbott_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbott_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    abbott_dbs_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    abbott_dqa_check_dbs = forms.IntegerField(label="DQA check")

#Hologic Panther

    hologic_panther_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologic_panther_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologic_panther_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologic_panther_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    hologic_panther_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologic_panther_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    hologic_panther_plasma_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    hologic_panther_dqa_check_plasma = forms.IntegerField(label="DQA check")

    hologic_panther_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologic_panther_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologic_panther_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologic_panther_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    hologic_panther_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologic_panther_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    hologic_panther_dbs_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    hologic_panther_dqa_check_dbs = forms.IntegerField(label="DQA check")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Reasons_for_failure_brti_vl_weekly
            fields = '__all__'

class Electric_outage_brti_vl_weeklyForm(forms.ModelForm):
    day_of_week = forms.CharField(max_length=20)


    number_of_hours_with_no_electricity_per_day	= forms.IntegerField(label="Number of hours with no electricity per day")
    number_of_hours_generator_was_on_per_day	= forms.IntegerField(label="Number of hours generator was on per day")
    litres_of_fuel_added_to_generator_per_day	= forms.IntegerField(label="Litres of Fuel added to generator per day")
    number_of_hours_machines_was_not_being_used_due_to_power_cut_per_day	= forms.IntegerField(label="Number of hours machine/s was not being used due to power cut per day<")
    total_tests_done_per_day_using_generator	= forms.IntegerField(label="Total Tests done per day using generator")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Electric_outage_brti_vl_weekly
            fields = '__all__'
 # ---------------------------------------------------------------------------------------------------------------------------------- 

#masving_brti_weekly_statistics_tool_31-6_june_2021


class Specimens_run_brti_weekly(forms.ModelForm):
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
    tests_done_abbott_failed_but_not_eligibale_for_repeat_plasma= forms.IntegerField(label="Failed but not eligible for repeat")
    tests_done_abbott_repeat_plasma= forms.IntegerField(label="Repeat")
    tests_done_abbott_failed_after_repeat_testing_plasma = forms.IntegerField(label="Failed After Repeat Testing")


    tests_done_abbott_number_of_samples_received_this_week_dbs = forms.IntegerField(label="Run (Number of samples received this week)")
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_dbs = forms.IntegerField(label="Run (Number of Carry Over Samples from previous weeks)")
    tests_done_abbott_failed_but_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed but eligible for repeat")
    tests_done_abbott_failed_but_not_eligibale_for_repeat_dbs= forms.IntegerField(label="Failed but not eligible for repeat")
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


    total_ncs_from_audit=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, label="Total NCs from Audit (exchange audits)")
    ncs_not_yet_closed=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=5000, label="NCs not yet closed")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Specimens_run_brti_weekly
            fields = '__all__'


class Specimens_received_brti_weeklyForm(forms.ModelForm):
    date_of_week= forms.IntegerField()

    samples_carried_over_previous_weeks_never_tested_plasma = forms.IntegerField(label="Plasma")
    samples_carried_over_previous_weeks_never_tested_dbs = forms.IntegerField(label="DBS")

    samples_carried_over_previous_failed_samples_plasma = forms.IntegerField(label="Plasma")
    samples_carried_over_previous_failed_samples_dbs = forms.IntegerField(label="DBS")



    samples_received_current_week_plasma = forms.IntegerField(label="Plasma")
    samples_received_current_week_dbs = forms.IntegerField(label="DBS")

    samples_rejected_current_week_plasma = forms.IntegerField(label="Plasma")
    samples_rejected_current_week_dbs = forms.IntegerField(label="DBS")
    
    total_samples_received_current_week_plasma = forms.IntegerField(label="Plasma")
    total_samples_received_current_week_dbs = forms.IntegerField(label="DBS")

    number_of_samples_entered_into_lims_on_day_of_arrival_plasma = forms.IntegerField(label="Plasma")
    number_of_samples_entered_into_lims_on_day_of_arrival_dbs = forms.IntegerField(label="DBS")

    number_of_samples_entered_into_lims_after_day_of_arrival_plasma = forms.IntegerField(label="Plasma")
    number_of_samples_entered_into_lims_after_day_of_arrival_dbs = forms.IntegerField(label="DBS")

    number_of_hours_lims_was_functional	 = forms.IntegerField(label="# of hours LIMS was Functional")

    total_samples_current_plus_carryover_plasma= forms.IntegerField(label="Plasma")
    total_samples_current_plus_carryover_dbs= forms.IntegerField(label="DBS")

    samples_reffered_plasma = forms.IntegerField(label="Plasma")
    samples_reffered_dbs = forms.IntegerField(label="DBS")

    lab_samples_reffered_to = forms.IntegerField(label="Lab Samples Referred to")

    percentage_rejection_rate_plasma = forms.DecimalField(label="Plasma",decimal_places=5,  max_digits=5)
    percentage_rejection_rate_dbs = forms.DecimalField(label="DBS", decimal_places=5,  max_digits=5)


    number_of_results_printed_from_lims_plasma = forms.IntegerField(label="Plasma")
    number_of_results_printed_from_lims_dbs = forms.IntegerField(label="DBS")

    total_results_dispatched_by_lab_plasma	= forms.IntegerField(label="Plasma")
    total_results_dispatched_by_lab_dbs	= forms.IntegerField(label="DBS")

    total_results_dispatched_by_lab_via_sms_plasma	= forms.IntegerField(label="Plasma")
    total_results_dispatched_by_lab_via_sms_dbs	= forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_dbs = forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_sample_quality_insufficient_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_sample_quality_insufficient_dbs = forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_sample_information_mismatch_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_sample_information_mismatch_dbs = forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_sample_or_request_form_missing_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_sample_or_request_form_missing_dbs = forms.IntegerField(label="DBS")


    reasons_for_rejections_sample_quality_compromised_qda_check_plasma = forms.IntegerField(label="Plasma")
    reasons_for_rejections_sample_quality_compromised_qda_check_dbs = forms.IntegerField(label="DBS")


    reasons_for_sample_refferal_reagent_or_kit_stockout_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_reagent_or_kit_stockout_dbs= forms.IntegerField(label="DBS")


    reasons_for_sample_refferal_instrument_mechanical_failure_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_instrument_mechanical_failure_dbs= forms.IntegerField(label="DBS")

    reasons_for_sample_refferal_insufficient_instrument_capacity_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_insufficient_instrument_capacity_dbs= forms.IntegerField(label="DBS")

    reasons_for_sample_refferal_insufficient_hr_capacity_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_insufficient_hr_capacity_dbs= forms.IntegerField(label="DBS")

    reasons_for_sample_refferal_dqa_check_plasma= forms.IntegerField(label="Plasma")
    reasons_for_sample_refferal_dqa_check_dbs= forms.IntegerField(label="DBS")

    comments=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), label=" Comments: Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=5000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Specimens_received_brti_weekly
            fields = '__all__'


class Reasons_for_failure_brti_weeklyForm(forms.ModelForm):

    day_of_week = forms.CharField(max_length=20)
#roche
    roche_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    roche_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    roche_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    roche_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    roche_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    roche_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    roche_plasma_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    roche_dqa_check_plasma = forms.IntegerField(label="DQA check")

    roche_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    roche_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    roche_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    roche_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    roche_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    roche_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    roche_dbs_number_of_failed_tests_due_to_other = forms.IntegerField()
    roche_dqa_check_dbs = forms.IntegerField(label="DQA check")

#bmx

    bmx_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmx_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmx_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmx_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    bmx_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmx_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    bmx_plasma_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    bmx_dqa_check_plasma = forms.IntegerField(label="DQA check")

    bmx_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    bmx_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    bmx_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    bmx_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    bmx_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    bmx_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    bmx_dbs_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    bmx_dqa_check_dbs = forms.IntegerField(label="DQA check")



#abbott

    abbott_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbott_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbott_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbott_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    abbott_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbott_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    abbott_plasma_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    abbott_dqa_check_plasma = forms.IntegerField(label="DQA check")

    abbott_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    abbott_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    abbott_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    abbott_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    abbott_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    abbott_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    abbott_dbs_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    abbott_dqa_check_dbs = forms.IntegerField(label="DQA check")




#Hologic Panther

    hologic_panther_plasma_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologic_panther_plasma_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologic_panther_plasma_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologic_panther_plasma_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    hologic_panther_plasma_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologic_panther_plasma_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    hologic_panther_plasma_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    hologic_panther_dqa_check_plasma = forms.IntegerField(label="DQA check")

    hologic_panther_dbs_number_of_failed_tests_due_to_sample_quality_issues = forms.IntegerField(label="# of failed tests due to sample quality issues")
    hologic_panther_dbs_number_of_failed_tests_due_to_reagent_quality_issues = forms.IntegerField(label="# of failed tests due to reagent quality issues")
    hologic_panther_dbs_number_of_failed_tests_due_to_due_to_qc_failure = forms.IntegerField(label="# of failed tests due to QC failure")
    hologic_panther_dbs_number_of_failed_tests_due_to_power_failure = forms.IntegerField(label="# of failed tests due to power failure")
    hologic_panther_dbs_number_of_failed_tests_due_to_mechanical_failure = forms.IntegerField(label="# of failed tests due to mechanical failure")
    hologic_panther_dbs_number_of_failed_tests_due_to_processing_error = forms.IntegerField(label="Processing Error")
    hologic_panther_dbs_number_of_failed_tests_due_to_other = forms.IntegerField(label="Other Specify")
    hologic_panther_dqa_check_dbs = forms.IntegerField(label="DQA check")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Reasons_for_failure_brti_weekly
            fields = '__all__'

class Electric_outage_brti_weeklyForm(forms.ModelForm):
    day_of_week = forms.CharField(max_length=20)


    number_of_hours_with_no_electricity_per_day	= forms.IntegerField(label="Number of hours with no electricity per day")
    number_of_hours_generator_was_on_per_day	= forms.IntegerField(label="Number of hours generator was on per day")
    litres_of_fuel_added_to_generator_per_day	= forms.IntegerField(label="Litres of Fuel added to generator per day")
    number_of_hours_machines_was_not_being_used_due_to_power_cut_per_day	= forms.IntegerField(label="Number of hours machine/s was not being used due to power cut per day")
    total_tests_done_per_day_using_generator	= forms.IntegerField(label="Total Tests done per day using generator")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = Electric_outage_brti_weekly
            fields = '__all__'

 # ----------------------------------------------------------------------------------------------------------------------------------         
 #General Info masvingo brti_covid_19_weekly_statistics_tool


class General_info_covid_19Form(forms.ModelForm):
    general_comments_regarding_testing_and_challenges_faced_by_the_laboratory = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), label="General comments regarding testing and challenges (interruptions) faced by the laboratory", max_length=5000)
   
    number_of_staff_who_tested_positive_to_covid_19_at_vl_lab=forms.IntegerField(label="# of staff who tested positive to Covid 19 at VL lab")
    number_of_staff_who_have_been_vaccinated	= forms.IntegerField( label="# of staff who have been vaccinated")
    number_Of_Staff_who_tested_positive_to_COVID_19_at_Hubs=forms.IntegerField(label="# Of Staff  who tested positive to COVID 19 at Hubs")
    Comments =forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), label="Comment (Please specify the occupation of the person  who has tested postive.Riders are also included )", max_length=5000)
   
    Request_to_brti_from_the_laboratory	= forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), label="Request to BRTI from the Laboratory", max_length=5000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-6' 
        self.helper.layout = Layout(
        )
        
    class Meta:
            model = General_info_covid_19
            fields = '__all__'

 # ---------------------------------------------------------------------------------------------------------------------------------- 

