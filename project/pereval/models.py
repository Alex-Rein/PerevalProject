from django.db import models

from pereval.utils import get_media_upload_path


# Create your models here.
class Pereval(models.Model):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'

    STATUSES = [
        (new, 'новый'),
        (pending, 'в обработке'),
        (accepted, 'принято'),
        (rejected, 'отклонено'),
    ]

    beauty_title = models.CharField(max_length=32, default='пер. ', blank=True)
    title = models.CharField(max_length=32, null=True, blank=True)
    other_titles = models.CharField(max_length=32, null=True, blank=True)
    connect = models.TextField(null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user')
    coord = models.OneToOneField('Coord', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUSES, default=new)


class User(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    otc = models.CharField(max_length=32, null=True, blank=True)
    phone = models.CharField(max_length=32)


class Coord(models.Model):
    latitude = models.FloatField(max_length=32, verbose_name='Широта')
    longitude = models.FloatField(max_length=32, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Level(models.Model):
    CHOICES = [
        ('1А', '1-А'),
        ('2А', '2-А'),
        ('3А', '3-А'),
        ('1Б', '1-Б'),
        ('2Б', '2-Б'),
        ('3Б', '3-Б'),
    ]
    winter = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True, verbose_name='Зима')
    summer = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True, verbose_name='Лето')
    autumn = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True, verbose_name='Осень')
    spring = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True, verbose_name='Весна')

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'


class Image(models.Model):
    data = models.ImageField(upload_to=get_media_upload_path)
    title = models.CharField(max_length=64)
    date_added = models.DateTimeField(auto_now_add=True)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.pk} {self.title}'
