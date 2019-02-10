from django.shortcuts import render
from user.models import User


# Create your views here.
def index(request):
    user = None
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])

    return render(request, 'pics/index.html', {
        'user': user
    })
