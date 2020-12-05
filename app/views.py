from django.shortcuts import render, redirect
from .models import Game

# Create your views here.
def home(request):
    return render(request, 'home.html')

def save_process(request):
    name = request.POST['game']
    price = request.POST['price']

    game = Game()

    game.name = name
    game.price = price

    game.save()

    return redirect('/')

def gamelist(request):
    context = {
        'games': Game.objects.all()
    }
    return render(request, 'list.html', context)