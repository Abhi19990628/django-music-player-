from django.db import models,

class Album(models.Model):
    album_name=models.CharField(max_length=20)
    album_image=models.FileField(upload_to="images")
    
    def __str__(self) :
        return self.album_name
    
class Songs(models.Model):
    name=models.CharField(max_length=20)
    album_name=models.ForeignKey(Album,on_delete=models.CASCADE)
    song=models.FileField(upload_to="song")
    picture=models.FileField(upload_to="picture")
    singer=models.CharField(max_length=20)
