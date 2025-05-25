from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406415399',
        'name': 'Elsa',
        'class': 'Tangled'
    }

    return render(request, "main.html", context)
