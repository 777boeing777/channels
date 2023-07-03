from django.http import HttpResponse
from django.shortcuts import render
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def index(request):
    return render(request, 'index.html', {'room_name': 'broadcast'})

