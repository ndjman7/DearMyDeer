import json
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view

from information.utils import future_centennial_hall_food, millennium_hall_food
from information.utils import return_today
from .models import DeerSchoolFood


@api_view(['GET'])
def keyboard(request):
    data = {
        'type': 'buttons',
        'buttons': [
            "미래백년관",
            "밀레니엄관",
            "페이스북",
        ]
    }
    return Response(data)


@api_view(['POST'])
def message(request):

    json_data = (request.body).decode('utf-8')
    received_json_data = json.loads(json_data)
    content = received_json_data['content']
    data = dict()
    if content == "미래백년관":
        deer_food = DeerSchoolFood.objects.get_or_create(date=timezone.localtime(timezone.now()).date())[0]
        if deer_food.future_centennial_hall_food is None:
            deer_food.future_centennial_hall_food = future_centennial_hall_food(return_today())
        data = {
            "message": {
                "text": deer_food.future_centennial_hall_food
            }
        }
    elif content == "밀레니엄관":
        deer_food = DeerSchoolFood.objects.get_or_create(date=timezone.localtime(timezone.now()).date())[0]
        if deer_food.millennium_hall_food is None:
            deer_food.millennium_hall_food = millennium_hall_food(return_today())
        data = {
            "message": {
                "text": deer_food.millennium_hall_food
            }
        }

    elif content == "페이스북":
        data = {
            "message": {
                "text":
                    "디어마이디어 공식 페이지",
                "photo": {
                    "url": "https://unripers.com/media/background.jpeg",
                    "width": 640,
                    "height": 480
                },
                "message_button": {
                    "label": "디어마이디어 공식 페이지",
                    "url": "https://www.facebook.com/smudearmydeer/"
                }
            }
        }

    data['keyboard'] = {
        "type": "buttons",
        "buttons": [
            "미래백년관",
            "밀레니엄관",
            "페이스북",
        ]
    }

    return Response(data)
