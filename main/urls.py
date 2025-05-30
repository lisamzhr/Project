from django.urls import path
from main.views import show_main, create_mood_entry
from main.views import show_main, create_mood_entry, show_xml

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-mood-entry', create_mood_entry, name='create_mood_entry'),
    path('xml/', show_xml, name='show_xml')
]