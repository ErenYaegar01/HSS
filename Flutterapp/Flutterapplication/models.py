from django.db import models

class SDVData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    speed = models.FloatField()
    distance_traveled = models.FloatField()
    fuel_consumed = models.FloatField()
    sensor_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Data at {self.timestamp} | Speed: {self.speed} km/h"
