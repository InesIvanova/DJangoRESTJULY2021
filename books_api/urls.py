from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookListCreate.as_view()),
    path('<int:book_id>', views.BookGetUpdateDelete.as_view()),
]