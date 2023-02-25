from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers import UserSerializer
from sso.jwt import *

class UserProfileAPIView(RetrieveModelMixin, GenericAPIView):
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        """
        User profile
        Get profile of current logged in user.
        """
        # token = request.headers.get('authorization').split('Bearer')[1]
        # print (token)
        token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ5OGY0OWJjNmNhNDU4MWVhZThkZmFkZDQ5NGZjZTEwZWEyM2FhYjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMTA3OTAwNzc0OTQ1NC1hYnJmdjluaDEzbmhnYTEyb2VqNmlrNDVlcTM3YnJkOC5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjEwNzkwMDc3NDk0NTQtYWJyZnY5bmgxM25oZ2ExMm9lajZpazQ1ZXEzN2JyZDguYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTc1Mjk3OTQ2ODM5ODAyMzU1NjAiLCJoZCI6InRyYXZjbGFuLmNvbSIsImVtYWlsIjoicHVzaHBlbmRyYS5ndXB0YUB0cmF2Y2xhbi5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IkJ6S0hUU3NubjJkUGQ3Qll6YVhnV2ciLCJuYW1lIjoiUHVzaHBlbmRyYSBHdXB0YSIsImdpdmVuX25hbWUiOiJQdXNocGVuZHJhIiwiZmFtaWx5X25hbWUiOiJHdXB0YSIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNjM5OTkxNjMzLCJleHAiOjE2Mzk5OTUyMzMsImp0aSI6ImE2N2ZhNTMwNTdkMDViNzYwNjAyMmUyNTdiOWUyYTAzZmIyODU5YjYifQ.ZjJ4YdIrq8pYKXPFuoXtP-b94chAXpmEm7EorxHeV8yyI6fibp3-N5ByJFT7RqBnhKUY9nU0Qq9dlyRbAtchike6GEY37tJadBUmK_rUFzjSfAv9bLTb-t_avjxevjVtTRF5nE5m5v0UNhky6yCncr0nh5ovzoLUMAaMhcbLylSGKpM0UlQOSfsDsVfb25TWqPvSPXcg3vzxjQQ8LkiMIkVB1SR7HBuIdJzGHMc75D2ivxe-wROalzep4II0IZXHCmD4AudNNsTVYQ2EkZuynN01IFX55MSqsR4tJgW4s4qw9VIs3CH-c83xSidBI3zMmEbqvpZ3BQe0fOOj86dx3Q'
        cognito_jwt_decode_handler(token.strip())

        return self.retrieve(request, *args, **kwargs)