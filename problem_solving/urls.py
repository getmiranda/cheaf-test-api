from django.urls import path

from problem_solving import views


urlpatterns = [
    path('count-words/', views.count_words, name='count-words'),
    path('distance-two-points/',
         views.distance_two_points, name='distance-two-points'),
]
