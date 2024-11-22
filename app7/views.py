from django.http import HttpResponse
from django.template import loader
def home(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def register(request):
    template=loader.get_template('register.html')
    return HttpResponse(template.render())