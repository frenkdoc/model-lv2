from django.urls import path

from .views import articoloDetailView, home

urlpatterns = [
    path("", home, name="homeviews"),
    path("articolo/<int:pk>", articoloDetailView, name="articolo_detail")
]
