from book.views import index, book_controller
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('book/', book_controller),
]
