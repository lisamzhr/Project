from django.shortcuts import render, redirect
from main.forms import MoodEntryForm
from main.models import MoodEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    mood_entries = MoodEntry.objects.all()
    
    context = {
        'npm' : '163231045',
        'name': 'sskytails',
        'mood_entries' : mood_entries
    }

    return render(request, "main.html", context)

def create_mood_entry(request) :
    form = MoodEntryForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST" :
        form.save()
        return redirect('main:show_main')
    context = {'form' : form}
    return render(request, "create_mood_entry.html", context)
    
def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
