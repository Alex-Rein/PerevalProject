from django.test import TestCase
from django.urls import reverse

from pereval.models import Coord, Image, Level, User, Pereval
from pereval.serializers import PerevalSerializer

from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.


class TestPerevalAPI(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='BT_test_1',
            title='T_test_1',
            other_titles='OT_test_1',
            connect='C_test_1',
            user=User.objects.create(
                email='user_test_1@mail.ru',
                fam='fam_test_1',
                name='name_test_1',
                otc='otc_test_1',
                phone='+79876543210'
            ),
            coord=Coord.objects.create(
                latitude='11.11111',
                longitude='22.22222',
                height='333'
            ),
            level=Level.objects.create(
                winter='1a',
                spring='1a',
                summer='1a',
                autumn='1a'
            ),
        )

        self.image_1 = Image.objects.create(
            title='image_test_1',
            data='image_test_1.jpg',
            pereval_id=self.pereval_1
        )

        self.pereval_2 = Pereval.objects.create(
            beauty_title='BT_test_2',
            title='T_test_2',
            other_titles='OT_test_2',
            connect='C_test_2',
            user=User.objects.create(
                email='user_test_2@mail.ru',
                fam='fam_test_2',
                name='name_test_2',
                otc='otc_test_2',
                phone='+70123456789'
            ),
            coord=Coord.objects.create(
                latitude='33.33333',
                longitude='44.44444',
                height='2222'
            ),
            level=Level.objects.create(
                winter='',
                spring='1a',
                summer='',
                autumn='1a'
            ),
        )

        self.image_2 = Image.objects.create(
            title='image_test_2',
            data='image_test_2.jpg',
            pereval_id=self.pereval_2
        )

    def test_get_list(self):
        url = f'{reverse("pereval-list")}?get_all=true'
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('pereval-detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class TestPerevalSerializer(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='BT_test_1',
            title='T_test_1',
            other_titles='OT_test_1',
            connect='C_test_1',
            user=User.objects.create(
                email='user_test_1@mail.ru',
                fam='fam_test_1',
                name='name_test_1',
                otc='otc_test_1',
                phone='+79876543210'
            ),
            coord=Coord.objects.create(
                latitude=11.11111,
                longitude=22.22222,
                height=333
            ),
            level=Level.objects.create(
                winter='1a',
                spring='1a',
                summer='1a',
                autumn='1a'
            ),
        )

        self.image_1 = Image.objects.create(
            title='image_test_1',
            data='image_test_1.jpg',
            pereval_id=self.pereval_1
        )

        self.pereval_2 = Pereval.objects.create(
            beauty_title='BT_test_2',
            title='T_test_2',
            other_titles='OT_test_2',
            connect='C_test_2',
            user=User.objects.create(
                email='user_test_2@mail.ru',
                fam='fam_test_2',
                name='name_test_2',
                otc='otc_test_2',
                phone='+70123456789'
            ),
            coord=Coord.objects.create(
                latitude=33.33333,
                longitude=44.44444,
                height=2222
            ),
            level=Level.objects.create(
                winter='',
                spring='1a',
                summer='',
                autumn='1a'
            ),
        )

        self.image_2 = Image.objects.create(
            title='image_test_2',
            data='image_test_2.jpg',
            pereval_id=self.pereval_2
        )

    def test_get_list(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        expected_data = [
            {
                'id': self.pereval_1.id,
                'beauty_title': 'BT_test_1',
                'title': 'T_test_1',
                'other_titles': 'OT_test_1',
                'connect': 'C_test_1',
                'add_time': self.pereval_1.add_time.strftime('%d %m %Y  %H:%M:%S'),
                'status': 'new',
                'user': {
                    'id': self.pereval_1.user.id,
                    'email': 'user_test_1@mail.ru',
                    'fam': 'fam_test_1',
                    'name': 'name_test_1',
                    'otc': 'otc_test_1',
                    'phone': '+79876543210'
                },
                'coord': {
                    'id': self.pereval_1.coord.id,
                    'latitude': 11.11111,
                    'longitude': 22.22222,
                    'height': 333
                },
                'level': {
                    'id': self.pereval_1.level.id,
                    'winter': '1a',
                    'spring': '1a',
                    'summer': '1a',
                    'autumn': '1a'
                },
                'images': [
                    {
                        'title': 'image_test_1',
                        'data': 'image_test_1.jpg'
                    },
                ]
            },

            {
                'id': self.pereval_2.id,
                'beauty_title': 'BT_test_2',
                'title': 'T_test_2',
                'other_titles': 'OT_test_2',
                'connect': 'C_test_2',
                'add_time': self.pereval_2.add_time.strftime('%d %m %Y  %H:%M:%S'),
                'status': 'new',
                'user': {
                    'id': self.pereval_2.user.id,
                    'email': 'user_test_2@mail.ru',
                    'fam': 'fam_test_2',
                    'name': 'name_test_2',
                    'otc': 'otc_test_2',
                    'phone': '+70123456789'
                },
                'coord': {
                    'id': self.pereval_2.coord.id,
                    'latitude': 33.33333,
                    'longitude': 44.44444,
                    'height': 2222
                },
                'level': {
                    'id': self.pereval_2.level.id,
                    'winter': '',
                    'spring': '1a',
                    'summer': '',
                    'autumn': '1a'
                },
                'images': [
                    {
                        'title': 'image_test_2',
                        'data': 'image_test_2.jpg'
                    },
                ]
            }
        ]
        self.assertEquals(serializer_data, expected_data)
