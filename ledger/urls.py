# ledger/urls.py

from django.urls import path
from .views import RecipeDetailView, RecipeListView

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<int:pk>/detail/', RecipeDetailView.as_view(), name='recipe-detail'),
]

app_name = 'ledger'
