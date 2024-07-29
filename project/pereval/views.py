from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers import CoordSerializer, LevelSerializer, ImageSerializer, PerevalSerializer, UserSerializer
from .models import Coord, Level, Image, Pereval, User


class CoordViewSet(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['get', 'post', 'patch', 'list']

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            print('=============')
            print(serializer.data)
            print('=============')
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data['id'],
            })
        else:
            print(serializer.errors)
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad Request',
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка подключения к базе данных',
                'id': None,
            })

    def list(self, request, *args, **kwargs):
        queryset = Pereval.objects.all()
        print('=============')
        print(self.request.query_params.get('email'))
        print('=============')
        email = self.request.query_params.get('email')
        if email is not None:
            queryset = queryset.filter(user__email=email)
            print('=============')
            print(queryset)
            print('=============')
            serializer = PerevalSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            super().list(request, *args, **kwargs)

    # def retrieve(self, request, pk=None, **kwargs):  # Получилось то же что и родительский метод
    #     pereval = get_object_or_404(self.queryset, pk=pk)
    #     serializer = PerevalSerializer(pereval)
    #     return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        pass

