from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello_world(requests):
#     return Response({'msg':'Hello World'})

@api_view(['POST'])
def hello_world(request):
    if request.method == "POST":
        return Response({'msg':'This is Post Request', 'data':request.data})