from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    instrument_type = models.CharField(max_length=255)
    
    
    def __str__(self) -> str:
        return self.first_name
    