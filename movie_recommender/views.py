import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .recommender import get_recommendation


@api_view(["GET"])
def home(r):
    return HttpResponse("<h1>Home Page 👽<h1>")


@api_view(["POST"])
def getRecommendation(request):
    try:
        movie = json.loads(request.body)
        recommendation = get_recommendation(movie["movie"])
    except:
        return JsonResponse({"message": "Enter Valid Data"}, status=401)
    if recommendation != "":
        return JsonResponse({"recommendations": recommendation}, status=201)
    else:
        return JsonResponse({"message": "Movie not in the DB"}, status=401)
