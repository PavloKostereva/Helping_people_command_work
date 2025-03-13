from django.shortcuts import render



def home(request):
    return render(request, 'myapp/index.html')


def about(request):
    return render(request,'about.html')




def log_in(request):
    return render(request, 'login.html')



def sign_up(request):
    return render(request, 'signup.html')