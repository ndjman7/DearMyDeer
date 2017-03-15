import calendar

from django.utils import timezone

__all__ = [
    'return_today',
]


def return_today():
    today = timezone.localtime(timezone.now()).strftime('%Y%m%d')
    this_year = int(today[:4])
    this_month = int(today[4:6])
    this_date = int(today[6:])
    this_year_calendar = calendar.Calendar(calendar.SUNDAY).yeardays2calendar(this_year, 1)
    month = this_year_calendar[int(this_month) - 1][0]
    for week in month:
        for date in week:
            if date[0] == int(this_date):
                return date[1]
