from django.test import TestCase
from django.contrib.auth.models import User
from selenium import webdriver

from .models import Question

# Create your tests here.


class TestModels(TestCase):

    def test_text(self):
        text = Question.objects.create(user=User.objects.create_user(username='chinigz', password='chingiz01'), text='Nma gap tincma', hashtag='sogliq', likes=1)
        obj1 = Question.objects.create(user=User.objects.create_user(username='speed', password='speed01'), text='OOP nima degani', hashtag='classes', likes=0)
        obj2 = Question.objects.create(user=User.objects.create_user(username='alabay', password='alabay01'), text='FP nma u', hashtag='function', likes=4)
        obj3 = Question.objects.create(user=User.objects.create_user(username='dilmurod', password='dilmurod01'), text='CMD qaytib ishlaydi', hashtag='tool', likes=1)
        obj4 = Question.objects.create(user=User.objects.create_user(username='roberto', password='roberto01'), text='HTTP bilan HTTPS ni farqi', hashtag='networking', likes=2)
        obj5 = Question.objects.create(user=User.objects.create_user(username='ronaldo', password='cristiano01'), text='Qanaq qilib 7ta oltin top olish mumkin', hashtag='tushingda', likes=21)
        self.assertEquals(text.text, 'Nma gap tincma')
        self.assertEquals(text.hashtag, 'sogliq')
        self.assertEquals(text.likes, 1)
        self.assertNotEquals(text.likes, 10)
        self.assertNotEquals(text.text, text.likes)
        self.assertNotEquals(text.hashtag, text.likes)
        self.assertNotEquals(text.likes, text.text)
        self.assertEquals(obj1.text, 'OOP nima degani')
        self.assertEquals(obj1.hashtag, 'classes')
        self.assertEquals(obj1.likes, 0)
        self.assertEquals(obj2.text, 'FP nma u')
        self.assertEquals(obj2.hashtag, 'function')
        self.assertEquals(obj2.likes, 4)
        self.assertEquals(obj3.text, 'CMD qaytib ishlaydi')
        self.assertEquals(obj3.hashtag, 'tool')
        self.assertEquals(obj3.likes, 1)
        self.assertEquals(obj4.text, 'HTTP bilan HTTPS ni farqi')
        self.assertEquals(obj4.hashtag, 'networking')
        self.assertEquals(obj4.likes, 2)
        self.assertEquals(obj5.text, 'Qanaq qilib 7ta oltin top olish mumkin')
        self.assertEquals(obj5.hashtag, 'tushingda')
        self.assertEquals(obj5.likes, 21)

    def test_failure(self):
        obj1 = Question.objects.create(user=User.objects.create_user(username='chinigz', password='chingiz01'), text='Nma gap tincma', hashtag='sogliq', likes=1)
        obj2 = Question.objects.create(user=User.objects.create_user(username='speed', password='speed01'), text='OOP nima degani', hashtag='classes', likes=0)
        obj3 = Question.objects.create(user=User.objects.create_user(username='alabay', password='alabay01'), text='FP nma u', hashtag='function', likes=4)
        obj4 = Question.objects.create(user=User.objects.create_user(username='dilmurod', password='dilmurod01'), text='CMD qaytib ishlaydi', hashtag='tool', likes=1)
        obj5 = Question.objects.create(user=User.objects.create_user(username='roberto', password='roberto01'), text='HTTP bilan HTTPS ni farqi', hashtag='networking', likes=2)
        obj6 = Question.objects.create(user=User.objects.create_user(username='ronaldo', password='cristiano01'), text='Qanaq qilib 7ta oltin top olish mumkin', hashtag='tushingda', likes=21)
        self.assertNotEquals(obj1.text, 'Nam gap tincma')
        self.assertNotEquals(obj1.hashtag, 'soglig')
        self.assertNotEquals(obj1.likes, 2)
        self.assertNotEquals(obj2.text, 'OOP nma degani')
        self.assertNotEquals(obj2.hashtag, 'classess')
        self.assertNotEquals(obj2.likes, 1)
        self.assertNotEquals(obj3.text, 'DP nma u')
        self.assertNotEquals(obj3.hashtag, 'tool')
        self.assertNotEquals(obj3.likes, '2')
        self.assertNotEquals(obj4.text, 'SMS qaytib ishlaydi')
        self.assertNotEquals(obj4.hashtag, 'tools')
        self.assertNotEquals(obj4.likes, 2)
        self.assertNotEquals(obj5.text, 'HTTS bilan HTTP ni farqi')
        self.assertNotEquals(obj5.hashtag, 'network')
        self.assertNotEquals(obj5.likes, 1)
        self.assertNotEquals(obj6.text, 'Qanaq qilib 6ta oltin top olish mumkin')
        self.assertNotEquals(obj6.hashtag, 'ok')
        self.assertNotEquals(obj6.likes, 20)


class TestView(TestCase):
    def setUp(self) -> None:
        obj1 = Question.objects.create(user=User.objects.create_user(username='chinigz', password='chingiz01'),
                                       text='Nma gap tincma', hashtag='sogliq', likes=1)
        obj2 = Question.objects.create(user=User.objects.create_user(username='speed', password='speed01'),
                                       text='OOP nima degani', hashtag='classes', likes=0)
        obj3 = Question.objects.create(user=User.objects.create_user(username='alabay', password='alabay01'),
                                       text='FP nma u', hashtag='function', likes=4)
        obj4 = Question.objects.create(user=User.objects.create_user(username='dilmurod', password='dilmurod01'),
                                       text='CMD qaytib ishlaydi', hashtag='tool', likes=1)
        obj5 = Question.objects.create(user=User.objects.create_user(username='roberto', password='roberto01'),
                                       text='HTTP bilan HTTPS ni farqi', hashtag='networking', likes=2)
        obj6 = Question.objects.create(user=User.objects.create_user(username='ronaldo', password='cristiano01'),
                                       text='Qanaq qilib 7ta oltin top olish mumkin', hashtag='tushingda', likes=21)

    def test_view(self):
        response = webdriver.Chrome()
        response.get('http://127.0.0.1:8000/ques')
        assert 'Nma gap tincma'
        assert 'sogliq'
        assert 'likes'
        assert 'OOP nima degani'
        assert 'classes'
        assert '0'
        assert 'function'
        assert 'FP nma u'
        assert 'CMD qaytib ishlaydi'
        assert 'tool'
        assert 'HTTP bilan HTTPS ni farqi'
        assert 'networking'
