from django.urls import path
from .views import MappingListCreateView, MappingDetailView, PatientMappingsView

urlpatterns = [
    path("", MappingListCreateView.as_view()),
    path("<int:pk>/", MappingDetailView.as_view()),
    path("<int:patient_id>/", PatientMappingsView.as_view()),
]
