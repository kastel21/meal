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