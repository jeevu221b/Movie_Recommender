import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .recommender import get_recommendation
import logging
from honeybadger.contrib.logger import HoneybadgerHandler


# Logger
hb_handler = HoneybadgerHandler(
    api_key='hbp_2AKL7yaM9fGujohj7yWpw0lNRP1vvb3ST8gR')
logger = logging.getLogger('honeybadger')
logger.addHandler(hb_handler)
logger.setLevel(logging.INFO)


@api_view(["GET"])
def home(r):
    return HttpResponse("<h1>Home Page 👽<h1>", status =200)


@api_view(["POST"])
def getRecommendation(request):
    try:
        movie = json.loads(request.body)
        logger.info(f"Method: {request.method}, Body: {movie}")
        recommendation = get_recommendation(movie["movie"])
    except Exception as e:
        logger.error(e)
        return JsonResponse({"error": "Enter Valid Data"}, status=400)
    if recommendation != "":
        return JsonResponse(recommendation, status=200, safe=False)
    else:
        message = "Movie not in the DB"
        logger.error(message)
        return JsonResponse({"error": message}, status=400)
