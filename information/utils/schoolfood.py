import requests

from django.utils import timezone

from bs4 import BeautifulSoup

__all__ = [
    'future_centennial_hall_food',
    'millennium_hall_food',
]

DAY_LIST = {
    0: '월',
    1: '화',
    2: '수',
    3: '목',
    4: '금',
    5: '토',
    6: '일'
}


def future_centennial_hall_food(today):
    if today == 5 or today == 6:
        return '금일은 학식정보를 제공하지 않습니다.'
    else:
        r = requests.get('https://www.smu.ac.kr/mbs/smu/jsp/restaurant/restaurant.jsp?configIdx=27144&id=smu_040501000000')
        bs = BeautifulSoup(r.text, 'html.parser')
        food_list = bs.find_all('tr')
        string = ''
        string += timezone.localtime(timezone.now()).strftime('%Y년 %m월 %d일 ')
        string += '{}요일\n'.format(DAY_LIST[today])
        day = today * 4
        string += '중식 (11:00~14:00)\n'
        string += '  뷔페식  (4500원)\n'
        string += '----------------\n'
        for food in food_list[day].find_all('p'):
            string += food.text
            string += '\n'
        string += '\n'
        string += '오늘의 메뉴 (4000원)\n'
        string += '----------------\n'
        for food in food_list[day+1].find_all('p'):
            string += food.text
            string += '\n'
        string += '\n'
        string += '간식 (16:00~17:00)\n'
        string += '----------------\n'
        string += food_list[day+2].find('div').text
        string += '\n'
        string += '석식 (17:00~18:30)\n'
        string += '----------------\n'
        for food in food_list[day+3].find_all('p'):
            string += food.text
            string += '\n'
        string += '\n'
        return string


def millennium_hall_food(today):
    if today == 5 or today == 6:
        return '금일은 학식정보를 제공하지 않습니다.'
    else:
        r = requests.get('https://www.smu.ac.kr/mbs/smu/jsp/restaurant/restaurant.jsp?configIdx=27145&id=smu_040501020000')
        bs = BeautifulSoup(r.text, 'html.parser')
        food_list = bs.select("#subContents > table > tbody:nth-of-type(1)")[0]
        string = ''
        string += timezone.localtime(timezone.now()).strftime('%Y년 %m월 %d일 ')
        string += '{}요일\n'.format(DAY_LIST[today])
        day = today*2
        string += '중식 (11:00~14:30)\n'
        string += '오늘의 메뉴 (6000원)\n'
        string += '----------------\n'
        string += food_list.find_all('div')[day].text
        string += food_list.find_all('div')[day+1].text
        return string
