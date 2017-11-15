# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LandsatCatalog(models.Model):
    scene_id = models.CharField(max_length=50, unique=True)
    landsat_product_id = models.CharField(max_length=50,default=None, unique=True)
    sensor = models.CharField(max_length=50,default=None)
    acquisition_date = models.DateTimeField(default=None)
    path = models.IntegerField(default=-1)
    row = models.IntegerField(default=-1)
    cloud_full = models.FloatField(default=-1)
    day_night = models.CharField(max_length=50, default=None)
    image_quality = models.IntegerField(default=-1)
    ground_control_points_model = models.CharField(max_length=50, default=None)
    browse_url = models.CharField(max_length=200, default=None)
    
class LansatAWS(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    entity_id = models.CharField(max_length=100)
    acquisitionDate = models.DateTimeField(default=None)
    cloudCover = models.FloatField(default=-1.0)
    processingLevel = models.CharField(max_length=10)
    path = models.IntegerField(default=-1)
    row = models.IntegerField(default=-1)
    min_lat = models.FloatField(default=-1)
    min_lon = models.FloatField(default=-1)
    max_lat = models.FloatField(default=-1)
    max_lon = models.FloatField(default=-1)
    download_url = models.CharField(max_length=200)