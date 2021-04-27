from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone


# Башкы бет
def index(request):
	return render(request, 'index.html', {})
