from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("competition/<int:pk>/", views.competition, name="competition"),
    path("competition/<int:competition_id>/post", views.post_form, name="post_form"),
    
]


