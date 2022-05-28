from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Accounts
from .serializers import AccountsSerializer
from rest_framework.parsers import JSONParser


# Create your views here.

@csrf_exempt
def Accounts_list(request):
    if request.method == 'GET':
        queryset = Accounts.objects.all()
        serializer = AccountsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

