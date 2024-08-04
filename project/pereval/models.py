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

    beauty_title = models.CharField(max_length=32, default='пер. ', verbose_name='Наименование препятствия')
    title = models.CharField(max_length=32, verbose_name='Наименование места')
    other_titles = models.CharField(max_length=32, null=True, blank=True, verbose_name='Другие наименования')
    connect = models.TextField(null=True, blank=True, verbose_name='Связь')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Когда добавлено')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user', verbose_name='Пользователь')
    coord = models.OneToOneField('Coord', on_delete=models.CASCADE, verbose_name='Координаты')
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUSES, default=new, verbose_name='Статус')

    def __str__(self):
        return f'{self.pk} {self.title} / {self.user.fam} {self.user.name}'


class User(models.Model):
    email = models.EmailField(max_length=150, verbose_name='Почта')
    fam = models.CharField(max_length=32, verbose_name='Фамилия')
    name = models.CharField(max_length=32, verbose_name='Имя')
    otc = models.CharField(max_length=32, null=True, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=32, verbose_name='Телефон')

    def __str__(self):
        return f'{self.fam} {self.name}'


class Coord(models.Model):
    latitude = models.FloatField(max_length=32, verbose_name='Широта')
    longitude = models.FloatField(max_length=32, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Level(models.Model):
    CHOICES = [
        ('1a', '1-А'),
        ('2a', '2-А'),
        ('3a', '3-А'),
        ('1b', '1-Б'),
        ('2b', '2-Б'),
        ('3b', '3-Б'),
    ]
    winter = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True, verbose_name='Зима')
    summer = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True, verbose_name='Лето')
    autumn = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True, verbose_name='Осень')
    spring = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True, verbose_name='Весна')

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'


class Image(models.Model):
    data = models.ImageField(upload_to=get_media_upload_path, null=True, blank=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images', verbose_name='Изображения')

    def __str__(self):
        return f'{self.pk} {self.title}'
