from django.db import models
from django.urls import reverse

# Create your models here.




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



class Specimens_recieved(models.Model):
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

    percentage_rejection_rate_plasma = models.IntegerField()
    percentage_rejection_rate_dbs = models.IntegerField()


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