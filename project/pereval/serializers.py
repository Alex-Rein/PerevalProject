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
    image = serializers.URLField(required=False)

    class Meta:
        model = Image
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['email', 'fam', 'name', 'otc', 'phone']

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

    class Meta:
        model = Pereval
        fields = ('add_time', 'beauty_title', 'title', 'other_titles',
                  'connect', 'user', 'coord', 'level', 'images', 'id', )
        read_only_fields = ('status', )

    def validate(self, data):
        if self.instance:
            user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = (
                user.email != data_user['email'],
                user.fam != data_user['fam'],
                user.name != data_user['name'],
                user.otc != data_user['otc'],
                user.phone != data_user['phone'],
            )
            if data_user and any(validating_user_fields):
                raise serializers.ValidationError('Отклонено: данные пользователя нельзя изменять')
            elif self.instance.status != data.get('status'):
                raise serializers.ValidationError('Отклонено: поле статуса нельзя изменять')
            elif self.instance.add_time != data.get('add_time'):
                raise serializers.ValidationError('Отклонено: поле времени добавления нельзя изменять')
        return data
