from django.urls import path
from .views import CreateView, ReadView, UpdateView, DeleteView, ListView

urlpatterns = [
    path('', ListView.as_view()),
    path('create/', CreateView.as_view()),
    path('<int:id>/', ReadView.as_view()),
    path('update/<int:id>/', UpdateView.as_view()),
    path('delete/<int:id>/', DeleteView.as_view())
]