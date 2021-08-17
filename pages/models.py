from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse

# Create your models here.

#skip masvingo brti covid weekly


class Record(models.Model):
    courseTitle = models.CharField(max_length=200)
    courseTopic = models.CharField(max_length=200)

    # courseCode = models.CharField(max_length=200, unique=True)
    # courseUnit = models.CharField(max_length=200)
    description = models.TextField()
    #desc = models.TextField( )
    # level = models.CharField(choices=LEVEL, max_length=3, blank=True)
    # semester = models.CharField(choices=SEMESTER, max_length=200)
    is_reviewed = models.BooleanField(default=False, blank=True, null=True)
    email = models.EmailField(default="takaengwa@gmail.com")
    submissionDate = models.DateTimeField(auto_now=True,editable=False)
    owner = models.CharField(max_length=300)

    def __str__(self):
        return self.courseTitle + " (" + self.courseTitle + ")"

    def get_absolute_url(self):
        return reverse('course_list', kwargs={'pk': self.pk})

    def get_total_unit(self):
        t = 0
        total = Course.objects.all()
        for i in total:
            t +=i
        return i


# masving_brti_vl_weekly_statistics_tool_31-6_june_2021
class Specimens_recieved_brti_vl_weekly(models.Model):
    day_of_week = models.CharField(max_length=20,null=False)


    samples_carried_over_previous_week_never_tested_plasma = models.IntegerField()
    samples_carried_over_previous_week_never_tested_dbs = models.IntegerField()

    samples_carried_over_previous_previous_failed_samples_plasma = models.IntegerField()
    samples_carried_over_previous_previous_failed_samples_dbs = models.IntegerField()


    samples_received_current_week_plasma = models.IntegerField()
    samples_received_current_week_dbs = models.IntegerField()

    samples_rejected_current_week_plasma = models.IntegerField()
    samples_rejected_current_week_dbs = models.IntegerField()


    total_samples_received_current_week_plasma = models.IntegerField()
    total_samples_received_current_week_dbs = models.IntegerField()

    number_of_samples_entered_into_lims_on_day_of_arrival_plasma = models.IntegerField()
    number_of_samples_entered_into_lims_on_day_of_arrival_dbs = models.IntegerField()


    number_of_samples_entered_into_lims_after_day_of_arrival_plasma = models.IntegerField()
    number_of_samples_entered_into_lims_after_day_of_arrival_dbs = models.IntegerField()

    number_of_hours_lims_was_functional = models.IntegerField()

    total_samples_current_and_carryover_plasma = models.IntegerField()
    total_samples_current_and_carryover_dbs = models.IntegerField()

    samples_reffered_plasma = models.IntegerField()
    samples_reffered_dbs = models.IntegerField()

    lab_samples_reffered_to = models.IntegerField()

    percentage_rejection_rate_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_rejection_rate_dbs = models.DecimalField(decimal_places=5,  max_digits=5)


    number_of_results_printed_from_lims_plasma = models.IntegerField()
    number_of_results_printed_from_lims_dbs = models.IntegerField()

    total_results_dispatched_by_lab_plasma	= models.IntegerField()
    total_results_dispatched_by_lab_dbs	= models.IntegerField()

    total_results_dispatched_by_lab_via_sms_plasma	= models.IntegerField()
    total_results_dispatched_by_lab_via_sms_dbs	= models.IntegerField()



    reasons_for_rejections_sample_quality_compromised_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_dbs = models.IntegerField()


    reasons_for_rejections_sample_quality_compromised_sample_quality_insufficient_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_sample_quality_insufficient_dbs = models.IntegerField()


    reasons_for_rejections_sample_quality_compromised_sample_information_mismatch_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_sample_information_mismatch_dbs = models.IntegerField()


    reasons_for_rejections_sample_quality_compromised_sample_or_request_form_missing_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_sample_or_request_form_missing_dbs = models.IntegerField()


    reasons_for_rejections_sample_quality_compromised_qda_check_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_qda_check_dbs = models.IntegerField()


    reasons_for_sample_refferal_reagent_or_kit_stockout_plasma= models.IntegerField()
    reasons_for_sample_refferal_reagent_or_kit_stockout_dbs= models.IntegerField()


    reasons_for_sample_refferal_instrument_mechanical_failure_plasma= models.IntegerField()
    reasons_for_sample_refferal_instrument_mechanical_failure_dbs= models.IntegerField()

    reasons_for_sample_refferal_insufficient_instrument_capacity_plasma= models.IntegerField()
    reasons_for_sample_refferal_insufficient_instrument_capacity_dbs= models.IntegerField()

    reasons_for_sample_refferal_insufficient_hr_capacity_plasma= models.IntegerField()
    reasons_for_sample_refferal_insufficient_hr_capacity_dbs= models.IntegerField()

    reasons_for_sample_refferal_dqa_check_plasma= models.IntegerField()
    reasons_for_sample_refferal_dqa_check_dbs= models.IntegerField()

    comments=models.TextField("Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=5000, null=True)

























    def __str__(self):
        return self.courseTitle + " (" + self.courseTitle + ")"

    def get_absolute_url(self):
        return reverse('course_list', kwargs={'pk': self.pk})

    def get_total_unit(self):
        t = 0
        total = Course.objects.all()
        for i in total:
            t +=i
        return i



class Specimens_run_brti_vl_weekly(models.Model):
    day_of_week = models.CharField(max_length=20,null=False)



#Roche
    tests_done_roche_number_of_samples_received_this_week_plasma = models.IntegerField()
    tests_done_roche_number_of_samples_carried_over_previous_weeks_plasma = models.IntegerField()
    tests_done_roche_failed_but_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_roche_failed_but_not_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_roche_repeat_plasma= models.IntegerField()
    tests_done_roche_failed_after_repeat_testing_plasma = models.IntegerField()


    tests_done_roche_number_of_samples_received_this_week_dbs = models.IntegerField()
    tests_done_roche_number_of_samples_carried_over_previous_weeks_dbs = models.IntegerField()
    tests_done_roche_failed_but_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_roche_failed_but_not_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_roche_repeat_dbs= models.IntegerField()
    tests_done_roche_failed_after_repeat_testing_dbs = models.IntegerField()
#BMX
    tests_done_bmx_number_of_samples_received_this_week_plasma = models.IntegerField()
    tests_done_bmx_number_of_samples_carried_over_previous_weeks_plasma = models.IntegerField()
    tests_done_bmx_failed_but_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_bmx_failed_but_not_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_bmx_repeat_plasma= models.IntegerField()
    tests_done_bmx_failed_after_repeat_testing_plasma = models.IntegerField()


    tests_done_bmx_number_of_samples_received_this_week_dbs = models.IntegerField()
    tests_done_bmx_number_of_samples_carried_over_previous_weeks_dbs = models.IntegerField()
    tests_done_bmx_failed_but_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_bmx_failed_but_not_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_bmx_repeat_dbs= models.IntegerField()
    tests_done_bmx_failed_after_repeat_testing_dbs = models.IntegerField()

#Abbott
    tests_done_abbott_number_of_samples_received_this_week_plasma = models.IntegerField()
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_plasma = models.IntegerField()
    tests_done_abbott_failed_but_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_abbott_failed_but_not_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_abbott_repeat_plasma= models.IntegerField()
    tests_done_abbott_failed_after_repeat_testing_plasma = models.IntegerField()


    tests_done_abbott_number_of_samples_received_this_week_dbs = models.IntegerField()
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_dbs = models.IntegerField()
    tests_done_abbott_failed_but_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_abbott_failed_but_not_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_abbott_repeat_dbs= models.IntegerField()
    tests_done_abbott_failed_after_repeat_testing_dbs = models.IntegerField()

#Hologic Panther
    tests_done_hologic_panther_number_of_samples_received_this_week_plasma = models.IntegerField()
    tests_done_hologic_panther_number_of_samples_carried_over_previous_weeks_plasma = models.IntegerField()
    tests_done_hologic_panther_failed_but_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_hologic_panther_repeat_plasma= models.IntegerField()
    tests_done_hologic_panther_failed_after_repeat_testing_plasma = models.IntegerField()


    tests_done_hologic_panther_number_of_samples_received_this_week_dbs = models.IntegerField()
    tests_done_hologic_panther_number_of_samples_carried_over_previous_weeks_dbs = models.IntegerField()
    tests_done_hologic_panther_failed_but_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_hologic_panther_repeat_dbs= models.IntegerField()
    tests_done_hologic_panther_failed_after_repeat_testing_dbs = models.IntegerField()

    total_tests_done = models.IntegerField()
    total_repeats = models.IntegerField()
    total_patients_run = models.IntegerField()
    targets_weekly = models.IntegerField()
    percentage_targets_achievements = models.DecimalField(decimal_places=5,  max_digits=5)


    percentage_error_rate_roche_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_roche_dbs = models.DecimalField(decimal_places=5,  max_digits=5)

    percentage_error_rate_bmx_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_bmx_dbs = models.DecimalField(decimal_places=5,  max_digits=5) 

    percentage_error_rate_abbott_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_abbott_dbs = models.DecimalField(decimal_places=5,  max_digits=5) 

    percentage_error_rate_hologic_panther_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_hologic_panther_dbs = models.DecimalField(decimal_places=5,  max_digits=5) 


    total_ncs_from_audit=models.TextField(max_length=5000,null=True)
    ncs_not_yet_closed=models.TextField(max_length=5000,null=True)



class Electric_outage_brti_vl_weekly(models.Model):
    day_of_week = models.CharField(max_length=20,null=False)


    number_of_hours_with_no_electricity_per_day	= models.IntegerField()
    number_of_hours_generator_was_on_per_day	= models.IntegerField()
    litres_of_fuel_added_to_generator_per_day	= models.IntegerField()
    number_of_hours_machines_was_not_being_used_due_to_power_cut_per_day	= models.IntegerField()
    total_tests_done_per_day_using_generator	= models.IntegerField()











class Reasons_for_failure_brti_vl_weekly(models.Model):
    day_of_week = models.CharField(max_length=20,null=False)
#roche
    roche_plasma_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_other = models.IntegerField()
    roche_dqa_check_plasma = models.IntegerField()

    roche_dbs_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_other = models.IntegerField()
    roche_dqa_check_dbs = models.IntegerField()

#bmx

    bmx_plasma_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_other = models.IntegerField()
    bmx_dqa_check_plasma = models.IntegerField()

    bmx_dbs_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_other = models.IntegerField()
    bmx_dqa_check_dbs = models.IntegerField()



#abbott

    abbott_plasma_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_other = models.IntegerField()
    abbott_dqa_check_plasma = models.IntegerField()

    abbott_dbs_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_other = models.IntegerField()
    abbott_dqa_check_dbs = models.IntegerField()




#Hologic Panther

    hologic_panther_plasma_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_other = models.IntegerField()
    hologic_panther_dqa_check_plasma = models.IntegerField()

    hologic_panther_dbs_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_other = models.IntegerField()
    hologic_panther_dqa_check_dbs = models.IntegerField()



#General Info masvingo brti_covid_19_weekly_statistics_tool


class General_info_covid_19(models.Model):
    general_comments_regarding_testing_and_challenges_faced_by_the_laboratory = models.CharField( max_length=5000, null=True)
    number_of_staff_who_tested_positive_to_covid_19_at_vl_lab	= models.IntegerField()
    number_of_staff_who_have_been_vaccinated	= models.IntegerField()
    Comments =models.CharField( max_length=5000, null=True)
    Request_to_brti_from_the_laboratory	= models.CharField( max_length=5000, null=True)








#another 


class Specimens_received_covid_19(models.Model):
    samples_carried_over_previous_weeks	= models.IntegerField()

    samples_received_current_week_nasopharyngeal_swab = models.IntegerField()
    samples_received_current_week_nasal_swab = models.IntegerField()
    samples_received_current_week_oropharyngeal_swab = models.IntegerField()
    samples_received_current_week_midturbinate_swab = models.IntegerField()
    samples_received_current_week_sputum = models.IntegerField()
    samples_received_current_week_whole_blood_or_plasma_or_serum = models.IntegerField()
    samples_received_current_week_other = models.IntegerField()


    samples_rejected_current_week =	models.IntegerField()
    total_samples_received_current_week	=	models.IntegerField()

    number_of_samples_entered_into_lims =	models.IntegerField()
    total_samples_current_plus_carryover	 =	models.IntegerField()
    samples_referred	=	models.IntegerField()
    rejection_rate_current_week = models.DecimalField(decimal_places=5,  max_digits=5)
    number_of_results_printed_lims =	models.IntegerField()
    total_results_dispatched_by_lab	=	models.IntegerField()
    comment= models.CharField( max_length=5000, null=True)

# class Machine_downtime_Reagent_stock_out_tool_covid_19(models.Model):
#     machine_breakdown_number_abbott	=	models.IntegerField()
#     machine_breakdown_number_bmx	=	models.IntegerField()
#     machine_breakdown_number_genexpert	=	models.IntegerField()
#     machine_breakdown_number_quant_studio_3	=	models.IntegerField()
#     machine_breakdown_number_hologic_panther	=	models.IntegerField()
#     machine_breakdown_number_comments	= models.CharField( max_length=5000, null=True)

#     machine_downtime_days_abbott = 	models.IntegerField()
#     machine_downtime_days_bmx = 	models.IntegerField()
#     machine_downtime_days_genexpert = 	models.IntegerField()
#     machine_downtime_days_quant_studio_3 = 	models.IntegerField()
#     machine_downtime_days_hologic_panther = 	models.IntegerField()
#     machine_downtime_days_comments = 	models.CharField( max_length=5000, null=True)

#     #reagent_stockout	

#     reagent_stockout_abbott = 	models.IntegerField()
#     reagent_stockout_bmx = 	models.IntegerField()
#     reagent_stockout_genexpert = 	models.IntegerField()
#     reagent_stockout_quant_studio_3 = 	models.IntegerField()
#     reagent_stockout_hologic_panther = 	models.IntegerField()
#     reagent_stockout_comments = 	models.CharField( max_length=5000, null=True)




class Specimens_run_covid_19(models.Model):
    #Roche
    tests_done_abbott_run = models.IntegerField()
    tests_done_abbott_failed_but_eligibale_for_repeat= models.IntegerField()
    tests_done_abbott_failed_but_not_eligibale_for_repeat= models.IntegerField()
    tests_done_abbott_repeat= models.IntegerField()


    tests_done_bmx_run = models.IntegerField()
    tests_done_bmx_failed_but_eligibale_for_repeat= models.IntegerField()
    tests_done_bmx_failed_but_not_eligibale_for_repeat= models.IntegerField()
    tests_done_bmx_repeat= models.IntegerField()

    # genexpert
    tests_done_genexpert_run = models.IntegerField()
    tests_done_genexpert_failed_but_eligibale_for_repeat= models.IntegerField()
    tests_done_genexpert_failed_but_not_eligibale_for_repeat= models.IntegerField()
    tests_done_genexpert_repeat= models.IntegerField()
# quant_studio_3
    tests_done_quant_studio_3_run = models.IntegerField()
    tests_done_quant_studio_3_failed_but_eligibale_for_repeat= models.IntegerField()
    tests_done_quant_studio_3_failed_but_not_eligibale_for_repeat= models.IntegerField()
    tests_done_quant_studio_3_repeat= models.IntegerField()
# hologic_panther	
    tests_done_hologic_panther_run = models.IntegerField()
    tests_done_hologic_panther_failed_but_eligibale_for_repeat= models.IntegerField()
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat= models.IntegerField()
    tests_done_hologic_panther_repeat= models.IntegerField()
# RDT
    tests_done_rdt_ab_run = models.IntegerField()
    tests_done_rdt_ab_failed_but_eligibale_for_repeat= models.IntegerField()
    tests_done_rdt_ab_failed_but_not_eligibale_for_repeat= models.IntegerField()
    tests_done_rdt_ab_repeat= models.IntegerField()

    tests_done_rdt_ag_run = models.IntegerField()
    tests_done_rdt_ag_failed_but_eligibale_for_repeat= models.IntegerField()
    tests_done_rdt_ag_failed_but_not_eligibale_for_repeat= models.IntegerField()
    tests_done_rdt_ag_repeat= models.IntegerField()


    total_tests_done = models.IntegerField()
    total_repeats = models.IntegerField()
    total_patients_run = models.IntegerField()


    error_rates_abbott = models.IntegerField()
    error_rates_bmx = models.IntegerField()
    error_rates_genexpert = models.IntegerField()
    error_rates_quant_studio_3 = models.IntegerField()
    error_rates_hologic_panther = models.IntegerField()
    error_rates_rdt_ab = models.IntegerField()
    error_rates_rdt_ag = models.IntegerField()





#masving_brti_weekly_statistics_tool_31-6_june_2021

class Specimens_run_brti_weekly(models.Model):
    day_of_week = models.CharField(max_length=20,null=False)



#Roche
    tests_done_roche_number_of_samples_received_this_week_plasma = models.IntegerField()
    tests_done_roche_number_of_samples_carried_over_previous_weeks_plasma = models.IntegerField()
    tests_done_roche_failed_but_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_roche_failed_but_not_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_roche_repeat_plasma= models.IntegerField()
    tests_done_roche_failed_after_repeat_testing_plasma = models.IntegerField()


    tests_done_roche_number_of_samples_received_this_week_dbs = models.IntegerField()
    tests_done_roche_number_of_samples_carried_over_previous_weeks_dbs = models.IntegerField()
    tests_done_roche_failed_but_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_roche_failed_but_not_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_roche_repeat_dbs= models.IntegerField()
    tests_done_roche_failed_after_repeat_testing_dbs = models.IntegerField()
#BMX
    tests_done_bmx_number_of_samples_received_this_week_plasma = models.IntegerField()
    tests_done_bmx_number_of_samples_carried_over_previous_weeks_plasma = models.IntegerField()
    tests_done_bmx_failed_but_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_bmx_failed_but_not_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_bmx_repeat_plasma= models.IntegerField()
    tests_done_bmx_failed_after_repeat_testing_plasma = models.IntegerField()


    tests_done_bmx_number_of_samples_received_this_week_dbs = models.IntegerField()
    tests_done_bmx_number_of_samples_carried_over_previous_weeks_dbs = models.IntegerField()
    tests_done_bmx_failed_but_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_bmx_failed_but_not_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_bmx_repeat_dbs= models.IntegerField()
    tests_done_bmx_failed_after_repeat_testing_dbs = models.IntegerField()

#Abbott
    tests_done_abbott_number_of_samples_received_this_week_plasma = models.IntegerField()
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_plasma = models.IntegerField()
    tests_done_abbott_failed_but_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_abbott_failed_but_not_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_abbott_repeat_plasma= models.IntegerField()
    tests_done_abbott_failed_after_repeat_testing_plasma = models.IntegerField()


    tests_done_abbott_number_of_samples_received_this_week_dbs = models.IntegerField()
    tests_done_abbott_number_of_samples_carried_over_previous_weeks_dbs = models.IntegerField()
    tests_done_abbott_failed_but_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_abbott_failed_but_not_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_abbott_repeat_dbs= models.IntegerField()
    tests_done_abbott_failed_after_repeat_testing_dbs = models.IntegerField()

#Hologic Panther
    tests_done_hologic_panther_number_of_samples_received_this_week_plasma = models.IntegerField()
    tests_done_hologic_panther_number_of_samples_carried_over_previous_weeks_plasma = models.IntegerField()
    tests_done_hologic_panther_failed_but_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat_plasma= models.IntegerField()
    tests_done_hologic_panther_repeat_plasma= models.IntegerField()
    tests_done_hologic_panther_failed_after_repeat_testing_plasma = models.IntegerField()


    tests_done_hologic_panther_number_of_samples_received_this_week_dbs = models.IntegerField()
    tests_done_hologic_panther_number_of_samples_carried_over_previous_weeks_dbs = models.IntegerField()
    tests_done_hologic_panther_failed_but_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_hologic_panther_failed_but_not_eligibale_for_repeat_dbs= models.IntegerField()
    tests_done_hologic_panther_repeat_dbs= models.IntegerField()
    tests_done_hologic_panther_failed_after_repeat_testing_dbs = models.IntegerField()

    total_tests_done = models.IntegerField()
    total_repeats = models.IntegerField()
    total_patients_run = models.IntegerField()
    targets_weekly = models.IntegerField()
    percentage_targets_achievements = models.DecimalField(decimal_places=5,  max_digits=5)


    percentage_error_rate_roche_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_roche_dbs = models.DecimalField(decimal_places=5,  max_digits=5)

    percentage_error_rate_bmx_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_bmx_dbs = models.DecimalField(decimal_places=5,  max_digits=5) 

    percentage_error_rate_abbott_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_abbott_dbs = models.DecimalField(decimal_places=5,  max_digits=5) 

    percentage_error_rate_hologic_panther_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_error_rate_hologic_panther_dbs = models.DecimalField(decimal_places=5,  max_digits=5) 


    total_ncs_from_audit=models.TextField(max_length=5000,null=True)
    ncs_not_yet_closed=models.TextField(max_length=5000,null=True)



class Specimens_received_brti_weekly(models.Model):
    date_of_week= models.IntegerField()

    samples_carried_over_previous_weeks_never_tested_plasma = models.IntegerField()
    samples_carried_over_previous_weeks_never_tested_dbs = models.IntegerField()

    samples_carried_over_previous_failed_samples_plasma = models.IntegerField()
    samples_carried_over_previous_failed_samples_dbs = models.IntegerField()



    samples_received_current_week_plasma = models.IntegerField()
    samples_received_current_week_dbs = models.IntegerField()

    samples_rejected_current_week_plasma = models.IntegerField()
    samples_rejected_current_week_dbs = models.IntegerField()
    
    total_samples_received_current_week_plasma = models.IntegerField()
    total_samples_received_current_week_dbs = models.IntegerField()

    number_of_samples_entered_into_lims_on_day_of_arrival_plasma = models.IntegerField()
    number_of_samples_entered_into_lims_on_day_of_arrival_dbs = models.IntegerField()

    number_of_samples_entered_into_lims_after_day_of_arrival_plasma = models.IntegerField()
    number_of_samples_entered_into_lims_after_day_of_arrival_dbs = models.IntegerField()

    number_of_hours_lims_was_functional	 = models.IntegerField()

    total_samples_current_plus_carryover_plasma= models.IntegerField()
    total_samples_current_plus_carryover_dbs= models.IntegerField()

    samples_reffered_plasma = models.IntegerField()
    samples_reffered_dbs = models.IntegerField()

    lab_samples_reffered_to = models.IntegerField()

    percentage_rejection_rate_plasma = models.DecimalField(decimal_places=5,  max_digits=5)
    percentage_rejection_rate_dbs = models.DecimalField(decimal_places=5,  max_digits=5)


    number_of_results_printed_from_lims_plasma = models.IntegerField()
    number_of_results_printed_from_lims_dbs = models.IntegerField()

    total_results_dispatched_by_lab_plasma	= models.IntegerField()
    total_results_dispatched_by_lab_dbs	= models.IntegerField()

    total_results_dispatched_by_lab_via_sms_plasma	= models.IntegerField()
    total_results_dispatched_by_lab_via_sms_dbs	= models.IntegerField()



    reasons_for_rejections_sample_quality_compromised_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_dbs = models.IntegerField()


    reasons_for_rejections_sample_quality_compromised_sample_quality_insufficient_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_sample_quality_insufficient_dbs = models.IntegerField()


    reasons_for_rejections_sample_quality_compromised_sample_information_mismatch_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_sample_information_mismatch_dbs = models.IntegerField()


    reasons_for_rejections_sample_quality_compromised_sample_or_request_form_missing_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_sample_or_request_form_missing_dbs = models.IntegerField()


    reasons_for_rejections_sample_quality_compromised_qda_check_plasma = models.IntegerField()
    reasons_for_rejections_sample_quality_compromised_qda_check_dbs = models.IntegerField()


    reasons_for_sample_refferal_reagent_or_kit_stockout_plasma= models.IntegerField()
    reasons_for_sample_refferal_reagent_or_kit_stockout_dbs= models.IntegerField()


    reasons_for_sample_refferal_instrument_mechanical_failure_plasma= models.IntegerField()
    reasons_for_sample_refferal_instrument_mechanical_failure_dbs= models.IntegerField()

    reasons_for_sample_refferal_insufficient_instrument_capacity_plasma= models.IntegerField()
    reasons_for_sample_refferal_insufficient_instrument_capacity_dbs= models.IntegerField()

    reasons_for_sample_refferal_insufficient_hr_capacity_plasma= models.IntegerField()
    reasons_for_sample_refferal_insufficient_hr_capacity_dbs= models.IntegerField()

    reasons_for_sample_refferal_dqa_check_plasma= models.IntegerField()
    reasons_for_sample_refferal_dqa_check_dbs= models.IntegerField()

   
   
   
   

   
   
    comments=models.TextField("Please input any comments regarding sample carryover, samples received, samples rejected, rejection rate, TAT, machine breakdowns & down time, reagent stock out if applicable", max_length=5000, null=True)


class Reasons_for_failure_brti_weekly(models.Model):
    day_of_week = models.CharField(max_length=20,null=False)
#roche
    roche_plasma_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    roche_plasma_number_of_failed_tests_due_to_other = models.IntegerField()
    roche_dqa_check_plasma = models.IntegerField()

    roche_dbs_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    roche_dbs_number_of_failed_tests_due_to_other = models.IntegerField()
    roche_dqa_check_dbs = models.IntegerField()

#bmx

    bmx_plasma_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    bmx_plasma_number_of_failed_tests_due_to_other = models.IntegerField()
    bmx_dqa_check_plasma = models.IntegerField()

    bmx_dbs_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    bmx_dbs_number_of_failed_tests_due_to_other = models.IntegerField()
    bmx_dqa_check_dbs = models.IntegerField()



#abbott

    abbott_plasma_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    abbott_plasma_number_of_failed_tests_due_to_other = models.IntegerField()
    abbott_dqa_check_plasma = models.IntegerField()

    abbott_dbs_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    abbott_dbs_number_of_failed_tests_due_to_other = models.IntegerField()
    abbott_dqa_check_dbs = models.IntegerField()




#Hologic Panther

    hologic_panther_plasma_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    hologic_panther_plasma_number_of_failed_tests_due_to_other = models.IntegerField()
    hologic_panther_dqa_check_plasma = models.IntegerField()

    hologic_panther_dbs_number_of_failed_tests_due_to_sample_quality_issues = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_reagent_quality_issues = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_due_to_qc_failure = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_power_failure = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_mechanical_failure = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_processing_error = models.IntegerField()
    hologic_panther_dbs_number_of_failed_tests_due_to_other = models.IntegerField()
    hologic_panther_dqa_check_dbs = models.IntegerField()




class Electric_outage_brti_vl_weekly(models.Model):
    day_of_week = models.CharField(max_length=20,null=False)


    number_of_hours_with_no_electricity_per_day	= models.IntegerField()
    number_of_hours_generator_was_on_per_day	= models.IntegerField()
    litres_of_fuel_added_to_generator_per_day	= models.IntegerField()
    number_of_hours_machines_was_not_being_used_due_to_power_cut_per_day	= models.IntegerField()
    total_tests_done_per_day_using_generator	= models.IntegerField()

















# masvingo_brti_covid_19_weekly_statistics_tool_31-6_June_2021


















































