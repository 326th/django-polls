from django.shortcuts import redirect

def redirect_polls(request):
    response = redirect('/polls/')
    return response


