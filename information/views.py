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
            "공지사항"
            "미래백년관",
            "밀레니엄관",
            "페이스북",
        ]
    }
    return Response(data)


@api_view(['POST'])
def message(request):

    content = request.data['content']
    data = dict()

    if content == "공지사항":
        data = {
            "message": {
                "text": "상명대학교 홈페이지 공지사항입니다."
            }
        }

    elif content == "미래백년관":
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
                "photo": {
                    "url": "http://unripers.com/media/background.jpeg",
                    "width": 640,
                    "height": 480
                },
                "message_button": {
                    "label": "디마디 공식 페이지",
                    "url": "https://www.facebook.com/smudearmydeer/"
                }
            }
        }

    data['keyboard'] = {
        "type": "buttons",
        "buttons": [
            "공지사항",
            "미래백년관",
            "밀레니엄관",
            "페이스북",
        ]
    }

    return Response(data)
