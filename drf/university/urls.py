from django.urls import path
from university import views

urlpatterns = [
    path('', views.UniversityListCreate.as_view()),
    path('<pk>/', views.UniversityRetrieveUpdateDestroy.as_view())
]
