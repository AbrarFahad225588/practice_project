from django.db import models

# Create your models here.

class PracticeModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField()
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    char_field = models.CharField(max_length=255)
    date_time_field = models.DateTimeField()
    