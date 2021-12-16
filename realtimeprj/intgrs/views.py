from django.shortcuts import render

# Create your views here.
def index(request):
    table = [{'a' : 1, 'b' : 2, 'c' : 3},
            {'a' : 2, 'b' : 7, 'c' : 4},
            {'a' : 5, 'b' : 8, 'c' : 8},
            {'a' : 4, 'b' : 7, 'c' : 9}]
    return render(request, 'index.html', context={'text' : 'Hello World', 'table' : table})