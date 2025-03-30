from django.shortcuts import render
from django.http import JsonResponse
from .models import RocketLog

# Create your views here.
def rocket_log_list(request):
  logs = RocketLog.objects.all().values()
  return JsonResponse(list(logs), safe=False)
