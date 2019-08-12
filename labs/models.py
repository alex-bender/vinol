from django.db import models
from django.contrib.auth.models import User

SCAN = 'SC'
DEVELOP = 'DE'

ORDER_TYPE_CHOICES = (
    (SCAN, 'Scan'),
    (DEVELOP, 'Develop'),
)

class Activity(models.Model):
    type = models.CharField(
        max_length=2,
        choices=ORDER_TYPE_CHOICES,
        default=DEVELOP
    )
    operator = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    order = models.ForeignKey(
        'Order', null=True, on_delete=models.SET_NULL,
        )
    price = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)
    count = models.PositiveSmallIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Activity: {} {}".format(
            self.type, self.count)


class Client(models.Model):
    """Represents the client of the V-Lab"""
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    total_sum = models.DecimalField(
        blank=True, null=True,
        max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Client " + self.name


class Order(models.Model):
    """Describe what should be done"""
    number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    issuance_date = models.DateField()
    done = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Order {} for {}".format(self.number, self.client)
