from django.shortcuts import render


def home_page1(request):
    return render(request, 'fourth_task/home_page.html')


def shop1(request):
    page_name = "Игры"
    game = ["Atomic Heart",
            "Cyberpunk 2077",
            "PayDay 2"]
    context = {
        'title': page_name,
        'game': game,
    }
    return render(request, 'fourth_task/shop.html', context)


def shopping_cart1(request):
    page_name = "Корзина"
    text_1 = "Ваша корзина пуста!"
    context = {
        'title': page_name,
        'text_1': text_1,
    }
    return render(request, 'fourth_task/shopping_cart.html', context)
