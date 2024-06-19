from django.db import models
from musician.models import MusicianModel
# Create your models here.
class AlbumsModel(models.Model):
    album_name = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.CharField(max_length=255)
    
    musician = models.ForeignKey(MusicianModel,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.album_name