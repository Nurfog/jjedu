from django.shortcuts import render

# Create your views here.
class Home:
    def index(request):
        return render(request, 'index.html')