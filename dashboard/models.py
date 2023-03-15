from django.db import models

# Create your models here.

def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'

class ImagemAlbum(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)
    

class Imagem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=300)
    length = models.FloatField(default=300)
    album = models.ForeignKey(ImagemAlbum, related_name='images', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name