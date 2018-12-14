from django.urls import path
from university import views

urlpatterns = [
    path('', views.UniversityListCreate.as_view()),
    path('<pk>/',
         views.UniversityDetail.as_view(),
         name='university-detail'),
    path('<int:university_id>/schools/',
         views.UniversitySchoolsList.as_view()),
    path('<int:university_id>/schools/<int:school_id>/',
         views.UniversitySchoolDetails.as_view())
]
