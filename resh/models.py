from django.db import models


# Create your models here.
class CustomLocation(models.Model):
    name = models.CharField('Local', max_length=50)
    region = models.CharField('Região', max_length=20)
    latitude = models.CharField('Latitude', max_length=20)
    longitude = models.CharField('Longitude', max_length=20)
    time_zone = models.CharField('Timezone', max_length=50)
    elevation = models.CharField('Elevação', max_length=20)

    class Meta:
        ordering = ('name', 'region')
        verbose_name_plural = "locais"
        verbose_name = "local"
