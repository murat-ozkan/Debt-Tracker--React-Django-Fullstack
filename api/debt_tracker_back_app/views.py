from django.shortcuts import render
from .models import Debt
from .serializers import DebtSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class DebtView(ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    # ÖZelleştirma yapılabilir. Mesela debt create edildiğinde 
    # kullanıcıya mesaj yollanabilir. Başarılı işlem vs. gibi.
    # İlgili metodun overwrite edilmesi.

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     return Response("data":serializer.data, "message":"Successfully created", status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()