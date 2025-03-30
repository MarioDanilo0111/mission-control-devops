from django.db import models

# Create your models here.

class RocketLog(models.Model):
  mission_name = models.CharField(max_length=100)
  launch_date = models.DateTimeField()
  success = models.BooleanField(default=True)
  notes = models.TextField(blank=True)

  def __str__(self):
    return f"{self.mission_name} ({'✅' if self.success else '❌'})"