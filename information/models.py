from django.db import models


class DeerSchoolFood(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    future_centennial_hall_food = models.TextField(null=True)
    millennium_hall_food = models.TextField(null=True)

