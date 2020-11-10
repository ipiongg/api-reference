from django.urls import path
from .views import TrabalhosList, TrabalhosDetailView


urlpatterns = [
    path('', TrabalhosList.as_view()),
    path('<int:id>', TrabalhosDetailView.as_view()),
]
