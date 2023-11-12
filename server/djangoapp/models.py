from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='car make')
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    SEDAN = "SE"
    SUV = "SU"
    WAGON = "WA"

    MODEL_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "WAGON"),
    ]

    name = models.CharField(null=False, max_length=30, default='car make')
    dealer_id = models.IntegerField()
    carType = models.CharField(null=False, max_length=2, choices=MODEL_CHOICES, default=SEDAN)
    year = models.DateField(null=True)

    def __str__(self):
        return "Name: " + self.name + "," + \
            "Dealer ID: " + self.dealer_id + "," + \
            "Type: " + self.carType + "," + \
            "Year: " + self.year


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
