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
    class Meta:
        model = Image
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        if self.is_valid():
            user = User.object.filter(email=self.validated_data.get('email'))

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

    class Meta:
        model = User
        fields = ('email', 'phone', 'fam', 'otc', 'phone')


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%d %m %Y  %H:%M:%S', read_only=True)
    user = UserSerializer()
    coord = CoordSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ('user', 'add_time', 'beauty_title', 'title', 'other_titles', 'connect', 'coord', 'level', 'images', )
        read_only_fields = ('status', )
