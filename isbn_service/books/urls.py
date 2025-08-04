from django.urls import path
from . import views

urlpatterns = [
    path('book/<str:isbn>/', views.get_book_details, name='get_book_details')
]

