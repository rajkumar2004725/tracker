from django.urls import path
from .views import ActionListCreateView, ActionRetrieveUpdateDeleteView

urlpatterns = [
    path('api/actions/', ActionListCreateView.as_view(), name='action-list-create'),
    path('api/actions/<int:pk>/', ActionRetrieveUpdateDeleteView.as_view(), name='action-detail'),
]
