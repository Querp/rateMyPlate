from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('db/', views.database, name='database'),
    path('logout/', views.custom_logout, name='logout'),
    
    path("competition/<int:pk>/", views.competition_detail, name="competition"), 
    path("competition/<int:competition_id>/post", views.post_form, name="post_form"),
    path("competition/new_competition/", views.new_competition, name="new_competition"),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/register', views.register, name='register'),
]


