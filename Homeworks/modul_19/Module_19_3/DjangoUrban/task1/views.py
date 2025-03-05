from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game


def home_page(request):
    return render(request, 'home_page.html')


def shop(request):
    page_name = "Игры"
    game = Game.objects.all()
    context = {
        'title': page_name,
        'game': game,
    }
    return render(request, 'shop.html', context)


def shopping_cart(request):
    page_name = "Корзина"
    text_1 = "Ваша корзина пуста!"
    context = {
        'title': page_name,
        'text_1': text_1,
    }
    return render(request, 'shopping_cart.html', context)


def registration(request):
    users = []
    users_in_base = Buyer.objects.all()
    for i in users_in_base:
        users.append(i.name)

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info = {}
            context = {'info': info, 'form': form}

            if password == repeat_password and int(age) > 18 and username not in users:
                Buyer.objects.create(name=username, balance='0', age=int(age))
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context)
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
