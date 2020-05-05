from django.shortcuts import render

# Create your views here.
def join(request):
    context = {
        'title': 'Quizwin'
    }
    return render(request, 'quiz/index.html', context)

def create(request):
    context = {
        'title': 'Create'
    }
    return render(request, 'quiz/create.html', context)