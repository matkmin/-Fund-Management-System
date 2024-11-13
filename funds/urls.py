from django.urls import path
from .views import FundListCreateView, FundDetailView

urlpatterns = [
    path('', FundListCreateView.as_view(), name='fund-list-create'),
    path('<int:pk>/', FundDetailView.as_view(), name='fund-detail'),
]