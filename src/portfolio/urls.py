from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.PortfolioView.as_view(), name='portfolio'),
    path('<slug:slug>/',
        views.ProjectDetailView.as_view(),
        name='project_detail'),
]
