from django.shortcuts import render
from .models import sublin ,monday ,thursday ,wednesday ,tuesday ,friday ,saturday

from django.http import HttpResponse
from django.utils import timezone
import datetime
import calendar 
# Create your views here.


def index(request):
    sub = sublin.objects.order_by('id')
    context={'ob':sub}
    return render(request,'tt/index.html',context)



def test(request):
    day = {'0': 'mon', '1':'tue','2':'wed','3':'thu','4':'fri','5':'saturday','6':'sunday'}
    day = day.get(str(datetime.datetime.today().weekday()))
    print(day)
    mon = monday.objects.order_by('period')
    tue = tuesday.objects.order_by('period')
    wed = wednesday.objects.order_by('period')
    the = thursday.objects.order_by('period')
    fri = friday.objects.order_by('period')
    context = {"day":day,"mon":mon,"tue":tue, "wed":wed ,"the":the ,"fri":fri}
    return render(request,'tt/time.html',context)