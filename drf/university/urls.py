from django.urls import path
from university import views

app_name = 'university'
urlpatterns = [
    path('', views.UniversityListCreate.as_view(), name='university-list'),
    path('<pk>/',
         views.UniversityDetail.as_view(),
         name='university-detail'),
    path('<int:university_id>/schools/',
         views.UniversitySchoolsList.as_view(),
         name='university_schools_list'),
    path('<int:university_id>/schools/<int:school_id>/',
         views.UniversitySchoolDetails.as_view(),
         name='university_school_detail')
]
