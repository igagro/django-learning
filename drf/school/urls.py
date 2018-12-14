from django.urls import path
from school import views

urlpatterns = [
    path('', views.SchoolListCreate.as_view()),
    path('<pk>/', views.SchoolRetrieveUpdateDestroy.as_view(), name='school-detail')
]
