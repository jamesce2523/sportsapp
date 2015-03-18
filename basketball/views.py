# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def home(request):
	context = {'message': 'This is a dynamic message variable!'}
	return render(request, "base.html", context)
