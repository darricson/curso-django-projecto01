from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'see': 'teste deu certo'
        }
    return render(request, 'recipes/pages/home.html', context)


def recipe(request, id):
    context = {
        'see': 'teste deu certo'
        }
    return render(request, 'recipes/pages/recipe-view.html', context)
