# from rest_framework import serializers
# from django.contrib.auth import get_user_model

# from accounts.api_endpoints.Profile.Register.tokens import (
#     generate_email_confirmation_token,
#     verify_email_confirmation_token
# )

# User = get_user_model()

# class EmailConfirmationRequestSerializer(serializers.Serializer):
#     email = serializers.EmailField()

#     def validate_email(self, value):
#         try:
#             self.user = User.objects.get(email=value)
#         except User.DoesNotExist:
#             return value
        
#         raise serializers.ValidationError("User with this email already exists.")

#     def save(self):
#         token = generate_email_confirmation_token(self.user)
#         self.context["send_email"](self.user.email, token)


# class EmailConfirmationConfirmSerializer(serializers.Serializer):
#     token = serializers.CharField()

#     def validate(self, attrs):
#         user_id = verify_email_confirmation_token(attrs["token"])
#         if not user_id:
#             raise serializers.ValidationError("Invalid or expired token.")
#         self.user = User.objects.get(pk=user_id)
#         return attrs

#     def save(self):
#         self.user.is_active = True
#         self.user.save()