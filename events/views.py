from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import Myform
from django.db.models import Count

# Create your views here.
def Home(request):
    result = (Event.objects
    .values('event_city')
    .annotate(dcount=Count('event_city'))
    .order_by()
    )
    p = []
    for x in result:
        p.append(Event.objects.filter(event_city = x['event_city']))
    params = {'evbyplace': p}
    return render(request, 'events/Home.html', params)

def eventform(request):
    if request.method == "POST":
        form = Myform(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            
        else:
            print("form invalid")
    else:
        form = Myform()
    return render(request, 'events/eventform.html', {'form': form})

def test(request):
    result = (Event.objects
    .values('event_city')
    .annotate(dcount=Count('event_city'))
    .order_by()
    )
    p = []
    for x in result:
        p.append(Event.objects.filter(event_city = x['event_city']))
    params = {'r': p}
    return render(request, 'events/test.html', params)

def displaypage(request):
    Eid = request.GET.get('eid', 'NA')
    print(Eid)
    event = Event.objects.get(event_id = Eid)
    param = {'Ev': event}
    return render(request, 'events/Evdisplay.html', param)