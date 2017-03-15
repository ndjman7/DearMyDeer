import json
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view

from information.utils import future_centennial_hall_food
from information.utils import return_today
from .models import DeerSchoolFood


@api_view(['GET'])
def test(request):
    data = {
        'type': 'buttons',
        'buttons': ["미래백년관", "밀레니엄관", "학식정보"]
    }
    return Response(data)


@api_view(['POST'])
def test2(request):

    json_data = (request.body).decode('utf-8')
    received_json_data = json.loads(json_data)
    content = received_json_data['content']
    data = dict()
    if content == "미래백년관":
        try:
            deer_food = DeerSchoolFood.objects.get(date=timezone.localtime(timezone.now()).date())
        except DeerSchoolFood.DoesNotExist:
            deer_food = DeerSchoolFood.objects.create(
                future_centennial_hall_food=future_centennial_hall_food(return_today())
            )
        data = {
            "message": {
                "text": deer_food.future_centennial_hall_food
            }
        }
    elif content == "밀레니엄관":
        data = {
            "message": {
                "text": "밀레니엄관"
            }
        }
    elif content == "학식정보":
        data = {
            "message": {
                "text":
                    "중식 : 11시 00분 ~ 14시 00분\
                     간식 : 16시 00분 ~ 17시 00분\
                     석식 : 17시 00분 ~ 18시 30분"
            }
        }

    data['keyboard'] = {
        "type": "buttons",
        "buttons": ["미래백년관", "밀레니엄관", "학식정보"]
    }

    return Response(data)
