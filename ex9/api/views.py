import json

from django.shortcuts import render
from django.views import View
# Create your views here.
from gallery.models import Photo, Album
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse, HttpResponseBadRequest

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')

def FavPhoto(request, *args, **kwargs):
    answer = {'error':False}
    response = {}
    if request.body:
        print(request.body)
        res = json.loads(request.body)
        try:
            pk = int(res['pk'])
            photo = get_object_or_404(Photo, id=pk)
            request.user.favorite_photos.add(photo)
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
        except Exception as e:
            answer['error'] = str(e)
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            print('views py error = ', e)
    response['Content-Type'] = 'application/json'
    return response

def FavAlbum(request, *args, **kwargs):
    answer = {'error':False}
    response = {}
    if request.body:
        print(request.body)
        res = json.loads(request.body)
        try:
            pk = int(res['pk'])
            album = get_object_or_404(Album, id=pk)
            request.user.favorite_albums.add(album)
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
        except Exception as e:
            answer['error'] = str(e)
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            print('views py error = ', e)
    response['Content-Type'] = 'application/json'
    return response

def UnFavPhoto(request, *args, **kwargs):
    answer = {'error':False}
    response = {}
    if request.body:
        print(request.body)
        res = json.loads(request.body)
        try:
            pk = int(res['pk'])
            photo = get_object_or_404(Photo, id=pk)
            request.user.favorite_photos.remove(photo)
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
        except Exception as e:
            answer['error'] = str(e)
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            print('views py error = ', e)
    response['Content-Type'] = 'application/json'
    return response

def UnFavAlbum(request, *args, **kwargs):
    answer = {'error':False}
    response = {}
    if request.body:
        print(request.body)
        res = json.loads(request.body)
        try:
            pk = int(res['pk'])
            album = get_object_or_404(Album, id=pk)
            request.user.favorite_albums.remove(album)
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
        except Exception as e:
            answer['error'] = str(e)
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            print('views py error = ', e)
    response['Content-Type'] = 'application/json'
    return response
