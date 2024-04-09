from django.shortcuts import render

def home(request):
    # Render the base.html template
    return render(request, 'base.html')
