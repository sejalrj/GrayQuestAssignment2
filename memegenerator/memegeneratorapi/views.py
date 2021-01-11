from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse
import requests
import random
# Create your views here.
@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
    return JsonResponse({"details": "CSRF cookie set"})

def login_page(request):
    return render(request, "login.html")


#@require_POST
def postlogin(request):
    print("Inside postlogin method")
    print("===========", request)
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username is None or password is None:
        return JsonResponse({
            "errors": {
                "__all__": "Please enter both username and password"
            }
        }, status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'postlogin.html')
        
    return JsonResponse(
        {"detail": "Invalid credentials"},
        status=400,
    )
    #return render(request, 'login.html')

def memepage(request):
    response = requests.get('https://api.imgflip.com/get_memes')
    print(response.json())
    memes_dict = response.json()['data']['memes']
    memes = []
    for i in range(4):
        res = random.choice(memes_dict)
        memes.append(str(res))
    return render(request, 'memes.html', {'memes': memes})