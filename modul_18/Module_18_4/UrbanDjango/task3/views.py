from django.shortcuts import render


def home_page(request):
    return render(request, 'third_task/home_page.html')


def shop(request):
    page_name = "Игры"
    game_1 = "Atomic Heart"
    game_2 = "Cyberpunk 2077"
    game_3 = "PayDay 2"
    buy = "Купить"
    context = {
        'title': page_name,
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
        'buy': buy,
    }
    return render(request, 'third_task/shop.html', context)


def shopping_cart(request):
    page_name = "Корзина"
    text_1 = "Ваша корзина пуста!"
    context = {
        'title': page_name,
        'text_1': text_1,
    }
    return render(request, 'third_task/shopping_cart.html', context)

