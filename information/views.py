from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def test(request):
    data = {
        'type': 'buttons',
        'buttons': ["선택 1", "선택 2", "선택 3"]
    }
    return Response(data)
