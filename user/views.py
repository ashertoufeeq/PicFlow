from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import User
from django.shortcuts import redirect


def sign_in(request):
    message = ''

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

            if password == user.password:
                request.session['user'] = user.id
                return redirect('index')

        except ObjectDoesNotExist:
            message = 'User Not Registered'

    return render(request, 'user/sign-in.html', {
        'message': message
    })


def sign_out(request):
    del request.session['user']
    return redirect('index')
