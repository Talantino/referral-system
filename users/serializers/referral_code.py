from datetime import datetime

from rest_framework import serializers

from users.models import ReferralCode
from users.utils import generate_code


class ReferralCodeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    code = serializers.CharField(read_only=True)

    class Meta:
        model = ReferralCode
        fields = "__all__"

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["code"] = generate_code()
        ReferralCode.objects.filter(user=validated_data["user"], expiry_date__gt=datetime.today(), is_active=True).update(is_active=False)
        return super().create(validated_data)
