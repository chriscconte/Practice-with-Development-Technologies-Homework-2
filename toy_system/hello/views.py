from django.shortcuts import render, get_object_or_404
import textwrap
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    print (request.POST) 
    try:
        name = request.POST['name']
        bio = request.POST['bio'] 
    except (KeyError, person.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'hello/detail.html', {
            'person': person,
            'error-message': 'oops something went wrong',
        })
    else:
        person.person_name = name
        person.person_bio = bio
        person.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('detail', args=(person.id,)))
