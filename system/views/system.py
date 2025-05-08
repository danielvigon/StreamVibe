from django.shortcuts import render

# Views here (MVT - model-view-template).
# The functions return pages after a user request.

def index(request):
    return render(
        request,
        'system/index.html',
    )

def presentation(request):
    return render(
        request,
        'system/presentation.html',
    )