from rest_framework.response import Response
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend

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
    http_method_names = ['get', 'post', 'patch']
    # http_method_names = ['get', 'post', 'patch', 'list']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__email']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

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

    # def list(self, request, *args, **kwargs):  # Переделал на фильтрсет
    #     queryset = Pereval.objects.all()
    #     print('=============')
    #     print(self.request.query_params.get('user__email'))
    #     print('=============')
    #     email = self.request.query_params.get('user__email')
    #     if email is not None:
    #         queryset = queryset.filter(user__email=email)
    #         print('=============')
    #         print(queryset)
    #         print('=============')
    #         serializer = PerevalSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None, **kwargs):  # Получилось то же что и родительский метод
    #     pereval = get_object_or_404(self.queryset, pk=pk)
    #     serializer = PerevalSerializer(pereval)
    #     return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != 'new':
            return Response({
                'state': '0',
                'message': f'Отклонено: изменение доступно только для новых немодерированных объектов.'
                           f'Статус вашего объекта - {instance.get_status_display()}'
            })
        serializer = PerevalSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'state': '1',
                'message': f'Изменения применены успешно'
            })
        else:
            return Response({
                'state': '0',
                'message': f'{serializer.errors["non_field_errors"][0]}'
            })
