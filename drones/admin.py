from django.contrib import admin
from drones import models
# Register your models here.
admin.site.register(models.Competition)
admin.site.register(models.Drone)
admin.site.register(models.DroneCategory)
admin.site.register(models.Pilot)