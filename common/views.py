from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from .models import Media
from .serializers import MediaSerializer
from estates.auth import CsrfExemptSessionAuthentication


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
