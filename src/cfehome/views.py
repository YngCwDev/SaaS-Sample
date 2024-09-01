from django.shortcuts import render
from  django.http import HttpResponse 

from visits.models import PageVisits

def home(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    page_qs =PageVisits.objects.filter(path=request.path)
    vars = {
        'name': 'Alcides',
        'page_visits': page_qs.count(),
        'total_visits_count': qs.count(),
    }
    PageVisits.objects.create()
    return render(request, 'home.html', vars)

