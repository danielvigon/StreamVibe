from django.shortcuts import render

# Create your views here (MTV - model-template-view).

def index(request):
    return render(
        request,
        'sistema/index.html',
    )


# request
# response