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

def result(request):
    tileName = request.GET.get('choice')

    context = {
        'tileName' : tileName
        # 'data : data
    }

    return render(request, 'recommender/result.html',
        context
    )