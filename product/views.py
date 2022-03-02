from django.shortcuts import render
from django.http import JsonResponse


def updateItem(request):
    return JsonResponse('Item added', safe = False)