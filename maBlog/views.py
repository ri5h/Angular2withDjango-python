from django.shortcuts import render
from django.http import JsonResponse as respo
# Create your views here.


def index(request):
	result = {}
	result['result']= "success"
	result['message']= "How you doin' ?"
	return respo(result)