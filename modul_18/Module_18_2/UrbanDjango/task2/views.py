from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'second_task/func_templates.html')


def page(request):
    return render(request, 'page.html')


class Index2(TemplateView):
    template_name = 'second_task/class_templates.html'