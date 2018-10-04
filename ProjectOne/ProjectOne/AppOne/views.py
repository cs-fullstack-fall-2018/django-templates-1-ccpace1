from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My First App</em>")