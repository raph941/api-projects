from django.db import models


class GeoCode(models.Model):
    """
    save the amount of remaining free request i can make
    """
    request_count = models.IntegerField() 

