from django.shortcuts import render
from django.http import HttpResponse

# Processing CRUD Requests
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'recommender/index.html', 
        # {
        #     'data': data
        # }
    
    )

# Front end rendering
def detail(request):
    return render(request, 'recommender/index.html', 
        # {
        #     'data': data
        # }
    
    )

def result(request):
    return render(request, 'recommender/result.html',
        # data
    )