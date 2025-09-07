from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError("Passwords must match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        user = User(
            username=validated_data["username"], email=validated_data.get("email", "")
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        try:
            self.token = RefreshToken(attrs["refresh"])
        except Exception:
            raise serializers.ValidationError("Invalid or expired refresh token.")
        return attrs

    def save(self, **kwargs):
        # Blacklist the refresh token
        self.token.blacklist()
