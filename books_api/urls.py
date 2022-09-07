from django.urls import path
from . import views


urlpatterns = [
    path('external-books/', views.external_books, name='external-books'),
    path('v1/books', views.books, name='books-get-post'),
    path('v1/books/<int:book_id>', views.update_book, name='update-book'),
]
