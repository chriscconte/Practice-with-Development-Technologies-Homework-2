# -*- coding: utf-8 -*-
from django.test import TestCase
from .views import *
from .models import *

# Create your tests here.

class HelloTests(TestCase):

    def setUp(self):
        Person.objects.create(person_name="lion", person_bio="roar")
        Person.objects.create(person_name="cat", person_bio="meow")

    def test_nameTest(self):
        p = get_object_or_404(Person, pk=1)

        self.assertIs((str("lion") ==  str(p.person_name)), True)

    def test_nameChange(self):
        class request(object):
            POST = {'name': 'name_test', 'bio':'bio_test'}
            def __init__(self):
                self.POST['name'] = 'name_test'


        post = request()
        edit(post, 1)
        
        p = get_object_or_404(Person, pk=1)
        edit(post, 1)
        
        self.assertIs(str(p.person_name) == post.POST['name'], True)
        

