from django.urls import path
from .views import reviews_list, add_review

urlpatterns = [
    path('reviews/', reviews_list, name='reviews_list'),
    path("reviews/add/", add_review, name='add_review')
]