from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the pages index.")




@method_decorator([login_required], name='dispatch')
class RecordAddView(CreateView):

    model = Record
    form_class = RecordAddForm
    template_name = 'templates/add_record.html'


    def form_valid(self, form):
        print("===============try try=====================================",self.request.user)

        #form.owner = str(self.request.user)
        obj = form.save(commit=False)
        obj.owner = str(self.request.user)
        obj.save()
        #form.save()
        return redirect('127.0.0.1:8000')

