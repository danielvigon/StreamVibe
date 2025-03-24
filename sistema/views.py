from django.shortcuts import render

# Create your views here (MVT - model-view-template).
# Controllers here.
# The index function calls a page after a user request.

def index(request):
    return render(
        request,
        'sistema/index.html',
    )


# request
# response