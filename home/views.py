from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render())

def detail(request):
    template = loader.get_template('detail/index.html')
    return HttpResponse(template.render())
