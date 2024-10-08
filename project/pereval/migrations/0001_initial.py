# Generated by Django 4.2.14 on 2024-07-24 14:36

from django.db import migrations, models
import django.db.models.deletion
import pereval.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=32, verbose_name='Широта')),
                ('longitude', models.FloatField(max_length=32, verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, choices=[('1А', '1-А'), ('2А', '2-А'), ('3А', '3-А'), ('1Б', '1-Б'), ('2Б', '2-Б'), ('3Б', '3-Б')], max_length=2, null=True, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, choices=[('1А', '1-А'), ('2А', '2-А'), ('3А', '3-А'), ('1Б', '1-Б'), ('2Б', '2-Б'), ('3Б', '3-Б')], max_length=2, null=True, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, choices=[('1А', '1-А'), ('2А', '2-А'), ('3А', '3-А'), ('1Б', '1-Б'), ('2Б', '2-Б'), ('3Б', '3-Б')], max_length=2, null=True, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, choices=[('1А', '1-А'), ('2А', '2-А'), ('3А', '3-А'), ('1Б', '1-Б'), ('2Б', '2-Б'), ('3Б', '3-Б')], max_length=2, null=True, verbose_name='Весна')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fam', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('otc', models.CharField(blank=True, max_length=32, null=True)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(blank=True, default='пер. ', max_length=32)),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('other_titles', models.CharField(blank=True, max_length=32, null=True)),
                ('connect', models.TextField(blank=True, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'в обработке'), ('accepted', 'принято'), ('rejected', 'отклонено')], default='new', max_length=10)),
                ('coord', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pereval.coord')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='pereval.user')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(upload_to=pereval.utils.get_media_upload_path)),
                ('title', models.CharField(max_length=64)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pereval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.pereval')),
            ],
        ),
    ]
