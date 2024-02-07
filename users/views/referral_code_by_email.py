from datetime import datetime

from rest_framework import generics, status
from rest_framework.response import Response

from users.models import ReferralCode
from users.serializers import ReferralCodeSerializer


class ReferralCodeByEmail(generics.GenericAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    lookup_field = "user__email"
    lookup_url_kwarg = "email"

    def get(self, request, email, *args, **kwargs):
        referral_code = ReferralCode.objects.filter(expiry_date__gt=datetime.today(), user__email=email).first()
        serializer = self.get_serializer(referral_code)
        return Response(serializer.data, status=status.HTTP_200_OK)
