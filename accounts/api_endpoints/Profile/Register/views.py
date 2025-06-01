from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site


from accounts.api_endpoints.Profile.Register.serializers import RegisterSerializer
from accounts.api_endpoints.Profile.Register.email_send import send_normal_email


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relative_link = reverse("email-verify")
            absurl = "http://" + current_site + relative_link + "?token=" + str(token)
            email_body = f"Hi {user.username} Use the link below to verify your email \n{absurl}"
            data = {
                "email_subject": "Verify your email",
                "email_body": email_body,
                "to_email": user.email,
            }
            send_normal_email(data)
            return Response({"msg": "Registration successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)