from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404, redirect, render



def index(request):
    return HttpResponse("Hello, world. You're at the pages index.")


def home(request):
    context={}

    return render(request, 'base.html', context)

def profile(request):
    context={}
    return render(request, 'brti_covid_19 _weekly_statistics _tool_may_week_4/Specimens_Run.html', context)

# def prof(request):
#     context={}
#     return render(request, 'brti_vl_eid_weekly_statistics_tool_may_week_4/specimens_run.html', context)


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

