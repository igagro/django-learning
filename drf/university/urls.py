from django.urls import path
from university import views

urlpatterns = [
    path('', views.UniversityListCreate.as_view()),
    path('<pk>/', views.UniversityDetail.as_view(),
         name='university-detail'),
    path('<pk>/schools/', views.UniversitySchoolsList.as_view()),
    path('<pk>/schools/<pk_school>/', views.UniversitySchoolDetails.as_view())
]
