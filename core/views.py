from rest_framework import permissions, viewsets
from .models import Member
from .serializer import MemberSerializer,MemberSimpleSerializer
from rest_framework.response import Response


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request, *args, **kwargs):
        queryset = Member.objects.all()
        serializer = MemberSimpleSerializer(queryset, many=True)
        return Response(serializer.data)