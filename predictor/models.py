from django.db import models
from .import variables
from django.contrib.auth.models import User


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    educational_level = models.PositiveIntegerField(choices=variables.educational_level_choices)
    gender = models.PositiveIntegerField(choices=variables.gender_choices)
    source_of_income= models.PositiveIntegerField(choices=variables.source_of_income_choices)
    do_you_avoid_any_kind_of_food= models.PositiveIntegerField(choices=variables.y_n_choices)
    do_you_have_a_meal_time_table= models.PositiveIntegerField(choices=variables.y_n_choices)
    vegetables= models.PositiveIntegerField(choices=variables.food_choices)
    red_meat= models.PositiveIntegerField(choices=variables.food_choices)
    chicken= models.PositiveIntegerField(choices=variables.food_choices)
    fish= models.PositiveIntegerField(choices=variables.food_choices)
    milk= models.PositiveIntegerField(choices=variables.food_choices)
    dairy_product= models.PositiveIntegerField(choices=variables.food_choices)
    egg= models.PositiveIntegerField(choices=variables.food_choices)
    bread= models.PositiveIntegerField(choices=variables.food_choices)
    legumes= models.PositiveIntegerField(choices=variables.food_choices)
    fruits= models.PositiveIntegerField(choices=variables.food_choices)
    tea= models.PositiveIntegerField(choices=variables.food_choices)
    coffee= models.PositiveIntegerField(choices=variables.food_choices)
    fresh_juice= models.PositiveIntegerField(choices=variables.food_choices)
    soft_juice= models.PositiveIntegerField(choices=variables.food_choices)
    eba= models.PositiveIntegerField(choices=variables.food_choices)
    fufu= models.PositiveIntegerField(choices=variables.food_choices)
    yam= models.PositiveIntegerField(choices=variables.food_choices)
    rice= models.PositiveIntegerField(choices=variables.food_choices)
    beans= models.PositiveIntegerField(choices=variables.food_choices)
    elubo= models.PositiveIntegerField(choices=variables.food_choices)
    maize= models.PositiveIntegerField(choices=variables.food_choices)
    garri= models.PositiveIntegerField(choices=variables.food_choices)
    pounded_yam= models.PositiveIntegerField(choices=variables.food_choices)

    monday_BF= models.PositiveIntegerField(choices=variables.daily_choices)
    monday_LH= models.PositiveIntegerField(choices=variables.daily_choices)
    monday_DN= models.PositiveIntegerField(choices=variables.daily_choices)
    tuesday_BF= models.PositiveIntegerField(choices=variables.daily_choices)
    tuesday_LH= models.PositiveIntegerField(choices=variables.daily_choices)
    tuesday_DN= models.PositiveIntegerField(choices=variables.daily_choices)
    wednesday_BF= models.PositiveIntegerField(choices=variables.daily_choices)
    wednesday_LH= models.PositiveIntegerField(choices=variables.daily_choices)
    wednesday_DN= models.PositiveIntegerField(choices=variables.daily_choices)
    thursday_BF= models.PositiveIntegerField(choices=variables.daily_choices)
    thursday_LH= models.PositiveIntegerField(choices=variables.daily_choices)
    thursday_DN= models.PositiveIntegerField(choices=variables.daily_choices)
    friday_BF= models.PositiveIntegerField(choices=variables.daily_choices)
    friday_LH= models.PositiveIntegerField(choices=variables.daily_choices)
    friday_DN= models.PositiveIntegerField(choices=variables.daily_choices)
    saturday_BF= models.PositiveIntegerField(choices=variables.daily_choices)
    saturday_LH= models.PositiveIntegerField(choices=variables.daily_choices)
    saturday_DN= models.PositiveIntegerField(choices=variables.daily_choices)
    sunday_BF= models.PositiveIntegerField(choices=variables.daily_choices)
    sunday_LH= models.PositiveIntegerField(choices=variables.daily_choices)
    sunday_DN= models.PositiveIntegerField(choices=variables.daily_choices)

    def __str__(self):
        return self.user



class Reservation(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    reserv_date = models.DateField()
    numb_guests = models.PositiveIntegerField()
    alt_reserv_date = models.TimeField()
    time = models.TimeField()

    def __str__(self):
        return self.first_name +' '+ self.last_name +' --- '+ self.phone