from django.db import models


class Shipment(models.Model):
    """Shipment class"""
    external_id = models.PositiveIntegerField(unique=True, verbose_name='External system ID')
    from_name = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)


