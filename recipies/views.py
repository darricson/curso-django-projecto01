from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'see': 'teste deu certo'
        }
    return render(request, 'recipies/pages/home.html', context)
