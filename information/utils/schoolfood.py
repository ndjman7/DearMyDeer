import datetime
import requests
from bs4 import BeautifulSoup

day_dict = {
    '월': 0,
    '화': 1,
    '수': 2,
    '목': 3,
    '금': 4
}

__all__ = [
    'future_centennial_hall_food',
]


def future_centennial_hall_food(today):
    r = requests.get('https://www.smu.ac.kr/mbs/smu/jsp/restaurant/restaurant.jsp?configIdx=27144&id=smu_040501000000')
    bs = BeautifulSoup(r.text, 'html.parser')
    food_list = bs.find_all('tr')
    string = ''
    string += datetime.date.today().strftime('%Y년 %m월 %d일')
    string += '\n'
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
