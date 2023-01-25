from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    # path('my-favorites/', views.FavoriteList.as_view()),
    path('projects/<int:pk>/delete/', views.DeleteProject.as_view()),
    path('projects/my-favorites/', views.FavouritedProjectList.as_view()),
    path('projects/<int:pk>/favorite/', views.FavoriteProject.as_view()),
    path('projects/<int:pk>/unfavorite/', views.UnfavoriteProject.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
