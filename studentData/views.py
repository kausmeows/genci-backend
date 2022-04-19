from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Certificate
from .serializers import certificateSerializer
from .models import generate_unique_code
from .utils import getCertiURL
from dotenv import load_dotenv
import os
load_dotenv()

@api_view(['GET'])
def getDetails():
    certificate = Certificate.objects.all()
    serializer = certificateSerializer(certificate, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def generate_certificate(request): 
    certi_data = request.data
    certi_data['certificateId'] = generate_unique_code()
    certi_data['certificateId'] = certi_data['event'] + certi_data['certificateId']
    certi_URL = getCertiURL(os.getenv('URL'))
    certi_data['certificateURL'] = certi_URL
    serializer = certificateSerializer(data=certi_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

