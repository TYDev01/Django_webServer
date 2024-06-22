from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def newVisitor(request):
    visitName = request.query_params.get('visitor', 'usersname')
    client_ip = request.META.get('REMOTE_ADDR')
    location = 'New York'
    data = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitName}!"
    }
    return Response(data)

