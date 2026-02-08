from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Status
from .serializers import StatusSerializer
# Create your views here.
class StatusViewer(APIView):
    def get(self, request, **kwargs):
        id = kwargs.get('id')
        status = Status.objects.get(pk=id)
        serializer = StatusSerializer(status, many=False)
        return Response(serializer.data)