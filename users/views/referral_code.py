from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.models import ReferralCode
from users.serializers import ReferralCodeSerializer


class ReferralCodeViewSet(ModelViewSet):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    permission_classes = [IsAuthenticated, ]
