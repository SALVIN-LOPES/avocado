from django.http import HttpResponse

def home_api(request):
    return httpResponse("this is home API")