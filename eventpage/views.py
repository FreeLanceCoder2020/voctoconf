from django.shortcuts import render
from authstuff.names import name_required
from django.http import HttpResponse
from .models import Room as EventRoom

def event_view(request):
    context = {}
    context['event_rooms'] = EventRoom.objects.filter(hide=False).order_by('order')
    return render(request, "event/event.html", context)
