from django.urls import path
from school import views

app_name = "school"
urlpatterns = [
    path('',
         views.SchoolListCreate.as_view(),
         name="school-list"),
    path('<pk>/',
         views.SchoolRetrieveUpdateDestroy.as_view(),
         name='school-detail'
         )
]
