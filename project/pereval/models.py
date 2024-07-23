from django.db import models


# Create your models here.
class Pereval(models.Model):
    new = 'NW'
    pending = 'PE'
    accepted = 'AC'
    rejected = 'RE'

    STATUSES = [
        (new, 'New'),
        (pending, 'Pending'),
        (accepted, 'Accepted'),
        (rejected, 'Rejected'),
    ]

    beauty_title = models.CharField(max_length=32, default='пер. ')
    title = models.CharField(max_length=32)
    other_titles = models.CharField(max_length=32, null=True, blank=True)
    connect = models.CharField(max_length=8, default='')
    add_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    coord_id = models.OneToOneField('Coord', on_delete=models.CASCADE)
    level_id = models.ForeignKey('Level', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUSES, default=new)


class User(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    otc = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)


class Coord(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Level(models.Model):
    CHOICES = [
        ('1А', '1-А'),
        ('2А', '2-А'),
        ('3А', '3-А'),
        ('1Б', '1-Б'),
        ('2Б', '2-Б'),
        ('3Б', '3-Б'),
    ]
    winter = models.CharField(max_length=2, choices=CHOICES)
    summer = models.CharField(max_length=2, choices=CHOICES)
    autumn = models.CharField(max_length=2, choices=CHOICES)
    spring = models.CharField(max_length=2, choices=CHOICES)


class Image(models.Model):
    data = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=64)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE)
