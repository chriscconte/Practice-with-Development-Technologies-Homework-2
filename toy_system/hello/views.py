from django.shortcuts import render
import textwrap
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import View

from .models import Person

def detail(request, person_id):
    person = Person.objects.get(id=person_id)
    context = {
	'person': person,
    }
    return render(request,'hello/detail.html',context)

def index(request):
    team_members = Person.objects.all()
    context = {
	'team_members': team_members,
    }
    return render(request,'hello/index.html',context)
