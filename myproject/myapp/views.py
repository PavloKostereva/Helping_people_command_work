from django.shortcuts import render



def home(request):
    return render(request, 'myapp/index.html')


def about(request):
    return render(request, 'myapp/about.html')



def log_in(request):
    return render(request, 'myapp/log_in.html')


def sign_up(request):
    return render(request, 'myapp/sign_up.html')

def instruction(request):
    return render(request, 'myapp/instruction.html')