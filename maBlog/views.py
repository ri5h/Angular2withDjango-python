from django.shortcuts import get_object_or_404,render
from django.http import JsonResponse

from .models import posts as postsData
# Create your views here.


def respo(data):
	result = {}
	result['status'] = "success"
	result['data'] = data
	return JsonResponse(result);

def index(request):
	message = "How you doin' ?"
	return respo(message)

def post(request,post_id):
	post = get_object_or_404(postsData, pk=post_id)
	data = {}
	data['author'] = post.author
	data['title'] = post.title
	data['id'] = post.id
	data['summary'] = post.summary
	data['date'] = post.date
	
	return respo(data)

def posts(resquet):
	#result = getallposts
	postList = postsData.objects.all()
	# print(post);
	response = []
	for p in postList:
		response_tmp = {}
		response_tmp['id'] = p.id
		response_tmp['summary'] = p.summary
		response_tmp['author'] = p.author
		response_tmp['date'] = p.date
		response_tmp['title'] = p.title
		response.append(response_tmp)
	return_data = {}
	return_data['status'] = "success"
	return_data['msg'] = "post fetch successfull"
	return_data['data'] = response

	return JsonResponse(return_data)

