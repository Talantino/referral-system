from datetime import datetime

from rest_framework import serializers

from users.models import User, ReferralCode


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "referral_code", "email")

    def validate(self, attrs):
        referral_code = attrs.get("referral_code")
        if referral_code and not ReferralCode.objects.filter(code=referral_code, expiry_date__gt=datetime.today(), is_active=True):
            raise serializers.ValidationError("invalid referral code")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
