from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Coord, Level, Image, User, Pereval


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    data = serializers.URLField(required=False)

    class Meta:
        model = Image
        fields = ('data', 'title')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def save(self, **kwargs):
        if self.is_valid():
            user = User.objects.filter(email=self.validated_data.get('email'))

            if user.exists():
                return user.first()
            else:
                new_user = User.objects.create(
                    email=self.validated_data.get('email'),
                    fam=self.validated_data.get('fam'),
                    name=self.validated_data.get('name'),
                    otc=self.validated_data.get('otc'),
                    phone=self.validated_data.get('phone'),
                )
                return new_user


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%d %m %Y  %H:%M:%S', read_only=True)
    user = UserSerializer()
    coord = CoordSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True, required=False)
    status = serializers.CharField()

    class Meta:
        model = Pereval
        fields = ('add_time', 'beauty_title', 'title', 'other_titles',
                  'connect', 'user', 'coord', 'level', 'images', 'id', 'status')
<<<<<<< HEAD
=======
        # read_only_fields = ('status', 'add_time')

    # def create(self, validated_data, **kwargs):
    #     user = validated_data.pop('user')
    #     coord = validated_data.pop('coord')
    #     level = validated_data.pop('level')
    #     images = validated_data.pop('images')
    #
    #     user, created = User.objects.get_or_create(**user)
    #
    #     coord = Coord.objects.create(**coord)
    #     level = Level.objects.create(**level)
    #     pereval = Pereval.objects.create(**validated_data, user=user, coord=coord, level=level, status='new')
    #
    #     for image in images:
    #         data = image.pop('data')
    #         title = image.pop('title')
    #         Image.objects.create(data=data, pereval=pereval, title=title)
    #
    #     return pereval
>>>>>>> 4c3b267794809fb5f1f23172c401e39897af0666

    def validate(self, data):
        if self.instance:
            user = self.instance.user
            data_user = data['user']
            validation_fields = [
                user.name == data_user['name'],
                user.fam == data_user['fam'],
                user.otc == data_user['otc'],
                user.email == data_user['email'],
                user.phone == data_user['phone'],
            ]
            if data_user and not all(validation_fields):
                raise serializers.ValidationError('Отклонено: данные пользователя нельзя изменять')
            # elif self.instance.status != self.initial_data['status']:  # для практики
            #     raise serializers.ValidationError('Отклонено: поле статуса нельзя изменять')
        return data
