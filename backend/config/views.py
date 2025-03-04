from django.http import JsonResponse

def test_env_status(request):
    return JsonResponse({"message": "Test environment is up and running!"})