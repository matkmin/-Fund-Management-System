from django.shortcuts import render
from .models import InvestmentFund
from .serializers import InvestmentFundSerializer
from rest_framework import generics

# Create your views here.

class FundListCreateView(generics.ListCreateAPIView):
    queryset = InvestmentFund.objects.all()
    serializer_class = InvestmentFundSerializer

class FundDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvestmentFund.objects.all()
    serializer_class = InvestmentFundSerializer