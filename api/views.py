from .serializer import URLSerializer, SignupSerializer, ReportedURLSSerializer
from ml.detection import detect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import ReportedURL
from rest_framework import pagination
from rest_framework import status



class SignUPView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(data.errors)

class DetectView(generics.GenericAPIView):
    serializer_class = URLSerializer
    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            url = data.validated_data['url']
            phish = detect(url)
            return Response(phish)
        else:
            return Response(data.errors)

class ReportView(generics.GenericAPIView):
    serializer_class = URLSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            user = request.user

            obj, created = ReportedURL.objects.get_or_create(url=data.validated_data['url'], user=user)
            
            if created:
                return Response({
                    'msg' : "Successfully saved"
                })
            else:
                return Response({
                    'msg': 'You have already reported the url'
                })
        else:
            return Response(data.errors)


class StatsUserView(generics.ListAPIView):
    queryset = ReportedURL.objects.all()
    serializer_class = ReportedURLSSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = pagination.PageNumberPagination